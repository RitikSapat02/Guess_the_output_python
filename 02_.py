l1 = [10,20,30]
l2 = l1[:]                   #copy list
print(id(l1),id(l2))

t1 = (10,20,30)
t2 = tuple(t1)
print(id(t1),id(t2))

s1 = "geeks"
s2 = s1[:]
print(id(s1),id(s2))

print(l1 is l2)
print(t1 is t2)
print(s1 is s2)
