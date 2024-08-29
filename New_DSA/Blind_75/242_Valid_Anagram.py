def isAnagram_1(s, t):
    if len(s) != len(t):
        return False
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


print(isAnagram('rahul', 'luhra'))