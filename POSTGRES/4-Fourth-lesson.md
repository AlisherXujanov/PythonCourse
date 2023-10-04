PostgreSQL Indexes

<!-- 
Indexes are special lookup tables that the database search engine can use to speed up data retrieval. Simply put, an index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.

When you look up a keyword in the back of a book, you then have a list of page numbers where that keyword is mentioned in the book. Without the index, the database would have to search every row of every table in the database to find the relevant data. If the table has an index for the columns in question, the database can quickly determine the position to seek to in the middle of the data file without having to look at all the data. If a table has 1,000 rows, this process will be 1,000 times faster than if the database engine did not use an index. 
-->
****
****
PYTHON + PSQL
```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);

CREATE INDEX users_names_inx
ON users (name) WHERE name IS 'Alex%';

By doing this we are telling the database to create an index on the table_name table, and that index will be based on the column1, column2, ... columns.
```

```python
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
def save_db_at_this_point():
    os.system('pg_dump -U postgres -h localhost -p 5432 -F c -f db.psql postgres')
# ========================================================
# To print the table in the terminal
cur.execute('''SELECT * FROM users;''')
rows = cur.fetchone()

if rows:
    print(rows)
else:
    print("No rows returned.")
# ========================================================
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States
```
 
