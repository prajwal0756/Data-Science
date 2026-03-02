f = open("26.poem.txt")
c = f.read()
if ("twinkle" in c):
    print("The twinkle is present in the file.")

else:
    print("The twinkle is not present in the file.")

f.close()


