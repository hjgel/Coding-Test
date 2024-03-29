import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> a = new ArrayList<Integer>();
		int cnt = 0; 
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		for(int i = 1; i <= N; i++ ) {
			int j = sc.nextInt();
			a.add(j);
		}
		
		Collections.reverse(a);
		
		for (int i : a) {
			while(i <= K) {
				K = K - i;
				cnt++;
			}
		}
		System.out.println(cnt);
		sc.close();
	}
}