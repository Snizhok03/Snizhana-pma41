from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Ініціалізація підключення до бази даних
        self.connection = None  # Представимо, що це підключення до бази даних

    @staticmethod
    def getInstance():
        return Database()

    def query(self, sql):
        # Логіка виконання запитів до бази даних
        pass

# Приклад використання
class Application:
    @staticmethod
    def main():
        foo = Database.getInstance()
        foo.query("SELECT ...")
        # ...
        bar = Database.getInstance()
        bar.query("SELECT ...")
        print(foo is bar)  # Поверне True, оскільки обидва змінних мають один і той самий екземпляр класу

Application.main()
