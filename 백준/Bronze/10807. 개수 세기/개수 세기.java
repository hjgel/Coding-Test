import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] s = new int[N];
		int count = 0;
		for(int i = 0; i < N; i++) {
			s[i] = sc.nextInt();
		}
		int v = sc.nextInt();
		for(int i = 0; i < N; i++) {
			if(s[i] == v) {
				count++;
			}
		}
		System.out.println(count);
	}
}