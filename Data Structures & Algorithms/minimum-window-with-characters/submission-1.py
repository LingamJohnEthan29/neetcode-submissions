from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        minLen = float('inf')
        minWin = ""

        if len(s) < len(t):
            return ""

        charS = Counter(t)
        charCounter = {}

        have = 0
        need = len(charS)

        while r < len(s):
            element = s[r]

            if element not in charCounter:
                charCounter[element] = 1
            else:
                charCounter[element] += 1

            if element in charS and charCounter[element] == charS[element]:
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    minWin = s[l:r + 1]

                ele = s[l]
                charCounter[ele] -= 1

                if ele in charS and charCounter[ele] < charS[ele]:
                    have -= 1

                l += 1

            r += 1

        return minWin