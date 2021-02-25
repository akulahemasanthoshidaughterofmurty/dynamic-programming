import java.util.*;
public class Unique
{
	public static void main(String args[])
	{
		Scanner s=new Scanner(System.in);
		String str=s.next();
		int count=0;
		int ans=0;
		int len=str.length();
		String str1=str.toLowerCase();
		int arr[]=new int[len];
		for(int i=0;i<len;i++)
		{
			count=0;
			for(int j=0;j<len;j++)
			{
		
			if(str1.charAt(i)==str1.charAt(j))
			{
 				count++;
			}
			}
			arr[i]=count;
			
			
		}
		for(int k=0;k<len;k++)
		{
			if(arr[k]==1)
			{
				ans=k;
				break;
			}
		}
		if(ans!=0)
		System.out.println(ans+1);
		else
                  System.out.println("-1");
		
	}
}