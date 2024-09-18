# DB SQL OPERATIONS

## Description
SQLite3 books database with fake random data. database
consists of two tables for '**books**' with 1000 records and '**authors**' with 500 records.

### **'books' table fields.**

| id | Name   | Category   | Number_of_Pages | Date   | Author_ID |
|----|--------|------------|-----------------|--------|-----------|
| 1  | _name_ | _category_ |  _num of pages_ | _date_ | _id_num_  |

**'books'** table **primary key** is **'id'** and it has an autoincrement constraint.

### **'authors' table fields.**
| id | First_Name   | Last_Name   | DoB    | Birth_City |
|----|--------------|-------------|--------|------------|
| 1  | _first name_ | _last name_ | _date_ | _city_     |

**'authors'** table **primary key** is **'id'** and it has an autoincrement constraint.

## Components
* **Database**: Handles the sqlite3 database operations like creating tables and inserting data. 
* **DataGenerator**: Uses Faker class and different providers from faker library. 
Is responsible for generating random data.
* **Tasks**: Fetches the records from the database tables according to tasks provided.

### Provided Tasks
* Find and print all fields of the book with maximum number of pages
* Find and print the average of the number of pages
* Print the youngest author
* Print the authors who have not written any books yet
* Find 5 authors with more than 3 books (Bonus Task)

## Dependencies
* **Faker**: external library for generating random data using different providers: BaseProvider, lorem, date_time, person.

#### Python Standard Library modules used:
* **sqlite3**: DB-API 2.0 interface for SQLite databases.
* **random**: Generate pseudo-random numbers.
* **datetime**: Basic date and time types.
