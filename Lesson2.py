# Collect user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message: ")

# Create username: first initial + last name, lowercase
username = f"{first_name[0].lower()}{last_name.lower()}"

# Full name in Title Case
full_name = f"{first_name} {last_name}".title()

# Clean bio: strip whitespace, then replace 'I am' with 'I'm'
clean_bio = bio.strip().replace("I am", "I'm")

# Character count of the cleaned bio
bio_length = len(clean_bio)

# Display formatted output
print(f"\n--- User Profile ---")
print(f"Full Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {clean_bio}")
print(f"Bio Length: {bio_length} characters")