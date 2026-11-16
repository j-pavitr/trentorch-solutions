def factorial(n):
    total = 1
    for i in range(1,n+1):
        total = total*i
    return total
    pass


def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))
    pass
