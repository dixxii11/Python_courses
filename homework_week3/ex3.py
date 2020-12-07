def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)




def get_even_sum(n):
    if n <= 0:
        return 0
    elif n % 2 == 1:
        return get_even_sum(n - 1)
    else:
        return n + get_even_sum(n - 1)

def get_odd_sum(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return get_odd_sum(n - 1)
    else:
        return n + get_odd_sum(n - 1)

