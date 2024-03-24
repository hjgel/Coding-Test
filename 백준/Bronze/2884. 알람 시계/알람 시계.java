import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        
         Scanner scanner = new Scanner(System.in);
         int H = scanner.nextInt();
         int M = scanner.nextInt();
         
         if (M < 45) {
        	 if (H == 0) H = 23;
        	 else --H;
        	 M = 60 + M - 45;
        	 System.out.printf("%d %d", H, M);
         } else if (M >= 45) {
        	 M = M - 45;
        	 System.out.printf("%d %d", H, M);
         } 
    }
}