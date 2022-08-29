import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class Solution {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        int l=scan.nextInt();
        for(int i=0; i<=l; i++){
            int arrive_ontime=0;
            int n=scan.nextInt();
            int k=scan.nextInt();
           for(int q=0; q<n; q++){
                int a=scan.nextInt();
                if(a<=0)
                arrive_ontime=1+arrive_ontime;
                }
           if (arrive_ontime>=k) {System.out.println("NO");}
           else {System.out.println("YES");}
           
        }

           
           
       }
       
    }


