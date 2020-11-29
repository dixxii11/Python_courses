def check_function():
    print('Write something:')
    number_to_be_checked = input()

    try:
        if int(number_to_be_checked):
            print(f'The integer number introduced is {number_to_be_checked}.')
    except ValueError as e:
        print(f'{0}')