# print('Curs 3')
#
# my_var = 50
#
# if my_var < 6:
#     print('Variabila noastra e mai mica decat 6')
# elif my_var < 10:
#     print('Variabila noastra e mai mare decat 6 si mai mica decat 10')
# elif my_var < 25:
#     print('Variabila noastra e destul de mare')
# else:
#     print('Variabila noastra e mare')
#
# apples = 0
# has_apples = 'Are mere' if apples else 'Nu are mere'
# print(has_apples)
#
# import random
#
# # l = []
# # for x in range(11):
# #     l.append(x)
# # print(l)
#
# choises = [x for x in range(11)]
# while True:
#     random_choise = random.choice(choises)
#     if random_choise % 3 == 0:
#         break
#     print(f'Random choice is {random_choise}')
#
# print(f'Exit Random choice is {random_choise}')
#
# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(f'{i} este par')
#
# def my_function(list_param):
#     local_list_param = list(list_param)
#     local_list_param.append(4)
#     print('list_param inside function', local_list_param)
#
# list_param = [1, 2, 3]
# my_function(list_param)
# print('list_param outside function',list_param)
#
# def my_function(name, age, job_name='Student', has_car=True):
#     has_car_str = 'a car' if has_car else 'no car'
#
#     print(f'My name is {name} and mu age is {age}. I\', a {job_name} and I hav {has_car_str}')
#
#
# my_function('John', 21)
# my_function('Maria', 30, 'Developer', False)
#
def  my_function(*args, **kwargs):
    print(args)
    print(kwargs)
    for arg in args:
        print(f'arg is {arg}')
    for key in kwargs.keys():
        print(f'key {key} has value {kwargs[key]}')

    print('-' * 80)

my_function('Ana')
my_function('Ana', 'are', 'mere')
my_function(name='Ana', verb='are', complement='mere')
my_function(1, 2, 3, name='Ana', verb='are', complement='mere')
#
# while True:
#     my_var = input('Introduceti un nr:')
#     try:
#         my_int = int(my_var)
#         print(mi_int)
#     except ValueError as e:
#         print('Va rog introduceti un intreg')
#     except NameError as e:
#         # print('Ai folosit o variabila nedefinita!')
#         pass
#     else:
#         print('Nici o exceptir nu a fost aruncata')
#     finally:
#         print('Se executa tot timpul')
#
# def my_function():
#     global msg
#     msg = 'Hello world'
#     print(msg)
#
# my_function()
# print(msg)
#
# def my_function():
#     def my_second_function():
#         print(f'my_second_function {msg}')
#
#     msg = 'Hello world'
#     my_second_function()
#     print(f'my_function {msg}')
#
# my_function()