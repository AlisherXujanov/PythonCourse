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

<!-- [==================================] -->


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

