import datetime
import random
from typing import List, Tuple
from faker import Faker
from faker.providers import BaseProvider, date_time, person, lorem

# List of book genres that will be used for random category.
GENRES = [
    "Fantasy", "Science Fiction", "Dystopian", "Action & Adventure", "Mystery",
    "Horror", "Thriller & Suspense", "Historical Fiction", "Romance",
    "Graphic Novel", "Children’s", "Biography", "Self-help", "History",
    "True Crime", "Essays"
]


class DataGenerator(Faker):
    """
    DataGenerator class that inherits from the Faker class.
    """

    def __init__(self):
        """
        Constructor for DataGenerator.

        Initializes the Faker class and adds providers for generating
        different types of data: date_time, lorem and person.
        initializes two lists to store data.
        """
        super().__init__()
        self.add_provider(lorem)
        self.add_provider(date_time)
        self.add_provider(BaseProvider)
        self.add_provider(person)
        self._authors_data_list = []
        self._books_data_list = []

    def generate_authors(self, num: int) -> List[Tuple]:
        """
        Generates author data randomly

        :param num: Number of authors to generate
        :return: authors_data_list: List containing author data.
        """
        for _ in range(num):
            first_name = self.first_name()
            last_name = self.last_name()
            dob = self.date_between(
                datetime.date(1960, 1, 1),
                datetime.date(1999, 12, 31)
            )
            city = self.city()
            self._authors_data_list.append((first_name, last_name, dob, city))
        return self._authors_data_list

    def generate_books(self, num: int, authors_range: int) -> List[Tuple]:
        """
        Generates book data randomly

        :param num: Number of books to generate
        :param authors_range: Number of authors to select an author_id from
        :return: books_data_list: List of tuples containing book data.
        """
        for _ in range(num):
            random_digit = self.random_int(min=15, max=1000)
            date = self.date_this_century()
            text = self.text(max_nb_chars=20).rstrip('.')  # Removing '.'
            category = random.choice(GENRES)
            author_id = random.randint(1, authors_range)
            self._books_data_list.append((
                text,
                category,
                random_digit,
                date,
                author_id
            ))
        return self._books_data_list
