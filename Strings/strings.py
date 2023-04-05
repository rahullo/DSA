class String():

    def isPalindrome(self, string):
        l = 0
        r = len(string)-1

        while l < r:
            while l < r and not string[l].isalnum():
                l+=1
            while l < r and not string[r].isalnum():
                r-=1
            if string[l].lower() != string[r].lower():
                return False
            l+=1
            r-=1
        return True
    
    def validPalindrome(self, s):
        l = 0
        r = len(s) -1 
        de = 0
        while l < r:
            if s[l] != s[r]:
                r-=1
                if de > 1:
                    return False
                de +=1
            l +=1
            r -=1
        return True
    
    def isAnagram(self, s, t) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        
        dict = Counter(s)

        for c in t:
            dict[c] -= 1
            if dict[c] < 0:
                return False
        return True
    
    def isValid(self, s):
        stack = []
        
        mapping = {
            '(':')',
            '[':']',
            '{':'}'            
        }
        
        for char in s:
            print(char)
            if char in mapping.keys():
                print("First IF")
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                print("Second IF")
                return False
            else:
                print("Third IF")
                stack.pop()
        
        return len(stack)==0
    
    def removeConsecutiveCharacter(self, S):
        s2 = ""
        prev = None
        
        for char in S:
            if prev != char:
                s2+=char
                prev = char
        return s2
    
    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ""
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][0:i]
                
        return strs[0]
                    




string = String()

# print(string.isValid("()"))
# print(string.isValid("()[]{}"))
# print(string.isValid("(]"))
print(string.longestCommonPrefix(["flower","flow","flight"]))