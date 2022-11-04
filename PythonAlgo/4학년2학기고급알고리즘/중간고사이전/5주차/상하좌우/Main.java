package 상하좌우;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String plans = sc.nextLine();
        int x = 1, y = 1;
        int dx[] = {0, 0, -1, 1};
        int dy[] = {-1, 1, 0, 0};
        char[] moveTypes = {'L','R','U','D'};
        int nx = 0, ny = 0;
        for (int i = 0; i < plans.length();i++){
            char plan = plans.charAt(i);
            for (int j = 0;j < moveTypes.length;j++){
                if(plan == moveTypes[j]){
                    nx = x + dx[j];
                    ny = y + dy[j];
                }
                if (nx < 1 || nx > n || ny < 1 || ny > n){
                    continue;
                }
                x = nx;
                y = ny;
            }
        }
        System.out.println(x + " " + y);
    }
}
