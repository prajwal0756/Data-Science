lists= ["Prajwal", "ok", 2, 3.5, "oh nice", False, True]

print(lists[1])

lists[1]=3 #element at particular index

print(lists[1])   #lists can be changed unlike string
print(lists)

print(lists[1:5])  #elements from 1 to 4 index

l1= [2,5,8,1,0,4,3]
l1.sort()   #sort the element in asccesnding order and it change the list itself 
print(l1)
l1.append(10)     #add the element at the end of the list
print(l1)
l1.reverse()     #it reverses the list 
print(l1)

l1.insert(3,9)    #it adds the element of index 3 to 9 first index and then element in syntax
print(l1)


l1.pop(3)    #it remove the element of particular index
print(l1)

l1.remove(0)     #it removes the element which is given 
print(l1)