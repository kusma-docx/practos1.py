from user import User
from regular_user import RegularUser

class Admin(User): #методы для управления книгами и пользователями, скрывая детали реализации этих операций.
    def __init__(self, username, password):
        super().__init__(username, password, "Admin")

# абстрагирует процесс добавления книги
    def add_book(self, books): #Инкапсуляция
        title = input("Введите название книги: ") #Полиморфизм
        author = input("Введите автора книги: ")
        genre = input("Введите жанр книги: ")
        books.append({"title": title, "author": author, "genre": genre})
        print("Книга успешно добавлена!")

    def remove_book(self, books):
        title = input("Введите название книги для удаления: ")
        book_to_remove = next((book for book in books if book['title'].lower() == title.lower()), None)
        if book_to_remove:
            books.remove(book_to_remove)
            print("Книга успешно удалена!")
        else:
            print("Книга не найдена.")

    def update_book(self, books):
        title = input("Введите название книги для обновления: ")
        book_to_update = next((book for book in books if book['title'].lower() == title.lower()), None)
        if book_to_update:
            new_title = input("Введите новое название книги (или нажмите Enter для сохранения): ")
            new_author = input("Введите нового автора книги (или нажмите Enter для сохранения): ")
            new_genre = input("Введите новый жанр книги (или нажмите Enter для сохранения): ")
            if new_title:
                book_to_update['title'] = new_title
            if new_author:
                book_to_update['author'] = new_author
            if new_genre:
                book_to_update['genre'] = new_genre
            print("Данные книги успешно обновлены!")
        else:
            print("Книга не найдена.")

    def add_user(self, users):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        role = input("Введите роль (Admin/User): ").capitalize()
        if role == "Admin":
            new_user = Admin(username, password)
        elif role == "User":
            new_user = RegularUser(username, password)
        else:
            print("Некорректная роль. Пользователь не добавлен.")
            return
        users.append(new_user)
        print(f"Пользователь {username} успешно добавлен!")