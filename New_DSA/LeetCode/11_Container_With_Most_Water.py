class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            minheight = min(height[l], height[r])
            ans = max(ans, minheight * (r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans

        

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))