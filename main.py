import os
import sqlite3

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute(
        '''
        CREATE TABLE students
        (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  VARCHAR NOT NULL,
            age   INTEGER,
            email VARCHAR UNIQUE,
            city  VARCHAR
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE courses
        (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name VARCHAR NOT NULL,
            instructor  text,
            credits     INTEGER
        )
        '''
    )

def insert_sample_data(cursor):
    # region Add Students to Database
    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", students)
    # endregion
    # region Add Courses to Database
    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]
    cursor.executemany("INSERT INTO courses VALUES (?, ?, ?, ?)", courses)
    # endregion
    print("Sample data inserted")

def basic_sql_operations(cursor):
    # region SELECT ALL Students
    print("-------------SELECT ALL-------------")
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")
    # endregion
    # region SELECT Columns
    print("-------------SELECT COLUMNS--------------")
    cursor.execute("SELECT name,age FROM students")
    records = cursor.fetchall()
    print(records)
    # endregion
    # region WHERE CLAUSE
    print("-------------WHERE CLAUSE AGE = 20--------------")
    cursor.execute("SELECT * FROM students WHERE age = 20")
    records = cursor.fetchall()
    print(records)
    # endregion

def sql_crud_operations(conn, cursor):
    # region INSERT
    cursor.execute("INSERT INTO students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()
    # endregion
    # region UPDATE
    cursor.execute("UPDATE students SET age = 24 WHERE id = 6")
    conn.commit()
    # endregion
    # region DELETE
    cursor.execute("DELETE FROM students WHERE id = 6")
    conn.commit()
    # endregion

def questions():
    '''
    Basic
    1) Retrieve all course information.
    2) Retrieve only the instructors’ names and the course names.
    3) Retrieve only the students who are 21 years old.
    4) Retrieve only the students who live in Chicago.
    5) Retrieve only the courses taught by ‘Dr. Anderson’.
    6) Retrieve only the students whose names start with ‘A’.
    7) Retrieve only the courses with 3 or more credits.

    Advanced
    1) Retrieve all students sorted alphabetically by name.
    2) Retrieve students older than 20, sorted by their names.
    3) Retrieve only the students who live in either ‘New York’ or ‘Chicago’.
    4) Retrieve only the students who do not live in ‘New York’.
    '''

def answers(cursor):
    # region Answer 1
    cursor.execute("SELECT * FROM courses")
    cursor.fetchall()
    # endregion
    # region Answer 2
    cursor.execute("SELECT course_name, instructor FROM courses")
    cursor.fetchall()
    # endregion
    # region Answer 3
    cursor.execute("SELECT * FROM students WHERE age = 21")
    cursor.fetchall()
    # endregion
    # region Answer 4
    cursor.execute("SELECT * FROM students WHERE city = 'Chicago'")
    cursor.fetchall()
    # endregion
    # region Answer 5
    cursor.execute("SELECT * FROM courses WHERE instructor = 'Dr. Anderson'")
    cursor.fetchall()
    # endregion
    # region Answer 6
    cursor.execute("SELECT * FROM courses WHERE name LIKE 'A%'")
    cursor.fetchall()
    # endregion
    # region Answer 7
    cursor.execute("SELECT * FROM courses WHERE credits>=3")
    cursor.fetchall()
    # endregion
    # region Answer 1
    cursor.execute("SELECT * FROM students ORDER BY name")
    cursor.fetchall()
    # endregion
    # region Answer 2
    cursor.execute("SELECT * FROM students WHERE age >20 ORDER BY name")
    cursor.fetchall()
    # endregion
    # region Answer 3
    cursor.execute("SELECT name, city FROM students WHERE city IN ('New York', 'Chicago')")
    cursor.fetchall()
    # endregion
    # region Answer 4
    cursor.execute("SELECT name, city FROM students WHERE city != 'New York'")
    cursor.fetchall()
    # endregion

def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_crud_operations(conn, cursor)
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
