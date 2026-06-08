n = int(input())

temp = n
digits = len(str(n))
s = 0

while temp:
    rem = temp % 10
    s += rem ** digits
    temp //= 10

if s == n:
    print(f"The string {n} is a Armstrong")
else:
    print(f"The string {n} is not a Armstrong")
