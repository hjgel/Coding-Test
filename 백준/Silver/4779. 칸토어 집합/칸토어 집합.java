import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static StringBuilder sb; // 전역변수 설정 
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str;
		
		while((str = br.readLine()) != null) { // str = br.readLine() != null
			n = Integer.parseInt(str);
			int len = (int)Math.pow(3, n);  // 제곱을 구하는 숫자함수 
			
			sb = new StringBuilder();
			for(int i = 0; i < len; i++) {
				sb.append("-"); // 27개만큼 들어감. 
			}

			func(0, len); // 시작 인덱스, 시작 길이 0번째 인덱스랑 27.
			System.out.println(sb);
		}
	}
	
	public static void func(int start, int size) { // 0, 27 들어감
		if(size == 1) { // size가 1이면 그냥 그대로 리턴, 
			return;
		}
		
		int newSize = size / 3; // newSize = 9로 설정 
		
		for(int i = start + newSize; i < start + 2 * newSize; i++) { // i = 0 + 9; i가 0 + 2 * 9(18)만큼; i++)
			sb.setCharAt(i,  ' '); // setCharAt(인덱스, 교체할문자) : 인덱스번호에 있는 문자를 해당 문자로 교체해줌. 9 ~ 17만큼 지워줌 총 9개.
		}
		func(start, newSize); // 0, 9 new size가 1이 될 때 까지 재귀함. 왼쪽 자리 정리
		func(start + 2 * newSize, newSize); // 0+2 * 9(18), newSize(9). 오른쪽 자리 정리
	}
}