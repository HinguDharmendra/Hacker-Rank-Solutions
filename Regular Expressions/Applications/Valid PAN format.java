import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
   
  
    // Template Credit goes to www.hackerrank.com/kogupta 
    private static boolean isValidPAN(String s) {

        String pattern = "^[A-Z]{5}[0-9]{4}[A-Z]{1}";
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(s);
        if(m.find()){
            return true;
        }
        else{
            return false;
    }
    }
  
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int i = Integer.parseInt(br.readLine());
            for (int j = 0; j < i; j++) {
                String s = br.readLine();
                System.out.println(isValidPAN(s) ? "YES" : "NO");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } 
    }
}
