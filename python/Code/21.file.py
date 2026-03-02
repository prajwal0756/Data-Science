
# # syntax of file opening and closing also reading 
# f = open("22.file.txt", "r")   # the read function is default if we want to write we should write "w"
# data = f.read()
# print(data)   #this program reads the data in the 22.file.txt and display here 
# f.close()

#using with statement 

with open("22.file.txt", "r") as f:   #by sing this we dont need to put fclose() in the code.
    print(f.read())






# str = "Hey, Now i am going to write something in the file using python programming. "
# f = open("23.file.txt", "w")   # the read function is default if we want to write we should write "w"
# data = f.write(str)
# print(data)   #this program create 23.file.txt and write  the data in the 23.file.txt and display there 
# f.close()


# f = open("22.file.txt")
# lines = f.readlines()  #this function creates list of data from the given file 
# print(lines, type(lines))
# f.close()