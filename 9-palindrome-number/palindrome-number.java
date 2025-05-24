class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false; 
        }
        int Number = x;
        int reversed = 0;
        while (x > 0) {
            int lastDigit = x % 10; 
            reversed = (reversed * 10) + lastDigit; 
            x /= 10; 
        }
        return Number == reversed;
    }
}