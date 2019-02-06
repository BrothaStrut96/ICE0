//  Problem 2 (Located: https://wiki.sei.cmu.edu/confluence/display/java/NUM00-J.+Detect+or+prevent+integer+overflow)


class vun2 {

    public static int multAccum(int oldAcc, int newVal, int scale) {
        // May result in overflow
        return oldAcc + (newVal * scale);
    }

    public static int multAccum(int oldAcc, int newVal, int scale) {
        return safeAdd(oldAcc, safeMultiply(newVal, scale));
    }

    //cannot result in overflow, as the safeAdd method handles the overflow check.

}
