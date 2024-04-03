import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long num = sc.nextInt();
		factorial(num);
		System.out.println(factorial(num));
		
		sc.close();
	}
	
	static long factorial(long num) {
		if (num == 0 || num == 1) {
			return 1;
		}
		return num * factorial(num-1);
	}
}
