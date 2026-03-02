                           # while loop 


# i=1
# while (i<5):
#     print(i)
#     i +=1

# l = [1,2,"Rohan", "hero", "okxatw", "khatam"]

# i=0
# while (i<len(l)):
#     print(l[i])
#     i  +=1


                            #For loop 


# n = int(input("Enter the n number: "))

# for i in range(n):
#     print(i)
    

l = ["ok", 45, 34, 56, "play", "python"]

for item in l :
    print(item)

else:
    print("done")  # this is printed when loop finish or exit 




                  #using Break and continue in for loop

for i in range(100):
    if(i ==45):
        break   # stops the iteration from there 
    print(i)



for i in range(100):
    if(i ==45):
        continue  #skip the particular iteration
    print(i)