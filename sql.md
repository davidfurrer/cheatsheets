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


| item      | category   | purchases  |
| --------- | ---------- | ---------- |
| kale      | vegetable  | 23         |
| orange    | fruit      | 2          |
| cabbage   | vegetable  | 9          |
| apple     | fruit      | 8          |
| leek      | vegetable  | 2          |
| lettuce   | vegetable  | 10         |

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER () AS total_purchases
FROM Produce
```

| item      | purchases  | category   | total_purchases |
| --------- | ---------- | ---------- | ---------- |
| orange    | 2          | fruit      | 54              |
| leek      | 2          | vegetable  | 54              |
| apple     | 8          | fruit      | 54              |
| cabbage   | 9          | vegetable  | 54              |
| lettuce   | 10         | vegetable  | 54              |
| kale      | 23         | vegetable  | 54              |

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


| item      | purchases  | category   | total_purchases |
| --------- | ---------- | ---------- | ---------- |
| orange    | 2          | fruit      | 10              |
| apple     | 8          | fruit      | 10              |
| leek      | 2          | vegetable  | 44              |
| cabbage   | 9          | vegetable  | 44              |
| lettuce   | 10         | vegetable  | 44              |
| kale      | 23         | vegetable  | 44              |


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

| item      | purchases  | category   | total_purchases |
| --------- | ---------- | ---------- | ---------- |
| orange    | 2          | fruit      | 2               |
| apple     | 8          | fruit      | 10              |
| leek      | 2          | vegetable  | 2               |
| cabbage   | 9          | vegetable  | 11              |
| lettuce   | 10         | vegetable  | 21              |
| kale      | 23         | vegetable  | 44              |



## cumsum over all items offset by 2

```sql
SELECT item, purchases, category, SUM(purchases)
  OVER (
    ORDER BY purchases
    ROWS BETWEEN UNBOUNDED PRECEDING AND 2 PRECEDING
  ) AS total_purchases
FROM Produce;
```

| item      | purchases  | category   | total_purchases |
| --------- | ---------- | ---------- | ---------- |
| orange    | 2          | fruit      | NULL            |
| leek      | 2          | vegetable  | NULL            |
| apple     | 8          | fruit      | 2               |
| cabbage   | 9          | vegetable  | 4               |
| lettuce   | 10         | vegetable  | 12              |
| kale      | 23         | vegetable  | 21              |


## Moving Average

```sql
SELECT item, purchases, category, AVG(purchases)
  OVER (
    ORDER BY purchases
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) AS avg_purchases
FROM Produce
```

| item      | purchases  | category   | avg_purchases   |
| --------- | ---------- | ---------- | ---------- |
| orange    | 2          | fruit      | 2               |
| leek      | 2          | vegetable  | 4               |
| apple     | 8          | fruit      | 6.33333         |
| cabbage   | 9          | vegetable  | 9               |
| lettuce   | 10         | vegetable  | 14              |
| kale      | 23         | vegetable  | 16.5            |
