import java.util.*;
import java.lang.*;
import java.io.*;
class Main 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] arr = new int[N][M];
        int i = 0; int j = 0;
        while(true)
        {
            if(j+1 > M)
            {            
                if(i+1 >= N)
                {
                    break;
                }
                else
                { 
                    j = 0;
                    i++;   
                }
            }
            arr[i][j] = sc.nextInt();
            j++;
        }
        int num = sc.nextInt();
        for(i = 0; i<num; i++)
        {
            int sum = 0;
            int a = sc.nextInt(); int b = sc.nextInt(); int x = sc.nextInt(); int y = sc.nextInt();
            for(int z = a-1; z<x; z++)
            {
                for(int u = b-1; u<y; u++)
                {
                    sum += arr[z][u];
                }
            }
            System.out.println(sum);
        }
    }
}