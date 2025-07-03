class Book  :

    def __init__(self, title , author) :
        self.title = title
        self.author = author

        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False
    
    def is_avilable (self):
        return not self._is_checked_out
    

class Library :

    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

        def check_out_book(self, title):
       
             for book in self._books:
                if book.title == title and book.is_available():
                    book.check_out()
                    break  # Only one match needed

    def return_book(self, title):
        """
        Mark a book as returned if it exists in the library.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                break

    def list_available_books(self):
        """
        Print all books that are currently available.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

        