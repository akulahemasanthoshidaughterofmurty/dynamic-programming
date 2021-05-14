class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if(nums[i]==0):
                nums[i]=-1
        prefix=0
       
        dic={}
        maxi=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if(prefix==0):
                maxi=i+1
            if(prefix in dic.keys()):
                maxi=max(maxi,i-dic[prefix])
            else:
                dic[prefix]=i
        return maxi
        
