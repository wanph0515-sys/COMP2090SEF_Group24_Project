[Task 1-REANME.md](https://github.com/user-attachments/files/25813434/Task.1-REANME.md)

# Task 1 - Library Management System

## Project Overview
This Task implements a lightweight Library Management System using Python, which core functions include book/user management, book borrowing/returning, keyword-based book search, and complete legality verification with error prompt mechanisms for basic library business logic.

#### Author: WAN Peiheng, TAN Guangxi

## Core Code Structure
### 1. Core Class Definitions
#### Book Class
```python
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id  # Unique book ID
        self.title = title      # Book title
        self.author = author    # Book author
        self.is_borrowed = False  # Borrow status, default to available

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}"
```

#### User Class
```python
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id  # Unique user ID
        self.name = name        # User name
        self.borrowed_books = []  # List of borrowed books

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            return True, f"Success! '{book.title}' has been lent to {self.name}"
        return False, f"Failed: Book is already borrowed"

    def return_book(self, book):
        if book.is_borrowed and book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return True, f"Success! '{book.title}' has been returned"
        return False, f"Failed: Book is not borrowed"

    def __str__(self):
        return f"User ID: {self.user_id} | Name: {self.name} | Number of borrowed books: {len(self.borrowed_books)}"
```

#### Library Class
```python
class Library:
    def __init__(self):
        self.books = {}  # Book dictionary: key=book_id, value=Book object
        self.users = {}  # User dictionary: key=user_id, value=User object

    def add_book(self, book):
        if book.book_id in self.books:
            return False, "Error: Book ID already exists"
        self.books[book.book_id] = book
        return True, "Book added successfully"

    def register_user(self, user):
        if user.user_id in self.users:
            return False, "Error: User ID already exists"
        self.users[user_id] = user
        return True, "User registered successfully"

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            return False, "Error: User not found"
        if book_id not in self.books:
            return False, "Error: Book not found"
        return self.users[user_id].borrow_book(self.books[book_id])

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            return False, "Error: User not found"
        if book_id not in self.books:
            return False, "Error: Book not found"
        return self.users[user_id].return_book(self.books[book_id])

    def search_book(self, keyword):
        results = []
        keyword = keyword.lower()
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        return results
```

### 2. Initialization Main Function
```python
def main():
    # Initialize library
    library = Library()
    
    # Add sample books
    book1 = Book("B001", "Python Crash Course", "Eric Matthes")
    book2 = Book("B002", "Data Structures and Algorithms in Python", "Michael T. Goodrich")
    library.add_book(book1)
    library.add_book(book2)
    
    # Register sample users
    user1 = User("U001", "Xiaoming")
    user2 = User("U002", "Xiaohong")
    library.register_user(user1)
    library.register_user(user2)
    
    return library

# Execute initialization
if __name__ == "__main__":
    lib = main()
    print("Library Management System initialized successfully!")
```

## Running Instructions
1. Save the above code as `Task1.py`;
2. Open terminal/command line, navigate to the directory where the code is saved, and execute the command:
```bash
python Task1.py
```
3. The system will automatically initialize sample data and return a library instance for subsequent interaction.

   (The Task1.py here is only preliminary code and cannot run normally. It is provided for reference only.)

## Basic Usage Examples
```python
lib = main()

# Example 1: Borrow a book
borrow_result, borrow_msg = lib.borrow_book("U001", "B001")
print(borrow_msg)  # Output: Success! 'Python Crash Course' has been lent to Xiaoming

# Example 2: Return a book
return_result, return_msg = lib.return_book("U001", "B001")
print(return_msg)  # Output: Success! 'Python Crash Course' has been returned

# Example 3: Search for books
search_results = lib.search_book("python")
for book in search_results:
    print(book)  # Output information of all books with "python" in title/author
```

## Error Handling Explanation
The system implements complete legality verification for core operations, with common error prompts as follows:

| Operation Scenario | Error Prompt | Reason |
|--------------------|--------------|--------|
| Adding book with duplicate ID | Error: Book ID already exists | The book ID is already registered in the system |
| Registering user with duplicate ID | Error: User ID already exists | The user ID is already registered in the system |
| Borrowing/Returning for non-existent user | Error: User not found | The user ID is not registered |
| Borrowing/Returning non-existent book | Error: Book not found | The book ID is not added to the system |
| Borrowing an already borrowed book | Failed: Book is already borrowed | The book status is "Borrowed" |
| Returning an unborrowed book | Failed: Book is not borrowed | The book status is "Available" |

## Functional Highlights
- Adopts object-oriented design, encapsulating three core entities (Book, User, Library) with clear logic;
- All operations return "execution result + prompt message" for easy debugging and user interaction;
- The search function supports fuzzy keyword matching and is case-insensitive to improve user experience;
- Complete boundary verification to avoid program exceptions caused by illegal operations.

