class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        for i in range(len(height)):
            hei = height[i]
            if i < 1:
                continue
            left_height = max(height[:i])
            right_height = max(height[i:])
            area = min(left_height,right_height)-hei
            if area > 0:
                trapped += area
        return trapped