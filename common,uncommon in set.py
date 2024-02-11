a="abcdef"
b="aybcdegh"
c=set(a)
d=set(b)
e=c.intersection(d)
print("common:",e)
n=c.symmetric_difference(d)
print("uncommon:",n)
