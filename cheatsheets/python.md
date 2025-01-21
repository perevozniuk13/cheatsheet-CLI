# Python Cheat Sheet
## DATA TYPES
```python
# Integer
x = 10
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Float
x = 3.14
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# String
str = "Hello, World!"
print(len(str)) # prints out 12
print(str[2:5]) # string slicing (prints out 'llo')
multi_string = """Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit """
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
text = " hello world "
print(text.strip())  # => "hello world"
print(text.upper())  # => " HELLO WORLD "


# Boolean
flag1 = True
flag2 = False

# List
mylist = []
mylist.append(1) # adds number 1 to the list
mylist.append(2) # adds number 2 to the list
for item in mylist:
    print(item) # prints out 1,2

mylist[start:end] # list slicing
mylist[start:end:step]  # list slicing with a step
mylist.pop() # removes the last element from the list and returns that removed element
del mylist[0] # deletes the first element from the list

mylist.sort() # sorts the list (sorted(mylist) also works)
mylist.reverse() # reverses the list (reversed(mylist) also works)
mylist.count(element) # counts occurences of 'element' in list 'mylist'

list2 = ["re"] * 3
print(list2) # prints out ['re', 're', 're']




# Tuple (Similar to List but immutable)
my_tuple = (1, 2, 3)
my_tuple = tuple((1, 2, 3))

# Set (Set of unique items/objects)
set1 = {"a", "b", "c"}   
set2 = set(("a", "b", "c"))

# Dictionary (Key: Value pair, JSON like object)
empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
print(a["one"]) # prints out 1
print(a.keys()) # prints out dict_keys(['one', 'two', 'three'])
print(a.values()) # prints out dict_values([1, 2, 3])
a.update({"four": 4}) # insert pair into the dictionary


```

## IF - ELSE
```python
# basic
num = 5
if num > 10:
    print("num is totally bigger than 10.")
elif num < 10:
    print("num is smaller than 10.")
else:
    print("num is indeed 10.")


# one-line
r = "a" if a > b else "b"
```

## LOOPS
```python
# Basic
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# With index
animals = ["dog", "cat", "mouse"]
# enumerate() adds counter to an iterable
for i, value in enumerate(animals):
    print(i, value)

# While
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1

# Range
for i in range(4):
    print(i) # Prints: 0 1 2 3

for i in range(4, 8):
    print(i) # Prints: 4 5 6 7

for i in range(4, 10, 2):
    print(i) # Prints: 4 6 8

```

## FUNCTIONS
```python 
# Basic
def my_function():
    print("Hello from a function")

my_function() # calls the function
```

## FILE HANDLING
```python 
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)
```

## ARITHMETIC
```python
result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125
# The / means quotient of x and y, and the // means floored quotient of x and y
```

## CLASSES & INHERITANCE
```python
class Animal: 
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        
class Dog(Animal): # Dog class inherits name and legs from Animal class
    def sound(self): # Method of the class
        print("Woof!")
 
Yoki = Dog("Yoki", 4) # Class Instantiation
print(Yoki.name) # => YOKI
print(Yoki.legs) # => 4
Yoki.sound()     # => Woof!
```

## STRING INTERPOLATION
```python
name = 'John'
print(f"Hello, {name}!") # prints out 'Hello, John!'
```
## LIST COMPREHENSION
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # prints out ['apple', 'banana', 'mango']
```

## ERROR HANDLING
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution continues...")
```
