package 소수구하기_1929;

import java.math.BigInteger;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        sc.close();
        
        IntStream.rangeClosed(start, end).boxed()
                .filter(i -> BigInteger.valueOf(i).isProbablePrime(10)).collect(Collectors.toList())
                .forEach(i -> System.out.println(i));
    }
}