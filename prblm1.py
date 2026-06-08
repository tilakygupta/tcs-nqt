# Weekly Exercise Summary
# Design a fitness app feature: take exercise minutes for 7 days. Print total and average (rounded to nearest integer). This was Q1 of Oct 3 2024 morning shift.
# Example
# Input:  45 15 30 15 5 10 20
#
# Output: Total exercise duration : 140 (minutes)
# Average daily exercise duration: 20 minutes
import sys

raw_data = sys.stdin.read().split()

data = [float(x) for x in raw_data]
if data:
    avg = sum(data)/len(data)

    print(avg)

total = sum(data)
print(total)