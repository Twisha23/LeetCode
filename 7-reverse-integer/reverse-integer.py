class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_signed = 2**31 - 1
        min_signed = -2**31
        temp = x
        if(x < 0):
            x = x * -1
        reversed = 0
        while (x > 0) :
            lastDigit = x % 10
            reversed = (reversed * 10) + lastDigit
            x /= 10

        if (temp < 0):
            reversed = reversed * (-1)

        if reversed < min_signed or reversed > max_signed:
            return 0
        return reversed
        