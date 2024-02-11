nums = [0,1,0,3,12,0,56,7,9,1,0,4,3]
z=[]
n=[]
r=[]
for i in nums:
    if i==0:
        z.append(i)
    else:
        n.append(i)
r=n+z
print(r)
