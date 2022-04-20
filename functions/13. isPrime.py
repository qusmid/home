def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

n = int(input("Input the number: "))
print(is_prime(n))