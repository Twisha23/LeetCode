class Solution {
    public int minSubArrayLen(int k, int[] nums) {
        int sum = 0;
        int minLen = Integer.MAX_VALUE;
        int i = 0;

        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];  // Accumulate sum instead of subtracting

            // While current window sum is greater than or equal to k
            while (sum >= k) {
                minLen = Math.min(minLen, j - i + 1);  // Update min length
                sum -= nums[i];  // Shrink window from the left
                i++;
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
