class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in '[({':
                stk.append(i)
            else:
                if stk:
                    if stk.pop()+i not in ['()','{}','[]']:
                        return False
                else:
                    return False
        if stk:
            return False
        return True
        
