package 연결하여만들수있는가장큰수;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int arr[] = {10, 68, 75, 7, 21, 12};
        List<String> aList = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            aList.add(String.valueOf(arr[i]));
        }
        // Collections.sort(aList, new Comparator<String>() {
        //     @Override
        //     public int compare(String xy, String ab) {
        //         return (ab + xy).compareTo(xy + ab);
        //     }
        // });
        
        // (xy, ab) <--- 람다식의 인자
        // 화살표 오른쪽은 리턴 값을 적어주면 된다.  
        Collections.sort(aList, (xy, ab) -> (ab + xy).compareTo(xy+ab));
        for (int i = 0; i < arr.length; i++) {
            System.out.print(aList.get(i));
        }
    }
}
