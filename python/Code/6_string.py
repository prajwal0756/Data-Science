                            #Intro to strings 

name = "John"
age = 30

nameslice = name[1:3]  # Slicing the string to get characters from index 1 to 2
# ageslice = str(age)[1:3]  # Slicing the string representation of age
print(nameslice)
character= name[1]
print(character)

#[1:3] means 1 is included but 3 is not included 



                                  #negative slicing 

ok= "okaxatw"
print(ok[-4:-1])


# skipping

now = "Prajwalsubedi"
print(now[1:7:4])



                                         # sting functions 

print(len(name))
print(len(character))
print(len(now))
print(len(ok))

print(name.endswith("n"))
print(ok.startswith("twn"))

         #escape sequence (\n, \t \"")

a= "I am the good boy\n a good \"learner\" \tcan be it and also 'ok' can be printed "
print(a)

name = input("Enter your name: ")
# print(f"Good morning {name} hero ")
Date= input("Enter the date: ")

print(f"Dear {name},\n you are selected! \n {Date}")


