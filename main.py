"""
LBR MG - Library Management System
Author: Arsh
Description: CLI-based Library Management System using SQLite.
"""

import sqlite3


AVAILABLE = 0
ISSUED = 1


class Book:
    def __init__(self, book_title: str, book_author: str, is_issued=False):
        self.book_title = book_title.strip()
        self.book_author = book_author.strip()
        self.is_issued = is_issued


class Library:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS BOOKS (
                BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                BOOK_TITLE TEXT NOT NULL,
                BOOK_AUTHOR TEXT NOT NULL,
                STATUS INTEGER NOT NULL
            )
            """)

    def add_book(self, book: Book):
        if not book.book_title or not book.book_author:
            print("Title and Author cannot be empty.")
            return

        with self.conn:
            self.conn.execute(
                "INSERT INTO BOOKS (BOOK_TITLE, BOOK_AUTHOR, STATUS) VALUES (?, ?, ?)",
                (book.book_title, book.book_author, AVAILABLE)
            )
        print(f"'{book.book_title}' added successfully!")

    def show_all_records(self):
        with self.conn:
            data = self.conn.execute("SELECT * FROM BOOKS").fetchall()

        if not data:
            print("No books available in the library.")
            return

        for row in data:
            status = "Issued" if row[3] == ISSUED else "Available"
            print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | Status: {status}")

    def issue_book(self, title: str):
        title = title.strip()
        if not title:
            print("Book title cannot be empty.")
            return

        with self.conn:
            book = self.conn.execute(
                "SELECT STATUS FROM BOOKS WHERE LOWER(BOOK_TITLE) = LOWER(?)",
                (title,)
            ).fetchone()

            if not book:
                print("Book not found.")
                return

            if book[0] == ISSUED:
                print("Book already issued.")
                return

            self.conn.execute(
                "UPDATE BOOKS SET STATUS = 1 WHERE LOWER(BOOK_TITLE) = LOWER(?)",
                (title,)
            )

        print("Book issued successfully.")

    def return_book(self, title: str):
        title = title.strip()
        if not title:
            print("Book title cannot be empty.")
            return

        with self.conn:
            book = self.conn.execute(
                "SELECT STATUS FROM BOOKS WHERE LOWER(BOOK_TITLE) = LOWER(?)",
                (title,)
            ).fetchone()

            if not book:
                print("Book not found.")
                return

            if book[0] == AVAILABLE:
                print("Book is already available.")
                return

            self.conn.execute(
                "UPDATE BOOKS SET STATUS = 0 WHERE LOWER(BOOK_TITLE) = LOWER(?)",
                (title,)
            )

        print("Book returned successfully.")

    def search_book(self, title: str):
        title = title.strip()
        if not title:
            print("Search cannot be empty.")
            return

        with self.conn:
            data = self.conn.execute(
                "SELECT * FROM BOOKS WHERE LOWER(BOOK_TITLE) LIKE LOWER(?)",
                (f"%{title}%",)
            ).fetchall()

        if not data:
            print("No record found.")
            return

        for book in data:
            status = "Issued" if book[3] == ISSUED else "Available"
            print(f"Title: {book[1]} | Author: {book[2]} | Status: {status}")
    
    def show_stats(self):
        """ This show statistics of books. """
        with self.conn:
            total = self.conn.execute("SELECT COUNT(*) FROM BOOKS").fetchone()[0]
            issued = self.conn.execute("SELECT COUNT(*) FROM BOOKS WHERE STATUS = 1").fetchone()[0]
            available = total - issued

        print("\nLibrary Statistics")
        print(f"Total Books: {total}")
        print(f"Issued Books: {issued}")
        print(f"Available Book: {available}")

    def close_connection(self):
        self.conn.close()


def menu():
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Show all books")
    print("2. Add book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Search book")
    print("6. Statistics")
    print("7. Exit")


def get_int_choice():
    while True:
        try:
            return int(input("Enter choice (1-7): ").strip())
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    library = Library()

    try:
        while True:
            menu()
            choice = get_int_choice()

            if choice == 1:
                library.show_all_records()

            elif choice == 2:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                library.add_book(Book(title, author))

            elif choice == 3:
                title = input("Enter book title to issue: ")
                library.issue_book(title)

            elif choice == 4:
                title = input("Enter book title to return: ")
                library.return_book(title)

            elif choice == 5:
                title = input("Enter book title to search: ")
                library.search_book(title)

            elif choice == 6:
                library.show_stats()
            elif choice == 7:
                print("Thanks for using LBR MG!")
                break

            else:
                print("Invalid option. Choose 1-6.")

    finally:
        library.close_connection()
