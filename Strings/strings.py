import collections


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
    
    def dialingNumber(self, string):
        stri = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999"]
        n = len(string)
        ans = ""

        for i in range(n):

            if string[i] == " ":
                ans = ans + "0"
            else:
                posi = ord(string[i]) - ord("A")
                ans += stri[posi]

        return ans
    
    def repeatingChar(self, string):
        for char in string:
            count = 0
            for char2 in string:
                if char == char2:
                    count +=1
            if count > 1:
                print(char, count)
            count = 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        ans = 0
        count = Counter()
        # print(count)
        l = 0
        for r, c in enumerate(s):
          count[c] += 1
          while count[c] > 1:
            count[s[l]] -= 1
            l += 1
          ans = max(ans, r - l + 1)
          print(c, count, s[l-1])

        return ans
                    
    def characterReplacement(self, s: str, k: int)-> int:
        ans = 0
        maxCount = 0
        from collections import Counter
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])
            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)
        print(dict)
        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)
        return dict.values()
    
    def longestPalindrome(self, s: str) -> str:
        substrings = []
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1]!='':
                    substrings.append(s[i:j+1])
        maxi = 0
        ans = 0

        for i in range(len(substrings)):
            subStr = substrings[i]
            if self.isPalindrome(subStr):
                if maxi < len(subStr):
                    ans = subStr
                    maxi = len(subStr)

        return ans
    
    def countSubstrings(self, s):
        substrings = []
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1]!='':
                    substrings.append(s[i:j+1])
        setSubString = collections.Counter(substrings)

        print(setSubString)
        ans = 0
        for item in setSubString:
            if self.isPalindrome(item):
                ans+= setSubString[item]
        return ans


    def countSubstrings2(self, s: str) -> int:
        def extendPalindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0

        for i in range(len(s)):
            ans += extendPalindromes(i, i)
            ans += extendPalindromes(i, i + 1)

        return ans
    
    def strStr(self, haystack, needle):
        hLen = len(haystack)
        nLen = len(needle)

        for i in range(hLen - nLen+1):
            if haystack[i: i+nLen] == needle:
                return i
        return -1
    
    def isSubsequence(self, s, t):
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return i == len(s)
    
    # 58. Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        newString = s.strip()
        ans = 0
        for i in range(len(newString)-1, -1, -1):
            if newString[i] == " ":
                return ans
            ans+=1
        return ans
    
    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)
        print(dict)
        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)
        return dict.values()

    def numUniqueEmails(self, emails):
        unique = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))

        return len(unique)

    def isIsomorphic(self, s: str, t: str) -> bool:
        unique = {}
        ans = ''

        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] = t[i]
                ans += unique[s[i]]
            else:
                ans += unique[s[i]]
        
        unique2 = {}
        ans2 = ''

        for i in range(len(t)):
            if t[i] not in unique2:
                unique2[t[i]] = s[i]
                ans2 += unique2[t[i]]
            else:
                ans2 += unique2[t[i]]
            

        print(ans)
        return ans == t and ans2 == s

        # mapST, mapTS = {}, {}

        # for c1, c2 in zip(s, t):

        #     if ((c1 in mapST and mapST[c1] != c2) or
        #         (c2 in mapTS and mapTS[c2] != c1)):
        #         return False

        #     mapST[c1] = c2
        #     mapTS[c2] = c1

        # return True

string = String()


print(string.isIsomorphic("add", "egg"))


