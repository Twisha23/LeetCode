class Solution(object):
    def addDigits(self, x):
        if x == 0:
            return 0
        
        last_digit = x % 10
        rem = x // 10

        # Convert remaining digits to list and calculate sum
        digits = [int(d) for d in str(rem)]
        summ = last_digit + sum(digits)

        if summ > 9:
            return self.addDigits(summ)
        else:
            return summ
