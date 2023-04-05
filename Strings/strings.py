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
    
string = String()

print(string.isPalindrome("hannah"))