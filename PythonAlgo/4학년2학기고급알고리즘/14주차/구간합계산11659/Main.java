package 구간합계산11659;

import java.util.*;

class Main {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] arrS = new int[n+1];
    for (int i = 1; i <= n; i++) {
        arrS[i] = arrS[i-1] + sc.nextInt();
    }
    for (int i = 0; i < m; i++) {
        int left = sc.nextInt();
        int right = sc.nextInt();
        System.out.println(arrS[right] - arrS[left - 1]);
    }
}
