a = "welcome to earth"
v = []

for i in range(len(a)):
    if a[i] in "aeiou":
        v.append(i)

print(v)
