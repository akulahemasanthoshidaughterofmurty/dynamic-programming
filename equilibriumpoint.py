class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
  
        if(len(A)==1):
            return 1
        prefix=[0]*N
        prefix[0]=A[0]
        for i in range(1,N):
                prefix[i]=prefix[i-1]+A[i]
        for j in range(1,N-1):
                left=prefix[j-1]
                right=prefix[N-1]-prefix[j]
                if(left==right):
                    return j+1
                    
        return -1
