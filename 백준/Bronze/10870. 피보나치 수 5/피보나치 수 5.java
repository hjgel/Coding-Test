import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		
		System.out.println(fibonachi(num));
	}
	
	static int fibonachi(int num) {
		if(num == 0) {
			return 0;
		}
		if (num == 1 || num == 2) {
			return 1;
		}
		return fibonachi(num - 1) + fibonachi(num - 2);
	}
}