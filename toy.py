n, q = map(int, input().split())

defect = (q/n) * 100

print(defect)

if defect <= 5:
    print("Pass")
else:
    print("Fail")