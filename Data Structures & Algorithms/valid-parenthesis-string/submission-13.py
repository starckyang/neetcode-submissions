class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy
        up, down=0, 0
        for c in s:
            if c=="(":
                up+=1
                down+=1
            elif c==")":
                up-=1
                down-=1
                if up<0:
                    return False
            else:
                up+=1
                down-=1
            down=max(0, down)
        return down==0     