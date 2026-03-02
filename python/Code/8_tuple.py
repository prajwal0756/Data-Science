
#It is also emmutable it cannot be change like string 

a = (1,2,3,4,"ok","don",)      # many elements tuple
print(a)
print(type(a))

b= (1,)
print(type(b))     #single element tuple we need to use comma

c= ()
print(type(c))      #Empty tuple

num = a.count(2)
print(num)
 
i = a.index(3)
print(i)

concatinate = a+b
print(concatinate)

