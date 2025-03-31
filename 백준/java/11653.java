import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int index = 0;
        while(true)    
        {
            if(number == 1)
            {
                break;
            }
            for(int i = 2; i<=number; i++)
            {
                if(number % i == 0)
                {
                    System.out.println(i);
                    number = number/i;
                    break;
                }
            }
        }
        sc.close();
    }
}