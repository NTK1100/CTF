public class Main {
    public static void main(String[] args) {
        for(int i = 10000; i <= 1000000000; i++) {
            if (isArousing(i)) 
                System.out.println(i + " is arousing");
        }
    }

    public static boolean isArousing(int i) {
        int i2 = i % 10;
        int i3 = i / 10;
        int i4 = i3 % 10;
        int i5 = i3 / 10;
        if (i4 % 2 != 0 || i2 != (i4 / 2) * 3) {
            return false;
        }
        for (int i6 = 0; i6 < 3; i6++) {
            if (i5 % 10 != i2) {
                return false;
            }
            int i7 = i5 / 10;
            if (i7 % 10 != i4) {
                return false;
            }
            i5 = i7 / 10;
        }
        return i5 == 0 && i2 % 2 != 0 && (i2 ^ i4) == 15;
    }
}
//69696969
//PIS{th1s_1s_why_c0mpu73rs_d0n7_h4v3_f33l1ng5}