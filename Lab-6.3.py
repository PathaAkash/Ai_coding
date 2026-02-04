# Task 1
#Python Student class with name, roll number, branch in init. Add display_details to print all info

class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")

# Example usage
student1 = Student("Alice", "101", "Computer Science") 
student1.display_details()

# Task 2
# writing a utility function to display multiples of a given number.

def display_multiples(number, count):
    for i in range(1, count + 1):
        print(f"{number} * {i} = {number * i}")

# Example usage
print("\nMultiples of 5:")
display_multiples(5, 10)  # Display first 10 multiples of 5



# Task 3
# building a basic classification system based on age.
def classify_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"
# Example usage
ages = [10, 15, 25, 65, -5]
print("\nAge Classification:")
for age in ages:
    category = classify_age(age)
    print(f"Age: {age}, Category: {category}")


# Task 4
#calculate the sum of the first n natural numbers.

def sum_of_natural_numbers(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

# Example usage
n = 10
total_sum = sum_of_natural_numbers(n)
print(f"\nSum of the first {n} natural numbers is: {total_sum}")


# Task 5
# designing a basic banking application. -> class with methods such as deposit(), withdraw(), and check_balance().
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

# Example usage
account = BankAccount("John Doe", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.withdraw(2000)