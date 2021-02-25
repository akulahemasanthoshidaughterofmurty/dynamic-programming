import java.util.Stack;
import java.util.*;
public class Static1
{
	public static void main(String args[])
	{
		int arr[]=new int[5];
		int arr1[]=new int[5];
		Scanner s=new Scanner(System.in);
		
		int top=-1;
		int y=0;
		int n;
		
		
		do
		{
			 n=s.nextInt();
			switch(n)
			{
			case 1:  if (top >= (5 - 1)) {
            			System.out.println("Overflow");
           			 break;
       				 }
       	 	
       				 else {
					int x=s.nextInt();
          			  arr[++top] = x;
       			     
    			        break;
     				   }
			case 2:if (top < 0) {
            			System.out.println("Underflow");
            			break;
        			}
        			else {
					int x=arr[top];
					arr1[y]=x;
					arr[top]=0;
					y=y+1;
          			   
           			 break;
        			}
			}
		}while(n!=3);
		for(int i=5-1;i>=0;i--)
		{	if(arr[i]==0)
			
				continue;
			
			
			else
				System.out.println(arr[i]);
		}
		
	}
}










		