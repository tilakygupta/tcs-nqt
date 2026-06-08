n = int(input())

max_title = ""
max_price = -1

for _ in range(n):
    title, price = input().split()
    price = int(price)

    if price > max_price:
        max_title = title
        max_price = price

print(f"Most expensive: {max_title} at ₹{max_price}")