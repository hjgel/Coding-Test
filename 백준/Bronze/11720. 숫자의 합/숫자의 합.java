import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int sum = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int C = Integer.parseInt(br.readLine());
		String N = br.readLine();

		for(int i = 0; i < C; i++) {
			int S = Integer.parseInt(N.substring(i,i+1));
			sum += S;
		}
		System.out.println(sum);
	}
}
