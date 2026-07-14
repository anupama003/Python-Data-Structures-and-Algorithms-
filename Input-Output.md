# Python Basic Input/Output

## Introduction
When you start learning Python, it’s important to focus on the basics first. Input and Output (I/O) are fundamental concepts. Let’s walk through how input and output work in Python.

### Including Libraries:
In Python, pre-built functions and tools are bundled into **modules**. You use the `import` keyword to include them. However, for basic I/O, Python has built-in functions, so you don't need to import anything!
* `import math` → used for mathematical functions.

```python
# No setup required! Your code runs directly.
print("Hello World")
```

---

## Output with print()
To print output, we use the built-in `print()` function.

```python
print("Hey there!")
```
**Output:** `Hey there!`

---

## Printing on Multiple Lines
In Python, every `print()` statement automatically adds a newline at the end by default.

```python
print("Hey, there!")
print("Hey, there!")
```
**Output:**
```text
Hey, there!
Hey, there!
```

### Changing the End Behavior
If you want to print without moving to a new line, you can change the `end` parameter of the `print()` function. 

```python
print("Hey, there!", end=" ")
print("Hey, there!", end="")
```
**Output:** `Hey, there! Hey, there!`

### Using \n vs Default print
* `\n` → inserts a newline character manually inside a string.
* By default, `print()` uses `end="\n"`. Python automatically handles buffer flushing for standard console output.

```python
print("Hey, there!\nHey, there!")
```

---

## Taking User Input with input()
The `input()` function is used to take input from the user. It always reads input as a **string**. If you need a number, you must explicitly convert it using type casting like `int()`.

```python
# Taking an integer input
x = int(input())
print("Value of x:", x)
```
**Input:** `10`  
**Output:** `Value of x: 10`

---

## Multiple Inputs
In Python, `input()` reads the whole line at once. To split space-separated values, we use the `.split()` method combined with `map()`.

```python
# Taking two space-separated integers
x, y = map(int, input().split())
print("Value of x:", x, "and y:", y)
```
**Input:** `10 20`  
**Output:** `Value of x: 10 and y: 20`

--- 

* Python automatically loads its massive library of built-in functions (like `print()`, `input()`, `len()`, `max()`, `min()`, `sum()`) on startup.
* You never need to pre-import basic data structures like arrays (Lists), sets, maps (Dictionaries), or stacks. They are always available out of the box!
