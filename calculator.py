def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


# Collect two numbers safely using type casting
num1 = get_float("Enter the first number: ")
num2 = get_float("Enter the second number: ")

# Basic arithmetic
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Handle division by zero
if num2 == 0:
    division = "Error: Cannot divide by zero"
    floor_division = "Error: Cannot divide by zero"
    modulus = "Error: Cannot divide by zero"
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

# Display formatted results table
print(f"\n{'--- Calculator Results ---':^40}")
print(f"{'Addition:':<20}{addition}")
print(f"{'Subtraction:':<20}{subtraction}")
print(f"{'Multiplication:':<20}{multiplication}")
print(f"{'Division:':<20}{division}")
print(f"{'Floor Division:':<20}{floor_division}")
print(f"{'Modulus:':<20}{modulus}")