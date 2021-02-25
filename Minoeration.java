import java.util.*;    
class Minoeration 
{ 
	public static void main(String args[]) 
    { 
	Scanner s=new Scanner(System.in);
	int n=s.nextInt();
	int arr[]=new int[n];
	for(int i=0;i<n;i++)
	{
		arr[i]=s.nextInt();
	}
        int arraySum, smallest, arr_size = arr.length; 
        arraySum = 0; 
        smallest = arr[0]; 
        for (int i = 0; i < arr_size ; i ++) 
        { 
		 if (arr[i] < smallest)             
                smallest = arr[i];             
   		 arraySum += arr[i]; 
        } 
  
        int minOperation = arraySum - arr_size * smallest; 
	 System.out.println( 
                               minOperation); 
  
    } 
}
   