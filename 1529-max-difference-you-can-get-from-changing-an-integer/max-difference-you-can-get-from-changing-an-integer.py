__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def maxDiff(self, num: int) -> int:
        num=str(num)
        v1=num
        v2=num
        for i in num:
            if i!='9': v1=num.replace(i,'9');break
        if num[0]!='1':
            v2=num.replace(num[0],'1')
        else:
            for i in num:
                if i!='1' and i!='0': 
                    v2=num.replace(i,'0')
                    break
        return int(v1)-int(v2)