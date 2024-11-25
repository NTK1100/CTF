package moodynumbers;

import java.math.BigInteger;
import java.security.MessageDigest;

/* loaded from: MoodyNumbers.jar:moodynumbers/NumberChecker.class */
public class NumberChecker {
    public boolean isHappy(int i) {
        return i % 270719 == 0 && i / 270719 == 6317;
    }

    public boolean isScary(int i) {
        return (i & 255) == 0 && (i >> 12) == 0 && ((i >> 8) ^ 15) == 4;
    }

    public boolean isNostalgic(int i) {
        try {
            return String.format("%032x", new BigInteger(1, MessageDigest.getInstance("MD5").digest(Integer.toString(i).getBytes("UTF-8")))).equals("08ef85248841b7fbf4b1ef8d1090a0d4");
        } catch (Exception e) {
            System.out.println("An error occurred: " + String.valueOf(e));
            return false;
        }
    }

    public boolean isArousing(int i) {
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