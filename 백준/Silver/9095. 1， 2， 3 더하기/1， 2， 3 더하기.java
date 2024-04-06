import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException   {
		int dp[] = new int [11];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		dp[1] = 1; //초기 값 초기화
		dp[2] = 2;
		dp[3] = 4;
		
		for(int j=4;j<=10;j++) { // 4부터 10까지 값 출력.
			dp[j] = dp[j-3] + dp[j-2] + dp[j-1]; 
		}
		// dp[4] = 1 + 2 + 4
		// dp[5] = 2 + 4 + 7
		// dp[6] = 4 + 7 + 13
		// dp[7] = 7 + 13 + 24
		// dp[8] = 13 + 24 + 44
		// dp[9] = 24 + 44 + 81
		// dp[10] = 44 + 81 + 149
		
		for(int i=0; i < T; i++) {
			int n = Integer.parseInt(br.readLine());
			
			System.out.println(dp[n]);
		}
	}
}