package 배열의왼쪽값간략;

public class Main {
    public static void main(String[] args) {
        int[] arr = {5,1,4,3,6,8,10,7,9};
        int n = arr.length;
        System.out.println("결과 = " + findElement(arr,n));
    }
    public static int findElement(int[] arr, int n) {
        int[] leftMax = new int[n];
        // 가장 왼쪽을 작은 값으로
        leftMax[0] = Integer.MIN_VALUE;
        // 1번 인덱스부터 가장 작은 값으로 leftMax[] 배열의 값을 채워나간다.
        for (int i = 1; i < leftMax.length; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], arr[i-1]);
        }
        int rightMin = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            if (leftMax[i] < arr[i] && arr[i] < rightMin) 
                return i;
            // 작은값으로 갱신
            rightMin = Math.min(rightMin, arr[i]);
        }
        return -1;
    }
}
