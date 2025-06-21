# Comma separated Values (CSV)

import csv

# Use forward slashes or raw strings for file paths to avoid escape character issues
with open('File-handling/CSV/users.csv', mode='r') as file:
    file_reader = csv.reader(file, delimiter=',', quotechar='"')

    # Use the csv_reader object, not the file object directly
    for row in file_reader:
        print(row)
    # No need to call file.close() when using 'with' statement - it auto-closes