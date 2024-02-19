a="abcdefghijklmnopqrstuvwxyz"
b="abcdefghijlmnopqrstuvwxyz"
for i in a:
    if i not in b:
        m=i
        break
print(m)
