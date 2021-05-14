class Solution:
	def longestCommonSum(self, arr1, arr2, n): 
		# code here 
		arr3=[0]*n
		for i in range(n):
		    arr3[i]=arr1[i]-arr2[i]
		prefix=0
		dic={}
		maxi=0
		for i in range(n):
		    prefix+=arr3[i]
		    if(prefix==0):
		        maxi=i+1
		    if(prefix in dic.keys()):
		        maxi=max(maxi,i-dic[prefix])
		    else:
		        dic[prefix]=i
		return maxi
