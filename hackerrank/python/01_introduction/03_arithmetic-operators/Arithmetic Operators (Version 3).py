# Python - Arithmetic Operators (Version 3)
# Skills: Python (Basic)
# Difficulty: Easy

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 10**10:
                return value
            print("Please enter a valid integer between 1 and 10^10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

a = get_valid_input("Enter the first integer (between 1 and 10^10): ")
b = get_valid_input("Enter the second integer (between 1 and 10^10): ")

print(a + b)
print(a - b)
print(a * b)