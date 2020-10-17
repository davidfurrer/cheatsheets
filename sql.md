# sql concepts

[ref](https://cloud.google.com/bigquery/docs/reference/standard-sql/analytic-function-concepts#compute_a_grand_total)

## OVER

```sql
WITH Produce AS
 (SELECT 'kale' as item, 23 as purchases, 'vegetable' as category
  UNION ALL SELECT 'orange', 2, 'fruit'
  UNION ALL SELECT 'cabbage', 9, 'vegetable'
  UNION ALL SELECT 'apple', 8, 'fruit'
  UNION ALL SELECT 'leek', 2, 'vegetable'
  UNION ALL SELECT 'lettuce', 10, 'vegetable')
SELECT * FROM Produce
```

| item    | category  | purchases |
| ------- | --------- | --------- |
| kale    | vegetable | 23        |
| orange  | fruit     | 2         |
| cabbage | vegetable | 9         |
| apple   | fruit     | 8         |
| leek    | vegetable | 2         |
| lettuce | vegetable | 10        |

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER () AS total_purchases
FROM Produce
```

| item    | purchases | category  | total_purchases |
| ------- | --------- | --------- | --------------- |
| orange  | 2         | fruit     | 54              |
| leek    | 2         | vegetable | 54              |
| apple   | 8         | fruit     | 54              |
| cabbage | 9         | vegetable | 54              |
| lettuce | 10        | vegetable | 54              |
| kale    | 23        | vegetable | 54              |

## OVER and PARTITION BY

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER (
    PARTITION BY category
    ORDER BY purchases
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS total_purchases
FROM Produce
```

| item    | purchases | category  | total_purchases |
| ------- | --------- | --------- | --------------- |
| orange  | 2         | fruit     | 10              |
| apple   | 8         | fruit     | 10              |
| leek    | 2         | vegetable | 44              |
| cabbage | 9         | vegetable | 44              |
| lettuce | 10        | vegetable | 44              |
| kale    | 23        | vegetable | 44              |

## OVER with cumsum

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER (
    PARTITION BY category
    ORDER BY purchases
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS total_purchases
FROM Produce
```

| item    | purchases | category  | total_purchases |
| ------- | --------- | --------- | --------------- |
| orange  | 2         | fruit     | 2               |
| apple   | 8         | fruit     | 10              |
| leek    | 2         | vegetable | 2               |
| cabbage | 9         | vegetable | 11              |
| lettuce | 10        | vegetable | 21              |
| kale    | 23        | vegetable | 44              |

## cumsum over all items offset by 2

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER (
    ORDER BY purchases
    ROWS BETWEEN UNBOUNDED PRECEDING AND 2 PRECEDING
  ) AS total_purchases
FROM Produce;
```

| item    | purchases | category  | total_purchases |
| ------- | --------- | --------- | --------------- |
| orange  | 2         | fruit     | NULL            |
| leek    | 2         | vegetable | NULL            |
| apple   | 8         | fruit     | 2               |
| cabbage | 9         | vegetable | 4               |
| lettuce | 10        | vegetable | 12              |
| kale    | 23        | vegetable | 21              |

## Moving Average

```sql
SELECT item, purchases, category, AVG(purchases)
  OVER (
    ORDER BY purchases
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) AS avg_purchases
FROM Produce
```

| item    | purchases | category  | avg_purchases |
| ------- | --------- | --------- | ------------- |
| orange  | 2         | fruit     | 2             |
| leek    | 2         | vegetable | 4             |
| apple   | 8         | fruit     | 6.33333       |
| cabbage | 9         | vegetable | 9             |
| lettuce | 10        | vegetable | 14            |
| kale    | 23        | vegetable | 16.5          |

## Compute the number of items within a range

```sql
SELECT animal, population, category, COUNT(*)
  OVER (
    ORDER BY population
    RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) AS similar_population
FROM Farm;
```

e.g. first row:

(goose, dog, ox, goat, duck, cat) = 4 animals between population range 0-2.

| animal | population | category | similar_population |
| ------ | ---------- | -------- | ------------------ |
| goose  | 1          | bird     | 4                  |
| dog    | 2          | mammal   | 5                  |
| ox     | 2          | mammal   | 5                  |
| goat   | 2          | mammal   | 5                  |
| duck   | 3          | bird     | 4                  |
| cat    | 23         | mammal   | 1                  |

## Get the most popular item in each category

```sql
SELECT item, purchases, category, LAST_VALUE(item)
  OVER (
    PARTITION BY category
    ORDER BY purchases
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS most_popular
FROM Produce
```

| item    | purchases | category  | most_popular |
| ------- | --------- | --------- | ------------ |
| orange  | 2         | fruit     | apple        |
| apple   | 8         | fruit     | apple        |
| leek    | 2         | vegetable | kale         |
| cabbage | 9         | vegetable | kale         |
| lettuce | 10        | vegetable | kale         |
| kale    | 23        | vegetable | kale         |

## Get the last value in a range

```sql
SELECT item, purchases, category, LAST_VALUE(item)
  OVER (
    PARTITION BY category
    ORDER BY purchases
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) AS most_popular
FROM Produce
```

| item    | purchases | category  | most_popular |
| ------- | --------- | --------- | ------------ |
| orange  | 2         | fruit     | apple        |
| apple   | 8         | fruit     | apple        |
| leek    | 2         | vegetable | cabbage      |
| cabbage | 9         | vegetable | lettuce      |
| lettuce | 10        | vegetable | kale         |
| kale    | 23        | vegetable | kale         |

alternatively:

```sql
SELECT item, purchases, category, LAST_VALUE(item)
  OVER (
    item_window
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) AS most_popular
FROM Produce
WINDOW item_window AS (
  PARTITION BY category
  ORDER BY purchases)
```

## Compute rank

```sql
SELECT name, department, start_date,
  RANK() OVER (PARTITION BY department ORDER BY start_date) AS rank
FROM Employees;
```

| name     | department | start_date | rank |
| -------- | ---------- | ---------- | ---- |
| Jacob    | 1          | 1990-07-11 | 1    |
| Anthony  | 1          | 1995-11-29 | 2    |
| Andrew   | 1          | 1999-01-23 | 3    |
| Isabella | 2          | 1997-09-28 | 1    |
| Daniel   | 2          | 2004-06-24 | 2    |
| Jose     | 2          | 2013-03-17 | 3    |

## named window function in a window frame clause

```sql
SELECT item, purchases, category, LAST_VALUE(item)
  OVER (item_window) AS most_popular
FROM Produce
WINDOW item_window AS (
  PARTITION BY category
  ORDER BY purchases
  ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING)
```

| item    | purchases | category  | most_popular |
| ------- | --------- | --------- | ------------ |
| orange  | 2         | fruit     | apple        |
| apple   | 8         | fruit     | apple        |
| leek    | 2         | vegetable | lettuce      |
| cabbage | 9         | vegetable | kale         |
| lettuce | 10        | vegetable | kale         |
| kale    | 23        | vegetable | kale         |

alternatively:

```sql
SELECT item, purchases, category, LAST_VALUE(item)
  OVER (item_window) AS most_popular
FROM Produce
WINDOW
  a AS (PARTITION BY category),
  b AS (a ORDER BY purchases),
  c AS (b ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING),
  item_window AS (c)
```

# Userdefined functions (UDF)

```sql
CREATE TEMP FUNCTION addFourAndDivide(x INT64, y INT64) AS ((x + 4) / y);
WITH numbers AS
  (SELECT 1 as val
  UNION ALL
  SELECT 3 as val
  UNION ALL
  SELECT 4 as val
  UNION ALL
  SELECT 5 as val)
SELECT val, addFourAndDivide(val, 2) AS result
FROM numbers;
```

| val | result |
| --- | ------ |
| 1   | 2.5    |
| 3   | 3.5    |
| 4   | 4      |
| 5   | 4.5    |

```sql
CREATE TEMP FUNCTION addFourAndDivideAny(x ANY TYPE, y ANY TYPE) AS (
  (x + 4) / y
);

SELECT addFourAndDivideAny(3, 4) AS integer_output,
       addFourAndDivideAny(1.59, 3.14) AS floating_point_output;
```

| integer_output | floating_point_output |
| -------------- | --------------------- |
| 1.75           | 1.7802547770700636    |

The following example shows a SQL UDF that uses a templated parameter to return the last element of an array of any type:

```sql
CREATE TEMP FUNCTION lastArrayElement(arr ANY TYPE) AS (
  arr[ORDINAL(ARRAY_LENGTH(arr))]
);

SELECT
  names[OFFSET(0)] AS first_name,
  lastArrayElement(names) AS last_name
FROM (
  SELECT ['Fred', 'McFeely', 'Rogers'] AS names UNION ALL
  SELECT ['Marie', 'Skłodowska', 'Curie']
);
```

| first_name | last_name |
| ---------- | --------- |
| Fred       | Rogers    |
| Marie      | Curie     |


# joins

## inner joins

```sql
FROM A INNER JOIN B ON A.w = B.y
```


Table A       Table B       Result

| w | x |  * | | y | z |  =| | w | x | y | z |
| -- | -- | - |- | -- | --- |-- | - | -- | -- |-- |-- |
| 1 | a |  |   | 2 | k |  |   | 2 | b | 2 | k |
| 2 | b |  |   | 3 | m |    | | 3 | c | 3 | m |
| 3 | c |  |   | 3 | n |  |   | 3 | c | 3 | n |
| 3 | d |  |   | 4 | p |  |   | 3 | d | 3 | m |
||||||    |    |                            | 3 | d | 3 | n |


if join columns are called same:

```sql
FROM A INNER JOIN B USING (x)
```

## Faltten array columns

```sql
FROM A CROSS JOIN A.y
```

Table A                    
    
| w | x | y         |  
   | -- |-- |-- | 
| 1 | a | [P, Q]    |      
| 2 | b | [R, S, T] |      
    
                           
                           
                           
Result

| w | x | y |
| -- |-- |-- |
| 1 | a | P |
| 1 | a | Q |
| 2 | b | R |
| 2 | b | S |
| 2 | b | T |

## Cross join

```sql
SELECT Roster.LastName, TeamMascot.Mascot
FROM Roster CROSS JOIN TeamMascot;
```

|Roster|TeamMascot|
|--|--|
|<table> <thead> <tr> <th>LastName </th> <th>SchoolID </th> </tr> </thead> <tbody> <tr> <td>Adams </td> <td>50 </td> </tr> <tr> <td>Buchanan</td> <td>52 </td> </tr> <tr> <td>Coolidge</td> <td>52 </td> </tr> <tr> <td>Davis </td> <td>51 </td> </tr> <tr> <td>Eisenhower </td> <td>77 </td> </tr> </tbody> </table>|<table> <thead> <tr> <th>SchoolID </th> <th>Mascot </th> </tr> </thead> <tbody> <tr> <td>50 </td> <td>Jaguars </td> </tr> <tr> <td>51</td> <td>Knights </td> </tr> <tr> <td>52</td> <td>Lakers </td> </tr> <tr> <td>53 </td> <td>Mustangs </td> </tr> </tbody> </table>|


Result:

| LastName   | Mascot       |
|--|--|
| Adams      | Jaguars      |
| Adams      | Knights      |
| Adams      | Lakers       |
| Adams      | Mustangs     |
| Buchanan   | Jaguars      |
| Buchanan   | Knights      |
| Buchanan   | Lakers       |
| Buchanan   | Mustangs     |
| ...                       |

