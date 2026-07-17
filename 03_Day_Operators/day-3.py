# Day 3: Python Operators

# Arithmetic operators
num1 = 10
num2 = 3

print("Arithmetic operators")
print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =", num1 * num2)
print("num1 / num2 =", num1 / num2)
print("num1 % num2 =", num1 % num2)
print("num1 // num2 =", num1 // num2)
print("num1 ** num2 =", num1 ** num2)

# Comparison operators
print("\nComparison operators")
print("num1 > num2:", num1 > num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)

# Logical operators
print("\nLogical operators")
print(num1 > 5 and num2 < 5)
print(num1 > 5 or num2 > 5)
print(not (num1 > 5))

# Assignment operators
print("\nAssignment operators")
value = 5
value += 3
print("value += 3 ->", value)
value *= 2
print("value *= 2 ->", value)

# Identity operators
print("\nIdentity operators")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)

# Membership operators
print("\nMembership operators")
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)
print("grape" not in fruits)

# Bitwise operators
print("\nBitwise operators")
print("10 & 3 =", 10 & 3)
print("10 | 3 =", 10 | 3)
print("10 ^ 3 =", 10 ^ 3)
print("~10 =", ~10)
