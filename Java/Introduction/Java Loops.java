import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0; i<t; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            int prev = a + (int)Math.pow(2, 0) * b;
            System.out.print(prev + " ");
            for(int j=1; j<n; j++){
                int temp = prev + (int)Math.pow(2, j) * b;
                prev = temp;
                System.out.print(temp + " ");
            }
            System.out.println();
        }
    }
}    