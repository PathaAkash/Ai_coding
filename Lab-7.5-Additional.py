
# =========== MUTABLE DEFAULT ARGUMENT BUG ===========

# ❌ BUGGY CODE - Shared list problem
print("=== BUGGY CODE ===")
def add_item_buggy(item, items=[]):
    """
    BUG: items=[] is created ONCE when function is defined,
    not each time the function is called. All calls share the SAME list!
    """
    items.append(item)
    return items

print("Call 1:", add_item_buggy(1))      # [1]
print("Call 2:", add_item_buggy(2))      # [1, 2] - BUG! Should be [2]
print("Call 3:", add_item_buggy(3))      # [1, 2, 3] - BUG! Should be [3]


print("\n=== FIXED CODE ===")
# ✅ FIXED CODE - Use None as default
def add_item_fixed(item, items=None):
    """
    SOLUTION: Use None as default, create new list each time function is called
    """
    if items is None:
        items = []
    items.append(item)
    return items

print("Call 1:", add_item_fixed(1))      # [1]
print("Call 2:", add_item_fixed(2))      # [2] - Correct!
print("Call 3:", add_item_fixed(3))      # [3] - Correct!


print("\n=== ALTERNATIVE FIX (Using list factory) ===")
# ✅ ALTERNATIVE FIX - Use factory function
from typing import List

def add_item_alternative(item, items: List = None):
    """Alternative way using list() constructor"""
    if items is None:
        items = []
    items.append(item)
    return items

print("Call 1:", add_item_alternative(10))  # [10]
print("Call 2:", add_item_alternative(20))  # [20]
print("Call 3:", add_item_alternative(30))  # [30]


print("\n=== COMPARISON: Persistent vs New List ===")
# If you WANT to persist the list (intentional behavior)
persistent_list = []

def add_item_persistent(item, items=None):
    """Use external list for persistence"""
    if items is None:
        items = persistent_list
    items.append(item)
    return items

print("Persistent Call 1:", add_item_persistent(100))  # [100]
print("Persistent Call 2:", add_item_persistent(200))  # [100, 200]
print("Persistent Call 3:", add_item_persistent(300))  # [100, 200, 300]


# ===== FLOATING-POINT PRECISION ERROR =====

# ❌ BUGGY CODE
def check_sum_buggy():
    return (0.1 + 0.2) == 0.3

print("BUGGY CODE:")
print(f"0.1 + 0.2 == 0.3: {check_sum_buggy()}")  # False - BUG!
print(f"Actual value: {0.1 + 0.2}")               # 0.30000000000000004


# ✅ FIXED CODE - Using Tolerance
def check_sum_fixed(tolerance=1e-9):
    return abs((0.1 + 0.2) - 0.3) < tolerance

print("\nFIXED CODE:")
print(f"0.1 + 0.2 ≈ 0.3: {check_sum_fixed()}")  # True - Correct!


# ✅ ALTERNATIVE FIX - Using math.isclose()
import math

def check_sum_isclose():
    return math.isclose(0.1 + 0.2, 0.3)

print("\nALTERNATIVE FIX (using math.isclose):")
print(f"0.1 + 0.2 ≈ 0.3: {check_sum_isclose()}")  # True - Correct!






# ===== TASK 3: RECURSION ERROR – MISSING BASE CASE =====

# ❌ BUGGY CODE (causes RecursionError)
# def countdown_buggy(n):
#     print(n)
#     return countdown_buggy(n-1)  # No base case!
# countdown_buggy(5)  # Would crash with RecursionError


# ✅ FIXED CODE
def countdown(n):
    if n < 0:  # BASE CASE - stop condition
        return
    print(n)
    countdown(n - 1)

countdown(5)



# ===== TASK 4: DICTIONARY KEY ERROR =====

# ❌ BUGGY CODE
print("❌ BUGGY CODE (causes KeyError):")
def get_value_buggy():
    data = {"a": 1, "b": 2}
    return data["c"]  # KeyError: 'c' doesn't exist!

# Uncomment to see error:
# print(get_value_buggy())


# ✅ FIXED CODE - Method 1: Using .get()
print("\n✅ FIXED CODE - Method 1: Using .get()")
def get_value_with_get():
    data = {"a": 1, "b": 2}
    return data.get("c")  # Returns None if key doesn't exist

print(f"Value: {get_value_with_get()}")  # None


 
 # ✅ FIXED CODE - Method 2: Using .get() with default value
 print("\n✅ FIXED CODE - Method 2: With default value")
 def get_value_with_default():
     data = {"a": 1, "b": 2}
     return data.get("c", "Key not found!")  # Default value
 
 print(f"Value: {get_value_with_default()}")  # Key not found!
 
 
 # ✅ FIXED CODE - Method 3: Using try-except
 print("\n✅ FIXED CODE - Method 3: Try-except")
 def get_value_with_try_except():
     data = {"a": 1, "b": 2}
     try:
         return data["c"]
     except KeyError:
         return "Key doesn't exist"
 
 print(f"Value: {get_value_with_try_except()}")  # Key doesn't exist
 
 
 # ✅ FIXED CODE - Method 4: Check if key exists
 print("\n✅ FIXED CODE - Method 4: Check before access")
 def get_value_with_check():
     data = {"a": 1, "b": 2}
     if "c" in data:
         return data["c"]
     else:
         return "Key not found"
 
 print(f"Value: {get_value_with_check()}")  # Key not found
 
 
 # ===== TASK 5: INFINITE LOOP – WRONG CONDITION =====
 
 # ❌ BUGGY CODE (causes infinite loop)
 print("❌ BUGGY CODE (infinite loop):")
 # def loop_example_buggy():
 #     i = 0
 #     while i < 5:
 #         print(i)  # i never increments!
 # loop_example_buggy()  # Would loop forever!
 
 
 # ✅ FIXED CODE - Method 1: Increment inside loop
 print("\n✅ FIXED CODE - Method 1: Increment i")
 def loop_example_fixed():
     i = 0
     while i < 5:
         print(i)
         i += 1  # Increment i!
 
 loop_example_fixed()
 
 
 # ✅ FIXED CODE - Method 2: Using for loop
 print("\n✅ FIXED CODE - Method 2: Using for loop")
 def loop_example_for():
     for i in range(5):
         print(i)
 
 loop_example_for()
 
 
 
 
 # ===== TASK 6: UNPACKING ERROR – WRONG VARIABLES =====
 
 # ❌ BUGGY CODE (causes ValueError)
 print("❌ BUGGY CODE (too many values to unpack):")
 # a, b = (1, 2, 3)  # ValueError: too many values to unpack!
 
 
 # ✅ FIXED CODE - Method 1: Unpack all values
 print("\n✅ FIXED CODE - Method 1: Unpack all values")
 a, b, c = (1, 2, 3)
 print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3
 
 
 # ✅ FIXED CODE - Method 2: Use underscore to ignore extra values
 print("\n✅ FIXED CODE - Method 2: Ignore extra values with _")
 a, b, _ = (1, 2, 3)
 print(f"a={a}, b={b}")  # a=1, b=2
 
 
 # ✅ FIXED CODE - Method 3: Use * to capture remaining values
 print("\n✅ FIXED CODE - Method 3: Capture remaining with *")
 a, b, *rest = (1, 2, 3, 4, 5)
 print(f"a={a}, b={b}, rest={rest}")  # a=1, b=2, rest=[3, 4, 5]
 
 
 # ✅ FIXED CODE - Method 4: Unpack with * in middle
 print("\n✅ FIXED CODE - Method 4: Unpack with * in middle")
 a, *middle, z = (1, 2, 3, 4, 5)
 print(f"a={a}, middle={middle}, z={z}")  # a=1, middle=[2, 3, 4], z=5
 
 
 
 # ===== TASK 7: MIXED INDENTATION – TABS VS SPACES =====
 
 # ❌ BUGGY CODE (causes IndentationError)
 print("❌ BUGGY CODE (mixed indentation):")
 # def func_buggy():
 #     x = 5
 #         y = 10  # Extra indentation - MIXED!
 #     return x+y
 # func_buggy()  # IndentationError!
 
 
 # ✅ FIXED CODE - Consistent 4-space indentation
 print("\n✅ FIXED CODE - Consistent indentation")
 def func_fixed():
     x = 5
     y = 10
     return x + y
 
 result = func_fixed()
 print(f"Result: {result}")  # Result: 15
 
 
 # ✅ FIXED CODE - With nested blocks
 print("\n✅ FIXED CODE - Nested blocks with consistent indentation")
 def calculate(a, b):
     if a > 0:
         sum_val = a + b
         product = a * b
         return sum_val, product
     else:
         return 0, 0
 
 sum_result, prod_result = calculate(3, 4)
 print(f"Sum: {sum_result}, Product: {prod_result}")  # Sum: 7, Product: 12
 
 
 # ✅ FIXED CODE - Loops with consistent indentation
 print("\n✅ FIXED CODE - Loops with consistent indentation")
 def loop_example():
     total = 0
     for i in range(1, 6):
         total += i
     return total
 
 print(f"Total: {loop_example()}")  # Total: 15
 
 # ===== TASK 8: IMPORT ERROR – WRONG MODULE USAGE =====
 
 # ❌ BUGGY CODE (causes ModuleNotFoundError)
 print("❌ BUGGY CODE (module not found):")
 # import maths  # ModuleNotFoundError: No module named 'maths'
 # print(maths.sqrt(16))
 
 
 # ✅ FIXED CODE - Correct module name
 print("\n✅ FIXED CODE - Correct import")
 import math
 print(f"sqrt(16) = {math.sqrt(16)}")  # sqrt(16) = 4.0
 
 
 # ✅ FIXED CODE - Alternative: from import
 print("\n✅ FIXED CODE - Using 'from' import")
 from math import sqrt, ceil, floor
 print(f"sqrt(25) = {sqrt(25)}")  # sqrt(25) = 5.0
 print(f"ceil(4.3) = {ceil(4.3)}")  # ceil(4.3) = 5
 print(f"floor(4.8) = {floor(4.8)}")  # floor(4.8) = 4
 
 
 # ✅ FIXED CODE - Using alias
 print("\n✅ FIXED CODE - Using alias for convenience")
 import math as m
 print(f"pi = {m.pi}")  # pi = 3.14159...
 print(f"sin(0) = {m.sin(0)}")  # sin(0) = 0.0
 
 
 # ✅ FIXED CODE - Common math functions
 print("\n✅ FIXED CODE - Common math functions")
 import math
 numbers = [16, 25, 36, 49]
 for num in numbers:
     print(f"sqrt({num}) = {math.sqrt(num)}")
     
     
 # ===== TASK 9: UNREACHABLE CODE – RETURN INSIDE LOOP =====
 
 # ❌ BUGGY CODE (returns early, doesn't process all items)
 print("❌ BUGGY CODE (returns on first iteration):")
 def total_buggy(numbers):
     for n in numbers:
         return n  # Returns immediately on first item!
     # Rest of loop never executes!
 
 print(f"Result: {total_buggy([1, 2, 3])}")  # Result: 1 (Only first item!)
 
 
 # ✅ FIXED CODE - Method 1: Accumulate then return
 print("\n✅ FIXED CODE - Method 1: Accumulate sum")
 def total_fixed(numbers):
     total_sum = 0
     for n in numbers:
         total_sum += n
     return total_sum  # Return AFTER loop completes
 
 print(f"Result: {total_fixed([1, 2, 3])}")  # Result: 6
 
 
 # ✅ FIXED CODE - Method 2: Using built-in sum()
 print("\n✅ FIXED CODE - Method 2: Using sum()")
 def total_simple(numbers):
     return sum(numbers)
 
 print(f"Result: {total_simple([1, 2, 3])}")  # Result: 6
 
 
 # ✅ FIXED CODE - Method 3: Return list of all items
 print("\n✅ FIXED CODE - Method 3: Return list of items")
 def collect_all(numbers):
     result = []
     for n in numbers:
         result.append(n)
     return result  # Return all items AFTER loop
 
 print(f"Result: {collect_all([1, 2, 3])}")  # Result: [1, 2, 3]
 
 
 # ✅ FIXED CODE - Method 4: Process and verify
 print("\n✅ FIXED CODE - Method 4: Process all items")
 def process_all(numbers):
     print("Processing: ", end="")
     for n in numbers:
         print(n, end=" ")
     print()  # New line
     return len(numbers)
 
 count = process_all([1, 2, 3])
 print(f"Total items processed: {count}")

#
 
# BUG: TypeError when adding int + str
# def add_values_buggy():
#     return 5 + "10"  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Explanation:
# Python does not implicitly convert between numbers and strings.
# You must explicitly convert types (e.g., int("10") or str(5)).

# FIXED: try numeric conversion, otherwise concatenate as strings
def add_values(a, b):
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        return str(a) + str(b)

# Tests
assert add_values(5, "10") == 15
assert add_values("5", "10") == 15
assert add_values(5, "x") == "5x"

print("All Task 11 tests passed.")
 
 
 
 
 
 
 
 











