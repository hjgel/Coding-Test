import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int oneCount = 0;
	static int zeroCount = 0;
	static int zero_plus_one;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();

		for(int i = 0; i < count; i++) {
			int num = Integer.parseInt(br.readLine());
			fibonachi(num);
			sb.append(zeroCount).append(' ').append(oneCount).append('\n');
		}
		System.out.println(sb);
	}
	
	public static void fibonachi(int num) {
		// 반드시 초기화 해야한다.
		zeroCount = 1;
		oneCount = 0;
		zero_plus_one = 1;
 
		for (int i = 0; i < num; i++) {
			zeroCount = oneCount;
			oneCount = zero_plus_one;
			zero_plus_one = zeroCount + oneCount;
		}
	}
}