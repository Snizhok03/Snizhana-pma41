from abc import ABC, abstractmethod

# Загальний інтерфейс ітераторів.
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Конкретний ітератор для списку користувачів.
class UsersListIterator(Iterator):
    def __init__(self, users):
        self._users = users
        self._index = 0

    def has_next(self):
        return self._index < len(self._users)

    def next(self):
        if self.has_next():
            user = self._users[self._index]
            self._index += 1
            return user
        else:
            raise StopIteration("End of collection reached")

# Конкретний ітератор для словника користувачів.
class UsersDictIterator(Iterator):
    def __init__(self, users):
        self._users = users
        self._keys = list(users.keys())
        self._index = 0

    def has_next(self):
        return self._index < len(self._keys)

    def next(self):
        if self.has_next():
            key = self._keys[self._index]
            user = self._users[key]
            self._index += 1
            return user
        else:
            raise StopIteration("End of collection reached")

# Загальний інтерфейс колекцій.
class UsersCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Конкретна колекція - список користувачів.
class UsersListCollection(UsersCollection):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def create_iterator(self):
        return UsersListIterator(self._users)

# Конкретна колекція - словник користувачів.
class UsersDictCollection(UsersCollection):
    def __init__(self):
        self._users = {}

    def add_user(self, user_id, user):
        self._users[user_id] = user

    def create_iterator(self):
        return UsersDictIterator(self._users)

# Приклад класу користувача
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

# Приклад використання:
list_collection = UsersListCollection()
list_collection.add_user(User(1, "John"))
list_collection.add_user(User(2, "Alice"))
list_collection.add_user(User(3, "Bob"))

dict_collection = UsersDictCollection()
dict_collection.add_user(101, User(101, "Jane"))
dict_collection.add_user(102, User(102, "Doe"))

# Використання ітератора для списку користувачів
list_iterator = list_collection.create_iterator()
while list_iterator.has_next():
    user = list_iterator.next()
    print(f"User ID: {user.user_id}, Name: {user.name}")

# Використання ітератора для словника користувачів
dict_iterator = dict_collection.create_iterator()
while dict_iterator.has_next():
    user = dict_iterator.next()
    print(f"User ID: {user.user_id}, Name: {user.name}")
