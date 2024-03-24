import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	 Scanner sc = new Scanner(System.in);
    	 
    	 while(true) {
        	 String n = sc.next();
        	 int len = n.length();
        	 boolean tOrF = true;
        	 
        	 if(n.equals("0")) break;
        	 
        	 for(int i = 0; i < len/2; i++) {
        		 if(n.charAt(i) != n.charAt(len-i-1)) tOrF = false;
        	 }
        	 if(tOrF)System.out.println("yes");
        	 else System.out.println("no");
    	 }
    }
}