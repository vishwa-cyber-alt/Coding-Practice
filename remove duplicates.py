from collections import Counter
a=[1,2,3,4,5,5,4,3]
remove=[]
ok=[]
c=Counter(a)
print(c)
for i in c:
    if c[i]>1:
        remove.append(i)
    else:
        ok.append(i)
#print(remove)
print(ok)
