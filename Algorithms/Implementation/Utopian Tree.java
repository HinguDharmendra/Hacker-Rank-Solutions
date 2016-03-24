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
            int height = 1;

            for(int i=1;i<=N;i++){
                if(i%2==1)
                    height = height*2;
                else
                    height++;
            }
            System.out.println(height);
            n--;
        }
    }
}