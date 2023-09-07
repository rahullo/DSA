###################
# 231. Power of Two
def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    
    return isPowerOfTwo(n/2)
    


# print(isPowerOfTwo(30))
