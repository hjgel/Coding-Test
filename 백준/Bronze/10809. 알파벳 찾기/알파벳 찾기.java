import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int sum = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();

        int[] cnt = new int[26];
        for(int i = 0; i < 26; i++){
        	cnt[i] = -1;
        }
        for(int i = 0; i < S.length(); i++) {
        	char ch = S.charAt(i);
            if(cnt[ch-'a'] == -1) {
            	cnt[ch-'a'] = i;
            }
        }
        
        for(int i : cnt) {
        	System.out.print(i + " ");
        }
	}
}
