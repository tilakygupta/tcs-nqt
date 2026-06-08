bill = float(input())

if bill <= 0:
    print("Invalid amount")
elif bill < 500:
    discount = 0
elif bill < 1000:
    discount = 0.10
else:
    discount = 0.20

if bill > 0:
    final = bill * (1 - discount)
    print(f"Final Amount: ₹{final}")