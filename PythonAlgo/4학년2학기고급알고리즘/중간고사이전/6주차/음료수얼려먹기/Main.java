package 음료수얼려먹기;

import java.util.Scanner;

public class Main {
    static int graph[][] = new int[1000][1000];
    static int n,m;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++)
        {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }
        sc.close();

        int result = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++) {
                if (dfs(i,j)) {
                    result += 1;

                }
            }
        }
        System.out.println(result);
    }
    public static boolean dfs(int x, int y) {
        if (x <= -1 || x>= n || y <= -1 || y>= m){
            return false;
        }
        if (graph[x][y] == 0) {
            graph[x][y] = 1;
            dfs(x-1,y);
            dfs(x, y-1);
            dfs(x+1,y);
            dfs(x,y+1);
            return true;
        }
        return false;
    }
}
