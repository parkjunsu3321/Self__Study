import java.util.*;

class Main {
    public static long GCD(long x, long y) {
        if (x < y) {
            long temp = y;
            y = x;
            x = temp;
        }
        while (y != 0) {
            long temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for (int i = 0; i < n; i++) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            
            long gcd = GCD(a, b);
            long lcm = (a / gcd) * b;
            
            System.out.println(lcm);
        }
        sc.close();
    }
}