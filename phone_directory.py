contacts = {
    "Thabo": "0821112222",
    "Amara": "0731234567",
    "Sipho": "0609876543",
}

name = input("Enter the name of the friend you're looking for: ").strip()

if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")
