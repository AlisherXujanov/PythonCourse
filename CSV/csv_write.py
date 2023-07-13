
import csv

# we need to install faker by running the following command in the terminal (pip/pipenv install faker)
from faker import Faker

fake = Faker()

with open('users.csv', mode='w') as file:
    file_writer = csv.writer(
        file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # csv.writer expects a list of values
    # file =>  file object to write to (created with open())
    # delimiter => character used to separate fields
    # quotechar => character used to quote fields containing special characters
    # quoting => controls when quotes should be generated by the writer

    file_writer.writerow(['first_name', 'last_name', 'email', 'bio'])

    for _ in range(100):
        file_writer.writerow(
            [fake.first_name(), fake.last_name(), fake.email(), fake.text()])
