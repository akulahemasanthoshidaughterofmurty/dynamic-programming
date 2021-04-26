n=int(input())
primes=[1]*n
def create_sieve():
    primes[0]=primes[1]=0
    for i in range(2,n):
        if(primes[i]==1):
            for j in range(i*i,n,i):
                primes[j]=0


create_sieve()
consecutive_sum=2
count=0
for i in range(3,n):
        if(primes[i]==1):
            consecutive_sum+=i
            if(consecutive_sum<n):
                if(primes[consecutive_sum]==1):
                    count+=1
                    print(consecutive_sum)
            

            else:
                break
print(count)

