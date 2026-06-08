num = int(input())

count = 0
sums = 0
product = 1

temp = num

while temp > 0:
    digit = temp % 10
    count += 1

    sums += digit
    product *= digit

    temp //= 10

print(count)
print(sums)
print(product)