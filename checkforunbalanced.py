arr=[2,3,4,7,8,6,11,13,22]
n=len(arr)
rmin=[0]*n
rmin[-1]=arr[-1]
lmax=[0]*n
lmax[0]=arr[0]
print(arr)
for i in range(n-2,-1,-1):
    rmin[i]=min(arr[i],rmin[i+1])
print(rmin)
for j in range(1,n):
    lmax[j]=max(arr[j],lmax[j-1])
print(lmax)
left=-1
right=0
while(lmax[left]==arr[left] or lmax[right]==rmin[right]):
    left+=-1
    right+=1
print(right,(left*-1)+1)
