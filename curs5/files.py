# with open('data.txt', 'w') as file:
#     file.write('Hello world!')


with open('data.txt', 'r') as file:
    for line in file.readlines():
        print(f'line: {line}', end='')

# import csv
# with open('cars.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     for row in rows:
#         print(row)
