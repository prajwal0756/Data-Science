# def avg():      #function defination
#     a = int(input("Enter the number: "))
#     b = int(input("Enter the number: "))
#     c = int(input("Enter the number: "))

#     print((a+b+c)/3)

# avg()  #function call
# avg()
# avg()


#  Function with arguement 

# def goodday(name):
#     print("Have a Good day, " +name )

# goodday("Prajwal")
# goodday("Kshtiz")
# goodday("Rohan")
# goodday("Kandel")
# goodday("Bhurtel")
# goodday("Manisha")
# goodday("PAwan")

# return valued function


# def okay(name):
#     print("Hello, " +name )
#     return "Finish"   # this takes value from function to give value to  any variable 

# a = okay("Prajwal")
# print(a)



def goodday(name, ending ="Thank you"):  #its a default value give to the function
    print("Have a Good day, " +name )
    print(ending)

goodday("Prajwal", "Thanks")  # if we put something in ending then it will take it else it take deafult value 
goodday("Kshtiz")