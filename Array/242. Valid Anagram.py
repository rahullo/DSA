from collections import Counter

def isAnagram(s, t):
    dict = Counter(s)

    if len(s) != len(t):
        return False

    for c in t:
        dict[c] -= 1
        if dict[c] < 0:
            return False
        
    return True


print(isAnagram('anagram', 'naagram'))
print(isAnagram('Rahul', 'luhaR'))
print(isAnagram('anagram', 'naagram'))