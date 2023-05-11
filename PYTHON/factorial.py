def factorialIterative(number):
    ans = 1
    for i in range(1, number+1):
        ans = ans * i

    return ans

# print(factorialIterative(100))


def factorialRecursive(number):
    if(number == 1):
        return number

    return number * factorialRecursive( number  - 1)

# print(factorialRecursive(4))

