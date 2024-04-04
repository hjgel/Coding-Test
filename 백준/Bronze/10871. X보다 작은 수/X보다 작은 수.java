import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] result = new int[N];
		int[] s = new int[N];
		int count = 0;
		for(int i = 0; i < N; i++) {
			s[i] = sc.nextInt();
			if(s[i] < K) {
				result[i] = s[i];
			}
		}
		for(int i = 0; i< result.length; i++) {
			if(result[i] != 0) {
				System.out.print(result[i] + " ");
			}
		}

	}
}
