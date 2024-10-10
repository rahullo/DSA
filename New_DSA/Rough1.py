# import numpy as np

# # Define the matrix A
# A = np.array([[4, 1],
#               [2, 3]])

# # Compute eigenvalues and eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(A)

# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:\n", eigenvectors)

def collatz(n):
    if n == 1:
        x = 0
        return x
    elif n%2 == 0:
        return collatz(n/2) + 1
    else:
        return collatz((n*3)+1) + 1

# print(collatz(1000))

def happySad(n):
    happy = n
    sad = 0
    for i in range(3):
        temp = happy
        happy = (happy *0.3) + (sad * 0.5)
        sad = (temp * 0.7) + (sad * 0.5)
    return happy, sad

# print(happySad(3000))

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def sumPrime(n):
    sum = 0
    for i in range(1, n+1):
        
        if is_prime(i):
            sum += i
        
    return sum

print(sumPrime(10))