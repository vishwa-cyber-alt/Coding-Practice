a=input("enter")
o=''
for i in a:
    if i.isalpha():
        x=i
    else:
        d=int(i)
        o=o+x*d
print(o)
