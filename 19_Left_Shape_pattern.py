n = int(input("Please input hear (Number only): "))

def pattern(n):
      for i in range(n):
           for j in range(i + 1):
                print("* ", end="")
           print("\r")
      
      for i in range(n, -1 , -1):
          for j in range(i + 1):
               print("* ", end="")
          print("\r")
 
pattern(n)