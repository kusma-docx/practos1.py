from user import User

class RegularUser(User):  # Наследуем от User
    def __init__(self, username, password):
        super().__init__(username, password, "User")  # Передаем роль User в родительский класс
        self.reserved_books = []  # Список для хранения забронированных книг

    def reserve_book(self, books):
        title = input("Введите название книги для бронирования: ")
        for book in books:
            if book.title.lower() == title.lower():
                self.reserved_books.append(book)  # Добавляем книгу в список забронированных
                print(f"Книга '{book.title}' успешно забронирована!")
                return
        print("Книга не найдена.")