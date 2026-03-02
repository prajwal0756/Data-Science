# a = int(input("Enter your number a: "))
# b = int(input("Enter your number b: "))
# c = int(input("Enter your number c: "))
# d = int(input("Enter your number d: "))

# if(a>b and  a>c and a>d):
#     print("a is greater.", a)

# elif(b>a and b>c and b>d):
#     print("b is greater.", b)

# elif(c>a and c>b and c>d):
#     print("c is greater.", c)

# else:
#     print("d is greater.", d)



   #spam detection program 

p1 = "Make a lot of money"
p2 = "Join my telegram"
p3 = "You get macbook pro"
p4 = "You can get valuable gifts"

message = input("Enter your comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is spam ")

else:
    print("Not a spam")

