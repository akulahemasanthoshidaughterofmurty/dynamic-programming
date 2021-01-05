class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count=0;
        for(int i=0;i<jewels.length();i++)
        { 
            for(int j=0;j<stones.length();j++)
            {
                if(jewels.charAt(i)==stones.charAt(j))
                    count++;
            }
        }
        return count;
        
    }
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        String jewels=s.next();
        String stones=s.next();
        Solution obj=new Solution();
        System.out.println(obj.numJewelsInStones(jewels,stones));
        
    }
}
