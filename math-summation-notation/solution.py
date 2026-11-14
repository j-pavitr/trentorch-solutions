def summation(f, lo, hi):
    total = 0

    if hi < lo:
        return 0

    for i in range(lo, hi + 1):
        total = total + f(i)

    return total
    # TODO: Implement the summation from Theory as an explicit loop.
    pass
