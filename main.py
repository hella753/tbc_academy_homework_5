from database import Database
from tasks import Tasks

def main():
    # Initialize the database
    db = Database("books_db")

    # Define table fields
    book_fields = (
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "Name TEXT NOT NULL, "
        "Category TEXT NOT NULL, "
        "Number_of_Pages INTEGER NOT NULL, "
        "Date TEXT NOT NULL, "
        "Author_ID INTEGER NOT NULL "
    )
    authors_field = (
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "First_Name TEXT NOT NULL, "
        "Last_Name TEXT NOT NULL, "
        "DoB TEXT NOT NULL, "
        "Birth_City TEXT NOT NULL "
    )

    # Create tables
    db.create_table("books", book_fields)
    db.create_table("authors", authors_field)

    # Generate and insert fake data
    books_data, authors_data = db.generate_fake_data(1000,500)
    db.insert_data(
        'books',
        "Name, Category, Number_of_Pages, Date, Author_ID",
        books_data
    )
    db.insert_data(
        'authors',
        "First_Name, Last_Name, DoB, Birth_City",
        authors_data
    )

    # Create and execute tasks
    tasks = Tasks(db)

    tasks.get_biggest_book() # Task 1
    tasks.get_avg_page_count() # Task 2
    tasks.get_youngest_authors() # Task 3
    tasks.get_authors_with_no_books() # Task 4
    tasks.bonus() # Bonus Task

    # Close the database connection
    db.close()

if __name__ == "__main__":
    main()

