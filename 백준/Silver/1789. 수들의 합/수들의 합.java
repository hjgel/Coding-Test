
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		
		long count = 0;
		long number = 0;
		long i = 1;
		while(N >= number) {
			number = number + i;
			i ++;
			count++;
		}
		System.out.println(count-1);
		
		sc.close();
	}

}
