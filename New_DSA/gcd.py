def gcd(m, n):
    i=2
    ans = 1;
    while(i<=m and i <= n):
        if(m % i==0 and n % i == 0):
            ans = i;
        i+=1
    return ans

print(f"GCD: {gcd(14,28)}")