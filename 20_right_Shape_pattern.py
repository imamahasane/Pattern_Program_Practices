n = int(input("Please input hear (Number only): "))

def pattern(n):
    k = 2 * n - 2
    for i in range(n-1):
        for j in range(k):
            print(end=" ")
        k -= 2
        for j in range(i + 1):
            print("* ", end="")
        print("\r")

    k = -1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k += 2
        for j in range(i + 1):
            print("* ", end="")
        print("\r")
 
 
pattern(n)
