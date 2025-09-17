class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

class Borrower: # Gathers the book borrowers ID and name of the borrower
    def __init__(self, borrower_id, name): 
        self.borrower_id = borrower_id # Creates new variables for borrower class: borrower_id and namew
        self.name = name

class Loan: # Gathers the which book is being loaned and who the borrower is 
    def __init__(self, book, borrower):
        self.book = book # Loan creates new variables for book and its borrower
        self.borrower = borrower

class BookManager: # Gathers all the books and puts it into a dictionary data structure
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author): # Adds new book entry into the library
        if book_id in self.books: # If statement rejects any book that is already present in the library
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author)

    def remove_book(self, book_id): # Removes book from the library 
        if book_id in self.books: # If statement will only deletes book from library if present, if not there is no removal
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

    def search_book(self, book_id): # Searches all books within the library and returns book and book ID
        return self.books.get(book_id, None)

class BorrowerManager: # Class gathers all info on who is borrowing a book and what they borrowed
    def __init__(self):
        self.borrowers = {} # Gathers all borrowers into a data structure

    def add_borrower(self, borrower_id, name): # Adds borrower entry into dictionary of borrowers
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.") # Rejects reoccurring borrower entries
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

    def remove_borrower(self, borrower_id): # Removes borrower data in dictionary of borrowers
        if borrower_id in self.borrowers: # If statement which removes borrower, if not it will raise an error
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.")

    def search_borrower(self, borrower_id): # Allows user to search for borrower
        return self.borrowers.get(borrower_id, None)

class LoanManager: 
    def __init__(self):
        self.loans = [] # New class that sorts loans into a list

    def create_loan(self, book, borrower): 
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        loan = Loan(book, borrower) # Creates loan variable which includes what book and its borrower
        self.loans.append(loan) # Adds newly create loan into list
        book.is_loaned = True # Provide book loan status, cannot be loaned unless status is False

    def return_loan(self, book):
        for loan in self.loans:
            if loan.book.book_id == book.book_id: 
                self.loans.remove(loan) # Removes the loan from list and changes the loan status back to false
                book.is_loaned = False 
                break
    
    class LibraryFacade: # Class that uses all previous classes to make methods easier 
        def __init__(self):
            self.book_manager = BookManager()
            self.borrower_manager = BorrowerManager()
            self.loan_manager = LoanManager()

        def add_book(self, book_id, title, author): # Method which adds a book entry and its data into the library including its name, author and book_id
            self.book_manager.add_book(book_id, title, author)

        def remove_book(self, book_id): # Methods that removes the book_id from the library
            self.book_manager.remove_book(book_id)

        def search_book(self, book_id):
            return self.book_manager.search_book(book_id) # Searches for a books ID using book manager class and returns the searched book

        def add_borrower(self, borrower_id, name):
            self.borrower_manager.add_borrower(borrower_id, name) # By using the borrower_manager class, adds borrower entry to dictionary of borrowers

        def remove_borrower(self, borrower_id):
            self.borrower_manager.remove_borrower(borrower_id) # Removes borrower data by using the borrow_manager class

        def search_borrower(self, borrower_id):
            return self.borrower_manager.search_borrower(borrower_id) # Searches for borrower_id by using the borrower_manager class, returns borrower_id

        def create_loan(self, book_id, borrower_id): # Using the book_manager, borrower_manager and loan_manager class, gathers all books data together to form a loan
            book = self.book_manager.search_book(book_id) # Creates new variables for book's ID and its borrower
            borrower = self.borrower_manager.search_borrower(borrower_id)
            if book and borrower:
                self.loan_manager.create_loan(book, borrower) # Using loan_manager class to create a loan using the book and its borrower
            else:
                raise ValueError("Book or Borrower not found.")

        def return_loan(self, book_id): # Searches for returning books ID and returns it, if not found it raises an error
            book = self.book_manager.search_book(book_id)
            if book:
                self.loan_manager.return_loan(book)
            else:
                raise ValueError("Book not found.")

if __name__ == "__main__":
    library = LibraryFacade

    # Adding books
    library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(2, "1984", "George Orwell")

    # Adding borrowers
    library.add_borrower(1, "Alice")
    library.add_borrower(2, "Bob")

    # Creating a loan
    library.create_loan(1, 1)  # Alice borrows "The Great Gatsby"

    # Searching for a book
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")

    # Returning a loan
    library.return_loan(1)

    # Checking the book status again
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")