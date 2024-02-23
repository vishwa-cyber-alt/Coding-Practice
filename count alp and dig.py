a="What do you think about 20241403"
alp=0
nu=0
for i in a:
  if i.isalpha():
    alp+=1
  elif i.isdigit():
    nu+=1
print(alp)
print(nu)
