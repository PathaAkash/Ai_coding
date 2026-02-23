def find_max(numbers):
    """Finds the maximum value in a list.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        int/float: The largest number in the list.

    Example:
        >>> find_max([1, 2, 3, 4])
        4
    """
    # Use built-in max() to find the largest number
    return max(numbers)  # returns the maximum value

# Test the function
print(find_max([1, 2, 3, 4]))  # Output: 


def login(user, password, credentials):
    """
    Checks if the provided username and password match the stored credentials.

    Args:
        user (str): The username entered by the user.
        password (str): The password entered by the user.
        credentials (dict): A dictionary storing valid username-password pairs.

    Returns:
        bool: True if login is successful, False otherwise.

    Example:
        >>> credentials = {"admin": "1234"}
        >>> login("admin", "1234", credentials)
        True
    """
    # Check if the password stored for the user matches the entered password
    return credentials.get(user) == password  # returns True or False

# Test the function
credentials = {"admin": "1234", "user1": "abcd"}
print(login("admin", "1234", credentials))   # Output: True
print(login("user1", "wrong", credentials))  # Output: False




"""
calculator module - performs basic arithmetic operations.
"""

def add(a, b):
    """
    Returns the sum of two numbers.

    Args:
        a (int/float): First number.
        b (int/float): Second number.

    Returns:
        int/float: Sum of a and b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b  # adds two numbers

def subtract(a, b):
    """
    Returns the difference of two numbers.

    Args:
        a (int/float): First number.
        b (int/float): Second number.

    Returns:
        int/float: Difference of a and b.

    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b  # subtracts b from a

def multiply(a, b):
    """
    Returns the product of two numbers.

    Args:
        a (int/float): First number.
        b (int/float): Second number.

    Returns:
        int/float: Product of a and b.

    Example:
        >>> multiply(2, 3)
        6
    """
    return a * b  # multiplies two numbers

def divide(a, b):
    """
    Returns the quotient of two numbers.

    Args:
        a (int/float): First number.
        b (int/float): Second number.

    Returns:
        float: Quotient of a and b.

    Raises:
        ValueError: If b is zero.

    Example:
        >>> divide(6, 2)
        3.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")  # handles division by zero
    return a / b  # divides a by b

# Test all functions
print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
print(multiply(2, 3))   # Output: 6
print(divide(6, 2))     # Output: 3.0

"""
conversion module - performs number system conversions.
"""

def decimal_to_binary(n):
    """
    Converts a decimal number to binary.

    Args:
        n (int): A decimal number.

    Returns:
        str: Binary representation of the number.

    Example:
        >>> decimal_to_binary(10)
        '1010'
    """
    return bin(n).replace("0b", "")  # removes '0b' prefix from binary

def binary_to_decimal(b):
    """
    Converts a binary number to decimal.

    Args:
        b (str): A binary number as string.

    Returns:
        int: Decimal representation of the binary number.

    Example:
        >>> binary_to_decimal('1010')
        10
    """
    return int(b, 2)  # converts binary string to decimal integer

def decimal_to_hexadecimal(n):
    """
    Converts a decimal number to hexadecimal.

    Args:
        n (int): A decimal number.

    Returns:
        str: Hexadecimal representation of the number.

    Example:
        >>> decimal_to_hexadecimal(255)
        'ff'
    """
    return hex(n).replace("0x", "")  # removes '0x' prefix from hexadecimal

# Test all functions
print(decimal_to_binary(10))        # Output: 1010
print(binary_to_decimal('1010'))    # Output: 10
print(decimal_to_hexadecimal(255))  # Output: ff












"""
course module - manages course records in a system.
"""

# Dictionary to store courses
courses = {}

def add_course(course_id, name, credits):
    """
    Adds a new course to the system.

    Args:
        course_id (int): Unique identifier for the course.
        name (str): Name of the course.
        credits (int): Number of credits for the course.

    Returns:
        str: Success message after adding the course.

    Example:
        >>> add_course(101, "Python", 3)
        'Course added successfully'
    """
    courses[course_id] = {"name": name, "credits": credits}  # stores course details
    return "Course added successfully"

def remove_course(course_id):
    """
    Removes a course from the system.

    Args:
        course_id (int): Unique identifier of the course to remove.

    Returns:
        str: Success or error message.

    Example:
        >>> remove_course(101)
        'Course removed successfully'
    """
    if course_id in courses:
        del courses[course_id]  # deletes the course from dictionary
        return "Course removed successfully"
    return "Course not found"  # returns error if course doesn't exist

def get_course(course_id):
    """
    Retrieves details of a course.

    Args:
        course_id (int): Unique identifier of the course.

    Returns:
        dict: Course details or error message.

    Example:
        >>> get_course(101)
        {'name': 'Python', 'credits': 3}
    """
    return courses.get(course_id, "Course not found")  # returns course or error message

# Test all functions
print(add_course(101, "Python", 3))       # Output: Course added successfully
print(add_course(102, "Java", 4))         # Output: Course added successfully
print(get_course(101))                    # Output: {'name': 'Python', 'credits': 3}
print(remove_course(101))                 # Output: Course removed successfully
print(get_course(101))                    # Output: Course not found