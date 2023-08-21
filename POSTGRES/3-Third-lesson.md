3. Syntax items - Continue of the second lesson


```sql
CREATE TABLE Customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE Orders (
  id SERIAL PRIMARY KEY,
  order_date DATE NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  customer_id INTEGER NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES Customers (id)
);

INSERT INTO Orders (order_date, total, customer_id)
VALUES ('2022-01-01', 100.00, 1);
```

<!-- [==============================================================================] -->
<!-- [==============================================================================] -->


```sql
-- Let's say we have two tables: Students and Courses. 
-- Each student can enroll in multiple courses, so we want to create a 
-- relationship between the two tables using the FOREIGN KEY constraint.

CREATE TABLE Students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE Courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  instructor VARCHAR(255) NOT NULL
);

CREATE TABLE Enrollments (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Students (id),
  FOREIGN KEY (course_id) REFERENCES Courses (id)
);

INSERT INTO Enrollments (student_id, course_id)
VALUES (1, 1);


-- This means that the student with an id of 1 is enrolled in the course with an id of 1
```

<!-- [==============================================================================] -->
<!-- [==============================================================================] -->

**SUBSTRING()** - Extracts a substring from a string
```sql
SYNTAX:  SELECT SUBSTRING(column_name, start_position, length) FROM table_name;

SELECT SUBSTRING(first_name, 1, 3) AS 'First Name' FROM customers;
This will return the first 3 characters of the first name column
So if: first_name = 'John'
The result will be: 'Joh'
```
<!-- -------------------------------------------------------------------------------- -->
**MAX()** - Returns the maximum value in a set of values
```sql
SELECT MAX(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**MIN()** - Returns the minimum value in a set of values
```sql
SELECT MIN(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**AVG()** - Returns the average value in a set of values
```sql
SELECT AVG(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**SUM()** - Returns the sum of all or distinct values in a set of values
```sql
SELECT SUM(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**COUNT()** - Returns the number of rows that matches a specified criteria
**COUNT(DISTINCT)** - Returns the number of distinct rows that matches a specified criteria
```sql
SELECT COUNT(*) FROM products;
SELECT COUNT(DISTINCT price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**ROUND()** - Rounds a number to a specified number of decimal places
```sql
SYNTAX:  SELECT ROUND(column_name, number_of_decimal_places) FROM table_name;

-- SELECT ROUND(price, 2) FROM products;
-- This will return the price column rounded to 2 decimal places
-- ex:
--    price = 10.1234
--    result = 10.12
```
<!-- -------------------------------------------------------------------------------- -->
**FORMAT()** - Formats how a field is to be displayed
```sql
SYNTAX:  SELECT FORMAT(column_name, 'C', 'en-US') FROM table_name;
-- 1st parameter: column_name
-- 2nd parameter: 'C' - Currency
-- 3rd parameter: 'en-US' - English (United States)
-- As default the format() function will return the value with 2 decimal places
-- We need format for example the price column to be displayed as a currency
-- ex:
--     price = 10.1234
--     result = $10.12
```
<!-- -------------------------------------------------------------------------------- -->
**CONCAT()** - Adds two or more expressions together
```sql
SELECT CONCAT(first_name, ' ', last_name) AS 'Full Name' FROM customers;
```
<!-- -------------------------------------------------------------------------------- -->


<!-- [==============================================================================] -->
<!-- [==============================================================================] -->

*Merging two or more columns*
```sql
-- Let's say we have a table with the following data:
________________________________
-- id | name  | email
-- 1  | John  | John@test.com
-- 2  | Mary  | Mary@test.com
-- 3  | Peter | Peter@test.com
________________________________
-- We want to add a new column called 'full_name' and populate it with the first name and last name
-- We can do this using the CONCAT() function

ALTER TABLE customers ADD COLUMN full_name VARCHAR(255);

UPDATE customers SET full_name = CONCAT(first_name, ' ', last_name);

-- We can also use the CONCAT() function to add a new column and populate it with the first name and last name

ALTER TABLE customers ADD COLUMN full_name VARCHAR(255) AS (CONCAT(first_name, ' ', last_name));

```




