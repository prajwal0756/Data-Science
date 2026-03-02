# Write a program to take a list of numbers and print only the even ones.

# l = [1,2,3,4,5,6,7,8,9,10]

# for i in l:
#     if (i%2==0):
#         print(i)
    


# Ask the user for a sentence and count how many vowels it contains.
# a = input("Enter the sentence: ")
# count = 0
# vowels = "aeiouAEIOU"   # handle uppercase too

# for i in a:
#     if i in vowels:
#         count += 1

# print("Number of vowels:", count)



# Given a list of names, print the names that start with a vowel.
        
l = ["prajwal", "Arbin", "anup", "ubin", "bipin","imran","owl"]
v= ("a","e","i","o","u")
for name in l:
      if(name.lower().startswith(v)):
            
            print(name)


# Take a number n and print its multiplication table up to 10.

# n= int(input("Enter the number: "))

# for i in range(1,11):
#       print(f"{n}*{i} = {n*i}")


# Reverse a given string without using slicing ([::-1] not allowed).

# a = input("Enter the string: ")
# reversed_str = ""

# for char in a:
#     reversed_str = char + reversed_str   # Add in front

# print("Reversed string:", reversed_str)





# using slicing 
a = input("Enter a string: ")
reversed_a = a[::-1]
print("Reversed string:", reversed_a)




        

