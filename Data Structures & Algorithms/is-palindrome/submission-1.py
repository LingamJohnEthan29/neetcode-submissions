class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.replace(" ","")
        stk = []
        for i in strs:
            if i.isalnum():
                stk.append(i.lower())
        left_ptr = 0
        right_ptr = len(stk) - 1
        while left_ptr <= right_ptr:
            left_char = stk[left_ptr]
            right_char = stk[right_ptr]
            if left_char != right_char:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True
