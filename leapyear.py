data = int(input())

if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print("leap year")
else:
    print("not leap year")