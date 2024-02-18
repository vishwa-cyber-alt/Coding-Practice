a="1abc23"
b=[]
c=[]
for i in a:
    if i.isalpha():
        b.append(i)
    else:
        c.append(int(i))
print(b)
print(c)
print(sum(c))
