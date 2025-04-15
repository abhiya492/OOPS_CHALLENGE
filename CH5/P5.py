class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.__isbn}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.__member_id = member_id
        self.borrowed_books = []
    
    def get_member_id(self):
        return self.__member_id
    
    def set_member_id(self, member_id):
        self.__member_id = member_id
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
    
    def __str__(self):
        return f"Member: {self.name}, ID: {self.__member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}"


class Librarian(Member):
    def __init__(self, name, member_id, employee_id):
        super().__init__(name, member_id)
        self.employee_id = employee_id
    
    def add_book(self, book, library):
        library.books.append(book)
    
    def remove_book(self, book, library):
        library.books.remove(book)
    
    def __str__(self):
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}, Member ID: {self.get_member_id()}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_member(self, member):
        self.members.append(member)
    
    def remove_member(self, member):
        self.members.remove(member)
    
    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"


# Example usage
library = Library()
librarian = Librarian("Alice", "M001", "E001")
member = Member("Bob", "M002")

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

librarian.add_book(book1, library)
librarian.add_book(book2, library)

library.add_member(librarian)
library.add_member(member)

member.borrow_book(book1)

print(library)
print(librarian)
print(member)
