# Train Travel Time
# A train covers 800 metres (400m track + 400m bridge). Given speed in km/hr, calculate time taken in seconds. Print as integer.
# Example
# Input:  72
#
# Output: 40

speed = int(input())

distance = 800

speed = speed * 5/18

time = int(distance / speed)

print(time)