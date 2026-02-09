# Buggy version (would raise NameError)
# def calculate_area():
#     return length * width
# print(calculate_area())

# Fixed: accept length and width as parameters
def calculate_area(length, width):
    return length * width

# Demo run
print(calculate_area(5, 4))  # 20

# Tests
assert calculate_area(2, 3) == 6
assert calculate_area(0, 5) == 0
assert calculate_area(3.5, 2) == 7.0

print("All assertions passed.")


# BUG (would raise TypeError):
# def add_values():
#     return 5 + "10"

# FIXED: convert to numbers when possible, otherwise concatenate as strings
def add_values(a, b):
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        return str(a) + str(b)

# Demonstration + tests
print(add_values(5, "10"))   # 15
assert add_values(5, "10") == 15
assert add_values("5", "10") == 15
assert add_values(5, "x") == "5x"
print("All Task 11 tests passed.")


# Bug: None + 10 -> TypeError
def compute(value=None, default=0):
    if value is None:
        value = default
    return value + 10

# Explanation:
# - NoneType cannot be added to numbers; provide a sensible default.

# Tests
assert compute(None) == 10
assert compute(5) == 15
assert compute(-10) == 0




# Combined fixes + tests for Tasks 12-15

# Task 12: Fix str + list
def combine(lst, use_join=False):
    # If use_join: join elements with spaces; otherwise use str(list)
    if use_join:
        return "Numbers: " + " ".join(map(str, lst))
    return "Numbers: " + str(lst)

# Task 13: Fix string * float
def repeat_text(times):
    # String repetition requires an int count; convert float->int
    return "Hello" * int(times)

# Task 14: Fix None + int
def compute(value=None, default=0):
    # If value is None, use default before adding
    if value is None:
        value = default
    return value + 10

# Task 15: Fix input treated as string
def sum_two_numbers_from_strings(a, b):
    # Convert inputs to int (works if ints or numeric-strings)
    return int(a) + int(b)

# --- Tests ---

# Task 12 tests
assert combine([1, 2, 3]) == "Numbers: [1, 2, 3]"
assert combine([4], use_join=True) == "Numbers: 4"
assert combine([], use_join=True) == "Numbers: "

# Task 13 tests
assert repeat_text(2.5) == "HelloHello"
assert repeat_text(3) == "HelloHelloHello"
assert repeat_text(0.9) == ""

# Task 14 tests
assert compute(None) == 10
assert compute(5) == 15
assert compute(-10) == 0

# Task 15 tests
assert sum_two_numbers_from_strings("2", "3") == 5
assert sum_two_numbers_from_strings("5", "10") == 15
assert sum_two_numbers_from_strings(4, "6") == 10

print("All tests passed.")