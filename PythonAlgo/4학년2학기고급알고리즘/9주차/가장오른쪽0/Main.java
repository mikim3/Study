package 가장오른쪽0;

import java.util.Scanner;

// 교수님 코드
// 근데 교수님이말하길 이런거 필요없고 중간꺼랑 원래수랑
// 비트OR하면 끝
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("result = " + setRightMostUnsetBit(n));

        sc.close();
    }
    public static int setRightMostUnsetBit(int n) {
        if (n == 0) return 1;
        if ((n & (n+1)) == 0) return n;
        int pos = getPosOfRightMostSetBit(n);

        return ((1 << pos) | n);
    }
    public static int getPosOfRightMostSetBit(int n) {
        return (int)(Math.log(~n & (n+1)) / Math.log(2));
    }
}
