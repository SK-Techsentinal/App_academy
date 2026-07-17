# Ask the user for their secret password
password = input("Enter your secret password: ")

# Clean up any accidental leading/trailing spaces
clean_password = password.strip()

# Grab the first and last letter using string indexing
first_letter = clean_password[0]
last_letter = clean_password[-1]

# Print the hint, forcing letters to uppercase
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")