def binPow(a, n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        return (a **(n/2)) ** 2
    elif n > 0 and n%2 != 0:
        return ((a **((n-1)/2)) ** 2) * a
    
# print(int(binPow(2, 9)))

# def binPow2(a, n):
#     if n == 0:
#         return 1

#     res = binPow2(a, n/2)
#     if n % 2:
#         return res * res * a
#     else:
#         return res * res

# print(binPow2(2, 9))

############################
#####################################
#####  GCD or HCF
def gcd(a, b):
    if(b == 0):
        return a
    elif a == 0:
        return b
    else:
        return gcd(b, a%b)

# print(gcd(30, 15))

#########   By swaping 
def gcdSwap(a, b):
    while(b):
        a %= b
        a, b = b, a
    return a

def lcm(a, b):
    return int(a / gcd(a, b) * b)

print(lcm(12, 6))