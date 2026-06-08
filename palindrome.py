n = input("Enter a string: ")

reverse = n[::-1]

if n == reverse:
    print(f"The string {n} is Palindrome")
else:
    print("Not Palindrome")