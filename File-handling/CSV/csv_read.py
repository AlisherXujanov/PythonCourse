import csv

with open('users.csv', mode='r') as file:
    file_reader = csv.reader(file, delimiter=',', quotechar='"')

    for row in file:
        print(row)
    file.close()