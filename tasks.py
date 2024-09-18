from database import Database


class Tasks:
    def __init__(self, db: Database):
        """
        Initialize the Tasks class.

        :param db: The database object used to interact with the database.
        """
        self.db = db

    def get_biggest_book(self) -> None:
        """
        Get the book with the max number of pages.

        Fetches the row where the "Number_of_Pages" is the largest
        and prints the information about the biggest book.
        """
        condition = (
            "WHERE Number_of_Pages = "
            "(SELECT MAX(Number_of_Pages) FROM books)"
        )
        biggest_book = self.db.fetch_data(
            "books",
            condition=condition
        )
        print(biggest_book, "\n")

    def get_avg_page_count(self) -> None:
        """
        Get the average number of pages.

        Calculates the average of the "Number_of_Pages"
        and prints the average page count.
        """
        average_page_count = self.db.fetch_data(
            "books",
            selected="AVG(Number_of_Pages)"
        )
        print(average_page_count[0][0], "\n")

    def get_youngest_authors(self) -> None:
        """
        Get the youngest authors from the "authors" table

        This method finds the authors with the earliest DoB and
        prints the authors names.
        """
        condition = (
            "WHERE DoB = "
            "(SELECT MAX(DoB) FROM authors)"
        )
        youngest_authors = self.db.fetch_data(
            "authors",
            selected="First_Name, Last_Name",
            condition=condition
        )
        for author in youngest_authors:
            first_name, last_name = author
            print(first_name, last_name)
        print()

    def get_authors_with_no_books(self) -> None:
        """
        Get the authors with no books.

        Checks for authors whose ID is not present in the "books" table,
        which means that they have not published any books yet. Print the name
        and the ID of the authors.
        """
        condition = (
            "WHERE id not in "
            "(SELECT Author_ID FROM books)"
        )
        authors_with_no_books = self.db.fetch_data(
            "authors",
            selected="id, First_Name, Last_Name",
            condition=condition
        )
        for author in authors_with_no_books:
            auth_id, first_name, last_name = author
            print(auth_id, first_name, last_name)
        print()

    def bonus(self) -> None:
        """
        Get authors who have written more than three books.

        Finds authors who have more than three books listed in the "books" table
        prints the names and the id of the authors.
        """
        condition = (
            "WHERE id IN "
            "(SELECT Author_ID FROM books "
            "GROUP BY Author_ID HAVING COUNT(*)>3)"
        )
        authors_with_more_than_three_books = self.db.fetch_data(
            "authors",
            selected="First_Name, Last_Name, id",
            condition=condition,
            limit="LIMIT 5"
        )

        for author in authors_with_more_than_three_books:
            first_name, last_name, auth_id = author
            print(first_name, last_name, auth_id)
        print()
