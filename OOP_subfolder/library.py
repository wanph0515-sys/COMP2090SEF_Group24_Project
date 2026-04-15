from models import Book, User, StaffUser

class Library:
    def __init__(self):
        self._items = {}
        self._users = {}

    def add_item(self, item):
        if item.item_id in self._items:
            return False, f"Item ID {item.item_id} already exists."
        self._items[item.item_id] = item
        return True, f"Item '{item.title}' added successfully."

    def register_user(self, user):
        if user.user_id in self._users:
            return False, f"User ID {user.user_id} already exists."
        self._users[user.user_id] = user
        return True, f"User '{user.name}' registered successfully."

    def borrow_item(self, user_id, item_id):
        if user_id not in self._users:
            return False, "User not found."
        if item_id not in self._items:
            return False, "Item not found."

        user = self._users[user_id]
        item = self._items[item_id]

        if item.is_borrowed:
            return False, f"Item '{item.title}' is already borrowed."

        if user.borrow_item(item):
            return True, f"Success! '{item.title}' borrowed by {user.name}."
        else:
            return False, "Borrow failed (unknown reason)."

    def return_item(self, user_id, item_id):
        if user_id not in self._users:
            return False, "User not found."
        if item_id not in self._items:
            return False, "Item not found."

        user = self._users[user_id]
        item = self._items[item_id]

        if not item.is_borrowed:
            return False, f"Item '{item.title}' is not borrowed."

        if user.return_item(item):
            return True, f"Success! '{item.title}' returned by {user.name}."
        else:
            return False, "Return failed (item not in user's borrowed list)."

    def search_items(self, keyword):
        results = []
        keyword_lower = keyword.lower()
        for item in self._items.values():
            if keyword_lower in item.title.lower():
                results.append(item)
            elif isinstance(item, Book) and keyword_lower in item.author.lower():
                results.append(item)
        return results

    def list_all_items(self):
        return list(self._items.values())

    def list_all_users(self):
        return list(self._users.values())

    def __len__(self):
        return len(self._items)

    def __getitem__(self, item_id):
        return self._items.get(item_id, None)

    @classmethod
    def create_preloaded_library(cls):
        lib = cls()
        lib.add_item(Book("B001", "Python Crash Course", "Eric Matthes"))
        lib.add_item(Book("B002", "Data Structures and Algorithms in Python", "Michael T. Goodrich"))
        lib.add_item(Book("B003", "Fundamentals of Financial Management", "Eugene F. Brigham"))
        lib.register_user(User("U001", "Xiaoming"))
        lib.register_user(StaffUser("U002", "Xiaohong", "Library Dept"))
        return lib
