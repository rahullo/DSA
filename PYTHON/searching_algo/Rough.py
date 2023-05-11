# import math
# import os

# def findNthRootOfM(n,m):
#     ans = m ** (1/n)
#     return '{0:.6f}'.format(ans)

# print(findNthRootOfM(4, 69))
from collections import Counter

def lengthOfLongestSubstring(s):
    ans = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
        # print(r, c)
        count[c] += 1
        print(count)
        while count[c] > 1:
            count[s[l]] -= 1
            l += 1
            ans = max(ans, r - l + 1)
    
    return ans

print(lengthOfLongestSubstring('abcabcbb'))