class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class LibraryBookDelegate:
    def __init__(self, library_book):
        self.library_book = library_book

    def check_out(self):
        return self.library_book.check_out()

    def return_book(self):
        return self.library_book.return_book()

    def get_info(self):
        return {
            "title": self.library_book.title,
            "author": self.library_book.author,
            "publication_year": self.library_book.publication_year,
            "is_checked_out": self.library_book.is_checked_out
        }

    def is_available(self):
        return not self.library_book.is_checked_out

    def check_condition(self):
        # Припустимо, що стан книги завжди "добрий", можна додати більше логіки
        return "Good"

# Використання коду
library_book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book_delegate = LibraryBookDelegate(library_book)

print(book_delegate.check_out())  # True
print(book_delegate.check_out())  # False
print(book_delegate.return_book())  # True
print(book_delegate.get_info())  # Інформація про книгу
print(book_delegate.is_available())  # True
print(book_delegate.check_condition())  # Good
