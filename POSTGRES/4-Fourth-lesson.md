The DELETE and TRUNCATE commands in PostgreSQL are used to remove rows from a table, but they work in different ways:

1. **DELETE TABLE**: This command removes one or more rows from a table. You can use a **WHERE** clause to specify which rows to delete. If you don't provide a **WHERE** clause, all rows will be deleted. However, the table structure, attributes, and indexes remain intact. **DELETE** operations are transaction-safe and can be rolled back.

```sql
DELETE FROM table_name WHERE condition;

ROLLBACK; -- to rollback the changes
-- By doing ROLLBACK after DELETE, we can restore the deleted rows
```


2. **TRUNCATE TABLE**: This command removes all rows from a table. It is similar to the **DELETE** command without a **WHERE** clause, but it is faster because it doesn't generate individual **DELETE** statements for each row. **TRUNCATE** operations are not transaction-safe and cannot be rolled back.

```sql
TRUNCATE TABLE table_name;
```

3. **DROP TABLE** is used to remove a table from the database. It removes the table structure, attributes, and indexes. The **DROP TABLE** command is not transaction-safe and cannot be rolled back.

```sql
DROP TABLE table_name;
```


4. JOINs in PostgreSQL are used to combine rows from two or more tables based on a related column between them. There are different types of JOINs in PostgreSQL:


-- \x -- to switch to the expanded output mode


- **INNER JOIN**: Returns rows when there is a match in both tables.
-- SYNTAX:
```sql
-- SELECT * FROM table1 JOIN table2 
-- ON table1.column_name = table2.column_name;

SELECT *
FROM customers
JOIN orders ON customers.id = orders.customer_id;
```

- **LEFT JOIN (or LEFT OUTER JOIN)**: 
Returns all rows from the left table and the matched rows from the right table.
- **RIGHT JOIN (or RIGHT OUTER JOIN)**: Returns all rows from the right table and the matched rows from the left table.
```sql
-- Let's consider two tables: Students and Courses.
The Students table:
 ____________
|    |       |
|ID	 | Name  |
|1	 | Alice |
|2	 | Bob   |
|3	 | Carol |
|____|_______|

The Courses table:
 _____________________________
|    |            |           |
|ID	 | CourseName | StudentID |
|1	 | Math	      | 1         |
|2	 | Science	  | 2         |
|3	 | History	  | 3         |
|4	 | Math	      | 2         |
|_____________________________|

-- Now, let's see how LEFT JOIN and RIGHT JOIN work.

`LEFT JOIN`
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.ID = Courses.StudentID;

-- This will return:
____________________
Name	| CourseName
Alice	| Math
Alice	| English
Bob	    | Science
Carol	| NULL
--------------------

`RIGHT JOIN`
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.ID = Courses.StudentID;
____________________
Name	| CourseName
Alice	| Math
Alice	| English
Bob	    | Science
--------------------
```

-->
****
****
INDEXES
```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);

CREATE INDEX users_names_inx
ON users (name) WHERE name LIKE 'Alex%';

By doing this we are telling the database to create an index on the table_name table, and that index will be based on the column1, column2, ... columns.
```

PYTHON + PSQL
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
# cur.execute('''INSERT INTO table_name 
#     VALUES (...)
# ''')  # - to insert data into the table

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
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States
```
 
