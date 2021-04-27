
N=10000
l=[1]*N
def gen_sei():
    for i in range(2,int(N**0.5)+1):
        for j in range(2*i,N,i):
            l[j]+=i

gen_sei()
for _ in range(int(input())):
    n=int(input())
    if(l[n]==n):
        print("YES")
    else:
        print("NO")
