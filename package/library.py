from faker import Faker
from collections import defaultdict

fake = Faker()

class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category
    def __repr__(self):
        return f'"{self.title}" by {self.author} ({self.category})'

class Shelf:
    def __init__(self, category: str):
        self.category = category
        self.books = []
    def add_book(self, book: Book):
        self.books.append(book)
    def sort_books(self):
        self.books.sort(key=lambda book: book.title)
    def __repr__(self):
        return f'Shelf {self.category}: {self.books}'

class Library:
    def __init__(self):
        self.shelves = defaultdict(Shelf)
    def add_book(self, book: Book):
        if book.category not in self.shelves:
            self.shelves[book.category] = Shelf(book.category)
        self.shelves[book.category].add_book(book)
    def organize_books(self):
        for shelf in self.shelves.values():
            shelf.sort_books()

    def show_books(self):
        for shelf in self.shelves.values():
            print(shelf)

library = Library()
categories = ["Fiction", "Drama", "Horror", "Novel"]
books = [Book(fake.sentence(nb_words=3), fake.name(), fake.random.choice(categories)) for _ in range(10)]
for book in books:
    library.add_book(book)
library.organize_books()
library.show_books()
