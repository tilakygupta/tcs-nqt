n = int(input())

prices = list(map(int, input().split()))

promo = input().strip()

subtotal = sum(prices)

print(f"Subtotal: ₹{subtotal}")

if promo == "SAVE10":
    after_promo = subtotal * 0.90
else:
    after_promo = subtotal

print(f"After promo: ₹{after_promo}")

gst = after_promo * 0.18

print(f"GST (18%): ₹{gst}")

total = after_promo + gst

print(f"Total: ₹{total}")