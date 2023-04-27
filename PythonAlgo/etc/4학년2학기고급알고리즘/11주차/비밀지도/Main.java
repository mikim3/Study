package 비밀지도;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        // int arr1 = {9,20,28,18,11};
        // int arr2 = {30, 1, 21,17,28};
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr1 = new int[n];
        int[] arr2 = new int[n];

        for (int i = 0; i < arr1.length; i++) {
            arr1[i] = sc.nextInt();
        }
        for (int i = 0; i < arr2.length; i++) {
            arr2[i] = sc.nextInt();
        }
        int row;
        for (int i = 0; i < arr2.length; i++) {
            row = arr1[i] | arr2[i];
            System.out.print("[");
            for (int j = n-1; j >= 0; j--) {
                if (((row >> j) & 1) == 1) {
                    System.out.print("#");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println("]");
        }
    }
}

