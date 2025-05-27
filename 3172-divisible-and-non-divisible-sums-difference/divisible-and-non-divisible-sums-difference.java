class Solution {
    public int differenceOfSums(int n, int m) {
        // n tak ke saare numbers ka sum nikalenge
        int totalSum = (n * (n + 1)) / 2;
        
        // n tak ke saare m ke multiples ka sum nikalenge
        int multipleSum = m * (n / m) * ((n / m) + 1) / 2;

        // n tak ke saare numbers ka sum jo m se divisible nahi hain
        int nonMultipleSum = totalSum - multipleSum;

        // nonMultipleSum aur multipleSum ka difference return karenge
        return nonMultipleSum - multipleSum;
    }
}