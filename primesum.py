n=100
primes=[1]*n
def create_sieve():
    primes[0]=primes[1]=0
    for i in range(2,n):
        if(primes[i]==1):
            for j in range(i*i,n,i):
                primes[j]=0


create_sieve()
num=int(input())
def checking(a,b,c,d):
    if((a<c or a==c) and b<d):
         a,b=a,b
    else:
         a,b=c,d
    return (a,b)
a=num
b=num
for i in range(0,num):
    for j in range(i,num):
        if(primes[j]==1 and primes[i]==1):
            if(i+i==num):
                c=i
                d=i
                if(checking(a,b,c,d)):
                    a,b=c,d
                '''if((a<c or a==c) and b<d):
                    a,b=a,b
                else:
                    a,b=c,d'''
                
            elif(i+j==num):
                c=i
                d=j
                if(checking(a,b,c,d)):
                    a,b=c,d
                '''if((a<c or a==c) and b<d):
                    a,b=a,b
                else:
                    a,b=c,d'''
print(a,b)

                    
                
    
