
# Task 1
'''
Prompt :
You are an AI coding assistant. 
Write a Python function in Google Colab that:
Accepts a list of numbers as input
Calculates the mean, minimum, and maximum values
Prints the results clearly

Then run the function on the list [12, 7, 9, 21, 5] and show the output.
'''


def calculate_statistics(numbers):
    """
    Calculate and print mean, minimum, and maximum values for a list of numbers.

    Args:
        numbers (list): A list of numeric values
    """
    if not numbers:
        print("Error: The list is empty")
        return

    # Calculate statistics
    mean_value = sum(numbers) / len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)

    # Print results clearly
    print("Statistics for the given numbers:")
    print(f"Mean: {mean_value:.2f}")
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")

# Test the function with the given list
test_list = [12, 7, 9, 21, 5]
calculate_statistics(test_list)




# Task 2
'''
Prompt: Armstrong Number Checker
Write a Python function that checks if a number is an Armstrong number.
Test it with 153 and 123, and print the results clearly.
'''

def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    # Convert number to string to get individual digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum equals the original number
    return armstrong_sum == number

# Test the function with given numbers
test_numbers = [153, 123]

for num in test_numbers:
    result = is_armstrong_number(num)
    status = "is" if result else "is not"
    print(f"{num} {status} an Armstrong number")



# Task 3
'''
Prompt 1 :
Write a Python function is_leap_year(year) that returns True if the year is a leap year, otherwise False.
Test it with 2000, 2021, 2024, and 2100, and print the results.
'''

def is_leap_year(year):
    """
    Check if a year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, AND
    - It is NOT divisible by 100, OR it IS divisible by 400

    Args:
        year (int): The year to check

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    # A year is a leap year if it is divisible by 4
    # but not by 100 unless it is also divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

# Test the function with given years
test_years = [2000, 2021, 2024, 2100]

for year in test_years:
    result = is_leap_year(year)
    status = "is" if result else "is not"
    print(f"{year} {status} a leap year")


'''
Prompt 2 :
Create a Python program check_leap_year(year) with a docstring and comments explaining the leap year rules.
Print descriptive messages for 1900, 2000, 2024, and 2100 showing why each year is or isn’t a leap year.
'''

def check_leap_year(year):
    """
    Check if a year is a leap year and print detailed explanation.
    Leap year rules (Gregorian calendar):
    - A year is a leap year if it is divisible by 4
    - However, if the year is divisible by 100, it must also be divisible by 400 to be a leap year
    - This rule prevents century years (like 1900) from being leap years unless they are divisible by 400
    Args:
        year (int): The year to check (must be a positive integer)

    Returns:
        None: Prints detailed explanation of leap year status
    """
    print(f"\nChecking year: {year}")
    # Step 1: Check if divisible by 4
    if year % 4 != 0:
        print(f"  {year} is not divisible by 4.")
        print(f"  Therefore, {year} is NOT a leap year.")
        return

    print(f"  {year} is divisible by 4.")

    # Step 2: If divisible by 4, check if it's a century year (divisible by 100)
    if year % 100 == 0:
        print(f"  {year} is a century year (divisible by 100).")

        # Step 3: For century years, must be divisible by 400
        if year % 400 == 0:
            print(f"  {year} is also divisible by 400.")
            print(f"  Therefore, {year} IS a leap year.")
        else:
            print(f"  {year} is not divisible by 400.")
            print(f"  Therefore, {year} is NOT a leap year.")
    else:
        print(f"  {year} is not a century year.")
        print(f"  Therefore, {year} IS a leap year.")

# Test the function with given years
test_years = [1900, 2000, 2024, 2100]

print("Leap Year Analysis:")
print("=" * 50)

for year in test_years:
    check_leap_year(year)



# Task 5: Sum of Even and Odd Numbers
'''
Write a Python program that calculates the sum of odd numbers and sum of even numbers in a given tuple using basic logic.

Then, refactor the same code using an AI tool to make it cleaner and more efficient.
'''

# Original code (student logic)
def calculate_sums_original(numbers):
    """
    Original implementation using basic loop logic
    """
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Refactored code (AI version) - More efficient and cleaner
def calculate_sums_refactored(numbers):
    """
    Refactored implementation using list comprehensions and built-in sum function
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

# Test both versions
test_tuple = (1, 2, 3, 4, 5, 6)




print("=== ORIGINAL CODE (Student Logic) ===")
even_sum_orig, odd_sum_orig = calculate_sums_original(test_tuple)
print(f"Sum of even numbers: {even_sum_orig}")
print(f"Sum of odd numbers: {odd_sum_orig}")

print("\n=== REFACTORED CODE (AI Version) ===")
even_sum_refactored, odd_sum_refactored = calculate_sums_refactored(test_tuple)
print(f"Sum of even numbers: {even_sum_refactored}")
print(f"Sum of odd numbers: {odd_sum_refactored}")
