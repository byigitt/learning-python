# Integer
age = 25

# Float
price = 19.99

# String
name = "John Doe"

# Boolean
is_active = True

# Single quotes
string1 = 'Hello world'

# Double quotes
string2 = "Hello world"

# Triple quotes (for multi-line strings)
string3 = """Hello 
world"""

x = 10
y = 5

# Operators

addition = x + y
substraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponent = x ** y
floor_division = x // y 

# Comparisons

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators

a = True
b = False

print(x and y) # False
print(x or y) # True
print(not x) # False

# Collections (arrays)
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])

# Modifying elements 
fruits[1] = "blueberry"

# Adding elements
fruits.append("orange")

# Removing elements
fruits.remove("cherry")

# Tuples (its immutable, not changable)
coordinates = (10, 20)

# Accesing to a tuple
print(coordinates[0])

# Sets (are unordered and do not allow duplicate values)
unique_numbers = {1, 2, 3, 4, 4}

# Adding elements
unique_numbers.add(5)

# Removing elements
unique_numbers.remove(3)

# Dictionaries
person = {
  "name": "Alice",
  "age": 30,
  "city": "New York"
}

# Accesing elements
print(person["name"])

# Modifying elements
person["age"] = 31

# Adding elements
person["email"] = "alice@example.com"

# Removing elements
del person["city"]

# If-Else Statements
if x > 5:
  print("x is greater than 5")
else:
  print("x is less than or equal to 5")

# For Loops
for fruit in fruits:
  print(fruit)

for i in range(5):
  print(i)