import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		for(int i = a; i <= b; i++) {
			if (sosu(i)) System.out.println(i);
		}
		sc.close();
	}
	
	public static boolean sosu(int i) {
		int j = 2;
		if (i < 2) return false;
		while (j*j <= i) {
			if (i % j == 0) {
				return false;
			}
			j += 1;
		}
		return true;
	}
}
