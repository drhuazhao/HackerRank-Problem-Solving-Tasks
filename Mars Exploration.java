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

class Result {

    /*
     * Complete the 'marsExploration' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */

    public static int marsExploration(String s) {
    // Write your code here
    
    int begin = 0;
    int end = 3;
    String sos = "SOS";
    int Count_letter =0;
    
    
     
    while(end <=s.length()){
        
       String checking_letter = (s.substring(begin,end));
       if (checking_letter =="SOS"){
           ;  
       }
       
       else {
           for(int i =0; i<3; i++){
              
               if (checking_letter.charAt(i) != sos.charAt(i)){
                   Count_letter = Count_letter+1;
                   
                   
               }
               else{
                   ;
               }
           }
       }
       
       begin +=3;
       end +=3;
        
    }
    
    return(Count_letter);
    

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int result = Result.marsExploration(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

