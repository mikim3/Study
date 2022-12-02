package 소수의판별기본;

public class Main { 
    public static void main(String[] args) {
        System.out.println(isPrimeNumber(4));
        System.out.println(isPrimeNumber(7));
    }
    public static boolean isPrimeNumber(int x) {
        // 2부터 (x - 1)까지의 모든 수를 확인하며
        for (int i = 2; i < x; i++) {
            // x가 해당 수로 나누어떨어진다면
            if (x % i == 0) {
                return false; // 소수가 아님
            }
        }
        return true; // 소수임
    }

}
