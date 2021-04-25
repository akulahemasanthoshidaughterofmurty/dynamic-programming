def gcd1(a,b):
    if(a==0):
         return b
    elif(b==0):
         return a
    elif(a<b):
        a,b=b,a
        return gcd1(a%b,b)
    else:
        return gcd1(a%b,b)
    
n=int(input())
for i in range(n):
    a=int(input())
    b=int(input())
    res=gcd1(a,b)
    if(res==1):
        print("yes")
    else:
        print("no")


