import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(reader.readLine());
        int N = Integer.parseInt(reader.readLine());
        int result = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine()); // 줄바꿈 전에 공백으로 분할해줌
            int a = Integer.parseInt(st.nextToken()); // 물건 가격
            int b = Integer.parseInt(st.nextToken()); // 물건 개수
            result += (a * b);
        }

        if (result == X) { System.out.println("Yes"); }
        else { System.out.println("No"); }
    }
}