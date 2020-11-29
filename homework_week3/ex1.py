def sum_function(*args, **kwargs):
    sum = 0
    for arg in args:
        if isinstance(arg, (int, float)) :
            sum += arg

    for key in kwargs.keys():
        if isinstance(kwargs[key], (int, float)):
            sum += kwargs[key]

    print(f'The sum of the integer and float numbers is {sum}')
    return sum
