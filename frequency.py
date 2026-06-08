items = input().split()

for item in items:
    if any (ch.isdigit() for ch in item):
        print("Invalid Input")
        exit()

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

for item in freq:
    print(item, freq[item])