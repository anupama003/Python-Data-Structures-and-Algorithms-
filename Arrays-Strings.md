# Python Basics: Lists (Arrays) and Strings

## What is an Array (Python List)?
In Python, standard arrays are implemented using **Lists**. A list is a linear data structure that stores a collection of items. You can randomly access any data in a list instantly using its index value.

```python
# A simple list in Python
my_list = [10, 20, 30, 40]
```

### Key Characteristics of Python Lists:
* **Contiguous Memory:** Like arrays in other languages, Python lists store references to elements next to each other in memory blocks, making data retrieval exceptionally fast.
* **Dynamic Sizing:** Unlike C++ arrays, you do not need to specify a size when creating a Python list. It automatically shrinks or grows as you add or remove elements.
* **Heterogeneous Data:** In many languages, arrays can only hold one data type (homogeneous). Python lists are highly flexible and can hold multiple data types at once (heterogeneous).

```python
# Python lists can hold different data types together
mixed_list = [1, "hello", True, 3.14]
```

---

## Why are Lists ‘0’ Indexed?
Counting from index `0` simplifies internal memory calculations for the computer. 

* The first element is at index `0`.
* A list of length `n` has indexes ranging from `0` to `n-1`.

```text
List:    [ "A",  "B",  "C",  "D" ]
Index:     0     1     2     3
```

---

## Finding and Modifying Elements

### 1. Accessing and Updating (O(1) Constant Time)
If you know the index, finding or changing an element is instant.

```python
numbers = [10, 20, 30, 40]

# Accessing
print(numbers[0])  # Output: 10

# Updating
numbers[1] = 99
print(numbers)     # Output: [10, 99, 30, 40]
```

### 2. Inserting Elements
* **At the end (O(1)):** Appending an element to the end of a list is incredibly fast.
* **In the middle/start (O(n)):** Inserting in the middle requires shifting all subsequent elements, which takes more time.

```python
items = [1, 2, 3]

# Fast insertion at the end
items.append(4)        # [1, 2, 3, 4]

# Slower insertion at index 1
items.insert(1, 99)    # [1, 99, 2, 3, 4]
```

### 3. Removing Elements
* **By Index:** Using `pop()` removes an item at a specific index. Removing from the end is `O(1)`.
* **By Value:** Using `remove()` searches for the item first, which takes `O(n)` time.

```python
items = [10, 20, 30, 40]

items.pop()        # Removes 40 from the end (Fast)
items.remove(20)   # Searches and removes 20
```

---

## What are Strings?
Strings in Python are sequences of characters enclosed in single or double quotes. Like lists, strings follow **0-based indexing**.

```python
h = "hello"
print(h[0])  # Output: 'h'
print(h[1])  # Output: 'e'
```

### Strings are Immutable!
Unlike C++, Python strings are **immutable**. This means you cannot change an individual character of a string in place.

```python
h = "hello"
# h[0] = 'M'  <-- This will throw a TypeError!

# Correct way: Create a new string
h = "M" + h[1:] 
print(h)      # Output: Mello
```

---

## Finding the Length of a String or List
In Python, you do not use `.size()` or `.length()`. Instead, you use the built-in global `len()` function.

```python
my_string = "hello"
my_list = [1, 2, 3, 4, 5]

print(len(my_string))  # Output: 7
print(len(my_list))    # Output: 5
```

---

## String Comparison
Python makes string comparison incredibly straightforward using standard comparison operators. You do not need any special methods or helper classes.

* `==` checks if two strings are identical in value.
* `!=` checks if two strings are completely different.

```python
# Simple comparison function inside a class
class Solution:
    def compare_strings(self, str1: str, str2: str) -> bool:
        # Returns True if strings are exactly equal, otherwise False
        return str1 == str2

# Driver code
if __name__ == "__main__":
    # Taking string inputs
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    obj = Solution()

    if obj.compare_strings(string1, string2):
        print("Strings are equal")
    else:
        print("Strings are not equal")
```
