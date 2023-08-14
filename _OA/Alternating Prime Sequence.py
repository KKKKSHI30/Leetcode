def minPenalty(arr):
    prime = []
    n_prime = []
    for num in arr:
        if isPrime(num):
            prime.append(num)
        else:
            n_prime.append(num)
    red = max(len(prime), len(n_prime)) - (min(len(prime), len(n_prime))+1)
    if len(prime) == len(n_prime):
        return 0
    elif len(prime) < len(n_prime):
        return sum(sorted(n_prime)[:red])

def isPrime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


arr = [1,2,4,3,6,5]
arr2 = [3,7,1,4,6,6,5]
minPenalty(arr2)