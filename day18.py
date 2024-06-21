class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"

# Membuat objek Book
book1 = Book("Dia", "Zulfa Fitri", 2024)
print(book1.get_book_info())

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book.get_book_info())

# Membuat objek Library
library = Library()

# Menambahkan buku ke perpustakaan
library.add_book(book1)
library.add_book(Book("Dia Angkasa", "Nuri Kasanah", 2020))

# Menampilkan daftar buku
library.list_books()

# Menghapus buku dari perpustakaan
library.remove_book(book1)

# Menampilkan daftar buku setelah penghapusan
library.list_books()
