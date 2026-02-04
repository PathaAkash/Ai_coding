# Task 1: Fibonacci Sequence (No Functions)
try:
    n = int(input("Enter the number of terms: "))

    # First two terms
    a, b = 0, 1
    count = 0

    # Check validity
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a, end=" ")
            nth = a + b
            # Update values
            a = b
            b = nth
            count += 1
    print() # Newline for clean output
except ValueError:
    print("Invalid input! Please enter a number.")
    
# Task 2: Optimized Fibonacci Sequence
try:
    n = int(input("Enter the number of terms: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 0, 1
        print(f"Fibonacci sequence ({n} terms):", end=" ")

        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b  # Optimized tuple swap
        print() # Newline

except ValueError:
    print("Invalid input. Please enter an integer.")
    
    
# Task 3: Modular Fibonacci (Using Functions)
def generate_fibonacci(n):
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)

    return sequence

# Main Execution
try:
    num = int(input("Enter number of terms for modular code: "))
    result = generate_fibonacci(num)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input.")
    
# Task 5: Iterative vs Recursive

# 1. Iterative Approach
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 2. Recursive Approach
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Testing both
n_terms = 5
print("Iterative Output:")
fib_iterative(n_terms)

print("Recursive Output:")
for i in range(n_terms):
    print(fib_recursive(i), end=" ")