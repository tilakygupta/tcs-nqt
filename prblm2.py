# Palindrome Count in Range
# Given a range M to N (inclusive), find all palindrome numbers and return their count. This was Q2 of Oct 3 2024 morning shift (easy variant).
# Example
# Input:  10 20
#
# Output: 1

m, n = map(int, input().split())

count = 0

for i in range (m, n+1):
    s = str(i)

    if s == s[::-1]:
        count += 1
print(count)