import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(n>0){
            int N = sc.nextInt();
            int K = sc.nextInt();
            int [] a = new int [N];
            
            for(int i=0;i<N;i++){
                a[i] = sc.nextInt();
            }
            
            int noK = 0;
            int pSum = 0, nSum = 0;
            for(int i=0;i<N;i++){
                if(a[i] <= 0){
                    noK++;
                    nSum += Math.abs(a[i]);
                }
                else{
                    pSum += Math.abs(a[i]);
                }
            }
            //System.out.println(noK);
            if(noK >= K)                
                System.out.println("NO");
            else
                System.out.println("YES");
            
            
            n--;
        }
    }
}