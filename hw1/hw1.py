import math
def compute_gcd(a,b):
    mod = b % a
    if mod == 0:
        return a
    else:
        return compute_gcd(mod, b)
    
print(f"1.b {compute_gcd(455,1235)}")


def find_p():
    from sympy import isprime
    p = 0
    x = 0
    while x == 0:
        p+=1
        if not isprime(2**p - 1) and isprime(p):
            x=1
    return p



print(f"2.a {find_p()}")

def find_all_primes():
    from sympy import isprime
    prime_list = []
    for i in range(2,100):
        if isprime(i) and isprime(2**i - 1):
            prime_list.append(i)
    return prime_list

print(f"2.b {find_all_primes()}")

def find_k():
    from sympy import isprime 
    p = 0
    x = 0
    k = 0
    prime_list2 = []
    while x == 0:
        p+=1
        if isprime(p):
            k += 1
            prime_list2.append(p)
            n = math.prod(prime_list2) + 1
            if not isprime(n):
                x = 1
    
    return k

print(f"4.a {find_k()}")

def find_ks():
    from sympy import isprime, primerange
    k_list = []
    prime_list = []
    k = 0
    for p in primerange(0,100):
        k+=1
        prime_list.append(p)
        n = math.prod(prime_list) + 1

        if isprime(n):
            k_list.append(k)

    return k_list

print(f"4.a {find_ks()}")
