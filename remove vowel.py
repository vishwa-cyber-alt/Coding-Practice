a = "welcome to earth"
n = []
v=[]
for i in range(len(a)):
    if a[i] in "aeiou":
        v.append(a[i])
    else:
        n.append(a[i])
print(n)
f=''.join(n)
print(f)
#remove vowel,print only vowel,freq of each char vowel
