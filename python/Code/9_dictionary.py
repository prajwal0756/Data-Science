d= {}   #empty dict

marks = {
    "prajwal" : 24,
    "ram": 24,
    "Hari":30,
    "manisha": 78

}

print(marks)
print(marks.items())     #show whole data in tuple form
print(marks.keys())     #show the name of student or show left hand keys
print(marks.values())    #show the marks of student or show left hand values
marks.update({"prajwal":90 , "shyam": 50})   #update or change the value in the dict and also add if not present in dict
print(marks)

print(marks.get("prajwal"))
print(marks["prajwal"])




mark = input("Enter the person you want to get marks: ")
print(marks[mark])