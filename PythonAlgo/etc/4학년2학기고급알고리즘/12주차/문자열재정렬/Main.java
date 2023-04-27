package 문자열재정렬;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // String input = "K1KA5CB7";
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        List<Character> list = new ArrayList<>();  
        
        int value = 0;
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            // if (Character.isLetter(ch))
            if (ch >= 65 && ch <= 90) {
                list.add(ch);
            } else {
                value += ch - '0';
            }
        }
        Collections.sort(list);
        for (Character item : list) {
            System.out.print(item);
        }
        if (value != 0) 
            System.out.println(value);
        sc.close();
    }
}
