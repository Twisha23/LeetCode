class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        double maxSum = Integer.MIN_VALUE;
        int i = 0; int j = 0;
        while(j < nums.length){
            sum += nums[j];
            if(j - i +1 < k){
                j++;
            }
            else if(j-i+1 == k){
                maxSum = Math.max(maxSum, sum);
                sum -= nums[i];
                i++; j++;
            }
        }  return maxSum/k; 
    }
}