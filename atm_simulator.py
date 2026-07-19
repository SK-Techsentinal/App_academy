# Fixed bank balance
balance = 500

# Ask user how much they want to withdraw
amount = float(input("Enter amount to withdraw: R"))

# Check the request against the balance
if amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif amount <= balance:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds")