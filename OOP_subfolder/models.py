from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str):
        self._item_id = item_id      
        self._title = title
        self._is_borrowed = False

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, status: bool):
        self._is_borrowed = status

    @abstractmethod
    def get_item_type(self) -> str:
        pass

    def __str__(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"[{self._item_id}] {self._title} ({self.get_item_type()}) - {status}"


class Book(LibraryItem):
    def __init__(self, book_id: str, title: str, author: str):
        super().__init__(book_id, title)
        self._author = author

    @property
    def author(self):
        return self._author

    def get_item_type(self) -> str:
        return "Book"

    def __str__(self):
        return f"[{self.item_id}] {self.title} by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"


class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name
        self._borrowed_items = []

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def borrowed_items(self):
        return self._borrowed_items.copy()

    def borrow_item(self, item: LibraryItem):
        if item not in self._borrowed_items and not item.is_borrowed:
            self._borrowed_items.append(item)
            item.is_borrowed = True
            return True
        return False

    def return_item(self, item: LibraryItem):
        if item in self._borrowed_items:
            self._borrowed_items.remove(item)
            item.is_borrowed = False
            return True
        return False

    def __str__(self):
        return f"User: {self._name} (ID: {self._user_id}), Borrowed: {len(self._borrowed_items)} items"


class StaffUser(User):
    def __init__(self, user_id: str, name: str, department: str):
        super().__init__(user_id, name)
        self._department = department

    @property
    def department(self):
        return self._department

    def borrow_item(self, item: LibraryItem) -> bool:
        print(f"[Staff] {self.name} is borrowing an item.")
        return super().borrow_item(item)

    def __str__(self):
        return f"Staff: {self.name} (ID: {self.user_id}, Dept: {self._department}), Borrowed: {len(self.borrowed_items)} items"
