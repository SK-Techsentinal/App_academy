# Ask user for trip details
kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# Calculate liters needed (1 liter per 10 km)
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Display results, rounded to 2 decimal places
print(f"\n--- Fuel Cost Estimate ---")
print(f"Distance: {kilometers} km")
print(f"Liters needed: {round(liters_needed, 2)} L")
print(f"Total cost: R{round(total_cost, 2)}")
