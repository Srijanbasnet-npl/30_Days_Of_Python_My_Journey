# Day 3: Operators in Python

Today we learned about different types of operators in Python.

## 1. Arithmetic Operators

These operators are used to perform mathematical operations.

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `%` modulus
- `//` floor division
- `**` exponentiation

Example:

```python
num1 = 10
num2 = 3

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)
print(num1 ** num2)
```

## 2. Comparison Operators

These compare two values and return a Boolean result.

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

Example:

```python
print(10 > 3)
print(10 == 3)
print(10 != 3)
```

## 3. Logical Operators

These are used to combine conditional statements.

- `and`
- `or`
- `not`

Example:

```python
print(10 > 5 and 3 < 5)
print(10 > 5 or 3 > 5)
print(not (10 > 5))
```

## 4. Assignment Operators

These assign values to variables.

- `=` assign
- `+=` add and assign
- `-=` subtract and assign
- `*=` multiply and assign
- `/=` divide and assign

Example:

```python
value = 5
value += 3
print(value)
```

## 5. Identity Operators

These check whether two variables refer to the same object.

- `is`
- `is not`

Example:

```python
a = [1, 2, 3]
b = a
print(a is b)
```

## 6. Membership Operators

These check whether a value exists in a sequence.

- `in`
- `not in`

Example:

```python
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)
```

## 7. Bitwise Operators

These work on binary numbers.

- `&` AND
- `|` OR
- `^` XOR
- `~` NOT
- `<<` left shift
- `>>` right shift

Example:

```python
print(10 & 3)
print(10 | 3)
print(10 ^ 3)
```

## Summary

Operators are symbols that perform operations on values and variables in Python.
