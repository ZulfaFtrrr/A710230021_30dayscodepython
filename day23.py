import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        if not self.books:
            return "The library is empty."
        else:
            return "\n".join(book.get_book_info() for book in self.books)


class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.library = Library()

    def initUI(self):
        self.setWindowTitle("Library Application")

        self.layout = QVBoxLayout()

        # Input fields for book information
        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()

        self.author_label = QLabel("Author:")
        self.author_input = QLineEdit()

        self.year_label = QLabel("Year:")
        self.year_input = QLineEdit()

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.author_label)
        self.layout.addWidget(self.author_input)
        self.layout.addWidget(self.year_label)
        self.layout.addWidget(self.year_input)

        # Buttons
        self.add_button = QPushButton("Add Book")
        self.display_button = QPushButton("Display Books")
        self.remove_button = QPushButton("Remove Book")
        self.remove_input = QLineEdit()
        self.result_area = QTextEdit()

        self.add_button.clicked.connect(self.add_book)
        self.display_button.clicked.connect(self.display_books)
        self.remove_button.clicked.connect(self.remove_book)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.display_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.remove_input)
        self.layout.addWidget(self.result_area)

        self.setLayout(self.layout)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        year = self.year_input.text()

        if title and author and year:
            book = Book(title, author, int(year))
            self.library.add_book(book)
            self.result_area.setText(f"Added book: {book.get_book_info()}")
        else:
            self.result_area.setText("Please fill in all fields.")

    def display_books(self):
        books = self.library.list_books()
        self.result_area.setText(books)

    def remove_book(self):
        title = self.remove_input.text()
        if self.library.remove_book(title):
            self.result_area.setText(f"Removed book: {title}")
        else:
            self.result_area.setText(f"Book with title '{title}' not found in the library.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LibraryApp()
    ex.show()
    sys.exit(app.exec_())
