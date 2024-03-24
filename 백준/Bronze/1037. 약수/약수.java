import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	 Scanner sc = new Scanner(System.in);
    	 int n = sc.nextInt(); // 약수의 개수
    	 int[] num = new int[n];
    	 
    	 
    	 for (int i = 0; i < n; i++) {
    		 num[i] = sc.nextInt();
    		 
    	 }
    	 Arrays.sort(num);
    	 System.out.println((num[0])*(num[n-1])); // 최소공배수랑 최대 공약수를 곱하면 될듯!
    	 
    	 
    }
}