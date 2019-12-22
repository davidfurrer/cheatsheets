# Higher Order Functions

## ForEach

### Plain JS

```javascript
for (let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}
```

### ForEach

```javascript
companies.forEach(function(company) {
  console.log(company.name);
});
```

### Arrow Function

```javascript
```

## Filter

### Plain JS

```javascript
let canDrink = [];
for (let i = 0; i < ages.length; i++) {
  if (ages[i] >= 21) {
    canDrink.push(ages[i]);
  }
}
```

### Filter

```javascript
const canDrink = ages.filter(function(age) {
  if (age >= 21) {
    return true;
  }
});
```

### Arrow Function

```javascript
const canDrink = ages.filter(age => age >= 21);
```

## map

### Plain JS

```javascript
```

### map

```javascript
const companyNames = companies.map(function(company) {
  return company.name;
});
```

### Arrow Function

```javascript
for (let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}
```

## reduce

### Plain JS

```javascript
for (let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}
```

### reduce

```javascript
for (let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}
```

### Arrow Function

```javascript
for (let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}
```
