n = int(input("Please input hear (Number only): "))

for i in range(n-1, -1, -1):
    for j in range(n-i):
        print(" ", end="")

    for k in range(i+1):
        print(k+1, end=" ")

    print()
