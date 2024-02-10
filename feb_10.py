#Remove all characters from string except alphabets
a="s3oft4ware31erlang33r"
alp=[]
str=[]
converttostring=[]
for i in a:
    if i.isdigit():
        alp.append(i)
    else:
        str.append(i)
converttostring=''.join(alp)
print(converttostring)
