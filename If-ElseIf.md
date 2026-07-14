# Python Conditional Statements: If-Else and Elif

## Introduction
Conditional statements are a fundamental concept in programming that allow you to make decisions based on certain conditions. These statements enable your code to execute different blocks of code depending on whether specific conditions are met or not. 

In Python, we handle decision-making using `if`, `elif`, and `else` statements.

---

## The `if-else` Statement

* **`if` statement:** Used to execute a block of code only if a certain condition is met (`True`).
* **`else` statement:** An optional companion that specifies what code to execute if the `if` condition is not met (`False`).

### Flow of Control:
1. If the condition in the `if` statement evaluates to `True`, the code inside the `if` block executes.
2. If the condition evaluates to `False`, the code inside the `else` block executes.

```python
# Ask the user for their age
age = int(input("Enter your age: "))  # input() reads as a string, so convert to integer

# Check if the entered age is greater than or equal to 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

---

## Checking Multiple Conditions with `elif`

As your code becomes more complex, you'll often encounter scenarios where you need to check multiple conditions sequentially. Instead of writing multiple independent `if` statements, Python uses the `elif` (short for *else if*) statement to create an **if-elif-else ladder**.

Let's look at a grading system example:

```python
# Declare and initialize marks variable
marks = 54

# Check grade conditions using if-elif-else ladder
if marks < 25:
    print("Grade: F")
elif marks >= 25 and marks <= 44:
    print("Grade: E")
elif marks >= 45 and marks <= 49:
    print("Grade: D")
elif marks >= 50 and marks <= 59:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: B")
elif marks >= 70 and marks <= 100:
    print("Grade: A")
else:
    print("Invalid marks entered.")
```

---

## Refactoring for Better Readability (Python Optimization)

The grading code above works fine, but it contains redundant comparisons. For example, checking `marks >= 25` in the second block is unnecessary because if `marks` were less than 25, the first `if` statement would have already caught it.

Because Python executes an `if-elif-else` ladder from **top to bottom**, we can safely remove the lower-bound checks. Here is the optimized, clean, and highly readable version:

```python
marks = 54

# Refactored and optimized grading logic
if marks < 0 or marks > 100:
    print("Invalid marks entered.")  # Early exit for boundary errors
elif marks < 25:
    print("Grade: F")
elif marks <= 44:
    print("Grade: E")
elif marks <= 49:
    print("Grade: D")
elif marks <= 59:
    print("Grade: C")
elif marks <= 69:
    print("Grade: B")
else:
    print("Grade: A")
```

### Why this is better:
* **Cleaner Code:** Removes clutter like repetitive `and` keywords.
* **Safer Execution:** Validates bad inputs first (e.g., negative numbers or scores over 100).
* **Easier Maintenance:** If grade ranges change, you only need to update a single value per line.
