# To work with postgresql we need to install psycopg2-binary
# pip install psycopg2-binary
import os
import faker
import psycopg2
import requests

# Connecting to the database
conn = psycopg2.connect(
    user="postgres",
    password="qweqweqwe",
    host="localhost",
    port="5432",
    database="postgres"
)
# This is for autocommiting the changes
# It means that we don't need to commit every time
# to save the changes in the database
# Otherwise, we need to commit every time when we
# change something by using conn.commit()
conn.autocommit = True

# This is the cursor
cur = conn.cursor()

# Creating the table
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    birthdate DATE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    bio TEXT
);
''')
cur.execute('''INSERT INTO table_name 
    VALUES (...)
''')  # - to insert data into the table

# ========================================================
# Insert 10000 rows of people into users table
# Each should have name, email, password, country
# Use faker to insert all the data
fake = faker.Faker()
for i in range(10):
    cur.execute('''
        INSERT INTO users 
        (birthdate, first_name, last_name, email, bio) 
        VALUES (%s, %s, %s, %s, %s);
        ''', (
        fake.date(),       # - generates 'YYYY-MM-DD'
        fake.first_name(), # - generates first name
        fake.last_name(),
        fake.email(),
        fake.text()
    ))
# ========================================================
# To write a code "pg_dump -U postgres -h localhost -p 5432 -F c -f база.psql postgres"
# to create a backup of the database with the help of python
# os.system('pg_dump -U postgres -h localhost -p 5432 -F c -f db.psql postgres')
# ========================================================
rows = cur.fetchall()
for row in rows:
    print(row) 
# ========================================================
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States
 
