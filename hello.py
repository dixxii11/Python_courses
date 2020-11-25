#python_no2

list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

list.sort() #
sorted_list = list
my_sliced_even_list = sorted_list[::2]
my_sliced_odd_list = sorted_list[1::2]
lista_multiplii = []

print(f"Lista ordonata ascendent: {sorted_list}")
print(f"Numere cu indici pari: {my_sliced_even_list}")
print(f"Numere cu indici impari: {my_sliced_odd_list}")
for i in sorted_list:
    if i % 3 == 0:
        lista_multiplii.append(i)

print(f"Multiplii lui 3: {lista_multiplii}")