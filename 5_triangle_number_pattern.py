n = int(input("Please input hear (Number only): "))

for i in range(n):
    for j in range(i+1):
        print(n-i, end= " ")
    print()