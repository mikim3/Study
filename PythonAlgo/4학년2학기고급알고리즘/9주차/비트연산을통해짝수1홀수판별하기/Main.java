package 비트연산을통해짝수1홀수판별하기;


public class Main {
    public static void main(String[] args){
        
        System.out.println(isEven(5));
        
    }

    private static int isEven(int n) {
        if ((n ^ 1) == n+1)
            return 1;
        return 0;
    }
}
