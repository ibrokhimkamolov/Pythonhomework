class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROWED_BOOKS = 3
    
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {Member.MAX_BORROWED_BOOKS} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        self.books[book.title] = book
    
    def add_member(self, member):
        self.members[member.name] = member
    
    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if member_name not in self.members:
            print(f"Member '{member_name}' not registered in the library.")
            return
        
        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)
    
    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not registered in the library.")
            return
        if book_title not in self.books:
            print(f"Book '{book_title}' not found in the library.")
            return
        
        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)

# Testing the library system
if __name__ == "__main__":
    library = Library()
    
    # Adding books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Moby Dick", "Herman Melville")
    book4 = Book("Pride and Prejudice", "Jane Austen")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    # Adding members
    member1 = Member("Alice")
    member2 = Member("Bob")
    
    library.add_member(member1)
    library.add_member(member2)
    
    # Borrowing books
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Moby Dick")
    
    # Exceeding borrow limit
    try:
        library.borrow_book("Alice", "Pride and Prejudice")
    except MemberLimitExceededException as e:
        print(e)
    
    # Borrowing an already borrowed book
    try:
        library.borrow_book("Bob", "1984")
    except BookAlreadyBorrowedException as e:
        print(e)
    
    # Returning a book
    library.return_book("Alice", "1984")
    
    # Trying to borrow a non-existent book
    try:
        library.borrow_book("Bob", "The Great Gatsby")
    except BookNotFoundException as e:
        print(e)