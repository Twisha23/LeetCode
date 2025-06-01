class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        is_neg = False
        digits = []
        limit = [2,1,4,7,4,8,3,6,4,7]
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        if s[i] not in '-+0123456789':
            return 0
        if s[i] in '-+':
            is_neg = True if s[i] == '-' else False
            i += 1
        if i == len(s):
            return 0
        while i < len(s) and s[i] == '0':
            i += 1
        if i == len(s) or not s[i].isdigit():
            return 0
        while i < len(s) and len(digits) < 11 and s[i].isdigit():
            digits.append(int(s[i]))
            i += 1
        if len(digits) == 11:
            return (-2 ** 31) if is_neg else (2 ** 31 - 1)
        outside_range = None
        if len(digits) == 10:
            if digits <= limit:
                outside_range = False
            else:
                if digits[0:9] != limit[0:9] or not is_neg:
                    outside_range = True
                elif digits[9] > limit[9] + 1:
                    outside_range = True
                else:
                    outside_range = False
                
        if outside_range:
            return (-2**31) if is_neg else (2**31 - 1)
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        if is_neg:
            num *= -1
        return num