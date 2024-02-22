a = 14032002
s = 0

while(a > 0):
    n = a % 10 
    s += n     
    a //= 10   

print(s)

