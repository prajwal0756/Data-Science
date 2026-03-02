e = set()  #emppty set

s = {1,5,6 ,7 ,8 ,3,5,6,7,"ok"}    #in set no value can be repetitive all are unique values
print(s)


o = {56, "ok", 45, "ram","ram", 2, 7, 6}
print(o)

o.add(64)
print(o)

print(len(s))
o.remove( 45)
print(o)
s.remove(1)
print(s)

# union and intersection

print(s.union(o))
print(s.intersection(o))