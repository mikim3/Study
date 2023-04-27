package 비트연산을통해짝수1홀수판별하기;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (isEven(n) == 0)
            System.out.println("ODD");
        else
            System.out.println("EVEN");
        sc.close();
    }
    private static int isEven(int n) {
        if ((n ^ 1) == n+1)
            return 1;
        return 0;
    }
}
