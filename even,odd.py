a=[1,2,3,4,5,6,7,8,10]
ac=[]
b=[]
for i in a:
    if i%2==0:
        ac.append(i)
    else:
        b.append(i)
print(ac)
print(b)
