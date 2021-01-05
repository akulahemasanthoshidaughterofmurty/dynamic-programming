class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
    
        int n=nums.length;
        int fr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            int count=0;
            for(int j=0;j<n;j++)
            {
                if(nums[i]>nums[j])
                    count++;
            }
            fr[i]=count;
        }
        return fr;
    }
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int nums[]=new int[n];
        Solution obj=new Solution();
        int re[]=new int[n];
        re=obj.smallerNumbersThanCurrent(nums);
        for(int i=0;i<n;i++)
        {
            System.out.print("["+re[i]+"]");
        }
        
    }
}
