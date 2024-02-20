a= [10, 3, 5, 60, 20]
a.sort()
print(a)
b=a[::-1]
c=b[:3]
t=1
print(c)
for i in c:
    t*=i
print("max product=",t)
