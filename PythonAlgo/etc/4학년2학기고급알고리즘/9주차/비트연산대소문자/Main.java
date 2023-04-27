package 비트연산대소문자;

import java.util.Scanner;

// 교수님 코드
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println("ori String : " + str);
        str = toggleCase(str.toCharArray());
        System.out.println("toggle case :" + str);

        sc.close();
    }
    public static String toggleCase(char[] a){
        for (int i = 0; i< a.length; i++) {
            a[i] ^= 32;
        }
        return new String(a);
    }

}
