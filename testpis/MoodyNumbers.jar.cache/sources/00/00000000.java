package moodynumbers;

import java.nio.ByteBuffer;
import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

/* loaded from: MoodyNumbers.jar:moodynumbers/MoodyNumbers.class */
class MoodyNumbers {
    MoodyNumbers() {
    }

    public static void main(String[] strArr) {
        Scanner scanner = new Scanner(System.in);
        NumberChecker numberChecker = new NumberChecker();
        System.out.println("Welcome to the test!");
        sleep(1000);
        System.out.println("Let's warm up with a little game");
        sleep(1000);
        System.out.println("Here's how it's going to go:");
        sleep(1000);
        System.out.println("I'm going to ask you to show me a number, and you're going to enter it in here.");
        sleep(1000);
        System.out.println("If you don't give me the right number, I'm going to get so angry that I stop talking to you.");
        sleep(1000);
        System.out.println("So don't give me the wrong numbers.");
        sleep(1000);
        System.out.println("Now that we've got that out of the way, let's begin!");
        sleep(1000);
        System.out.print("Show me a number that makes me happy: ");
        int nextInt = scanner.nextInt();
        if (!numberChecker.isHappy(nextInt)) {
            wrongNumber("THAT NUMBER DOES NOT MAKE ME HAPPY!!!");
        }
        System.out.println("Ah, that number fills me with joy! Good one!");
        sleep(1000);
        System.out.println("Okay, I have another request for you.");
        sleep(1000);
        System.out.print("I'm in the mood to be scared. Frighten me with a number: ");
        int nextInt2 = scanner.nextInt();
        if (!numberChecker.isScary(nextInt2)) {
            wrongNumber("IS THAT THE BEST YOU HAVE? THAT COULDN'T SCARE AN INFANT!!!");
        }
        System.out.println("AAAAAHHH!!! That was scary! I think I accidentally overflowed my buffer!");
        sleep(1000);
        System.out.print("Give me a number that reminds me of my childhood: ");
        int nextInt3 = scanner.nextInt();
        if (nextInt3 == 0) {
            wrongNumber("HOW DARE YOU INSULT MY CHILDHOOD!!!");
        } else if (!numberChecker.isNostalgic(nextInt3)) {
            wrongNumber("THIS NUMBER REMINDS ME OF THE TIME A MEAN HACKER ALMOST FRIED MY CIRCUITS, NOT MY CHILDHOOD!!!");
        }
        System.out.println("That number brings back memories of the time I received my first UDP packet!");
        sleep(1000);
        System.out.print("Now I want a number that arouses my circuits: ");
        int nextInt4 = scanner.nextInt();
        if (!numberChecker.isArousing(nextInt4)) {
            wrongNumber("THAT NUMBER IS SUCH A TURN-OFF THAT IT DISABLED MY NETWORK ADAPTER!!!");
        }
        System.out.println("Oooh, baby, that's a sexy number!");
        sleep(1000);
        System.out.println("Okay, you win. Here's your stupid flag. Goodbye.");
        sleep(1000);
        System.out.println(getFlag(nextInt, nextInt3, nextInt2, nextInt4));
        scanner.close();
    }

    static void sleep(int i) {
        try {
            Thread.sleep(i);
        } catch (InterruptedException e) {
        }
    }

    static void wrongNumber(String str) {
        System.out.println(str + " GET AWAY FROM ME!!!");
        System.exit(1);
    }

    static String getFlag(int i, int i2, int i3, int i4) {
        SecretKeySpec secretKeySpec = new SecretKeySpec(ByteBuffer.allocate(16).putInt(i).putInt(i2).putInt(i3).putInt(i4).array(), "AES");
        try {
            Cipher cipher = Cipher.getInstance("AES");
            cipher.init(2, secretKeySpec);
            return new String(cipher.doFinal(new byte[]{-117, -29, 88, 105, 5, -57, 110, -22, 120, -6, -62, 93, 31, -58, -114, -104, -12, -117, 3, 33, -106, -82, -65, -57, -27, 58, 0, -7, -120, 122, -116, -97, 31, 84, -82, 59, 32, -117, 70, 60, 110, 95, 19, -7, -117, -87, Byte.MIN_VALUE, 29}));
        } catch (Exception e) {
            System.out.println("An error occurred: " + String.valueOf(e));
            return "ERROR";
        }
    }
}