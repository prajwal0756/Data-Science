n =int(input("Enter the number: "))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end = "")   
    print("")
    

# n =int(input("Enter the number: "))

# for i in range(1, n+1):
#     print( " "* (i-1) , end="")
#     print("*"* (2*(n-i)+1), end = "")   # the end=""  prevents the creation of new line in print()
#     print("")
       