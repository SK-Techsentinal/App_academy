first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

full_name = f"{first_name} {surname}"

print(f"Welcome, {full_name}!")
print(f"Name in UPPERCASE: {full_name.upper()}")
print(f"Name in Title Case: {full_name.title()}")

age_in_months = age * 12
print(f"Age in months: {age_in_months}")

rounded_favourite = round(favourite_number, 2)
print(f"Favourite number (rounded): {rounded_favourite}")

print(f"Type of first_name: {type(first_name)}")
print(f"Type of surname: {type(surname)}")
print(f"Type of age: {type(age)}")
print(f"Type of favourite_number: {type(favourite_number)}")