from admin import Admin
from regular_user import RegularUser
from book import Book

users = [Admin("Админ", "admin_you"), RegularUser("Пользователь", "user_you")]
books = [
    Book("Маленький принц", "Антуан де Сент-Экзюпери", "Сказка"),
    Book("Война и мир", "Лев Толстой", "Роман-Эпопея"),
    Book("1984", "Джордж Оруэлл", "Антиутопия"),
    Book("Мастер и Маргарита", "Михаил Булгаков", "Фантастика"),
    Book("Дубровский", "Александр Пушкин", "Роман"),
    Book("Девочка со спичками", "Ханс Кристиан Андерсен", "Сказка"),
    Book("Преступление и наказание", "Фёдор Достоевский", "Психологический роман"),
    Book("Убийства на улице Морг", "Эдгар Аллан По", "Детектив")
]

current_user = None

def authorize_user():
    global current_user
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user.username == username and user._check_password(password, user.password):
            current_user = user
            print(f"Выполнен вход, {current_user.username} ({current_user.role})!")
            return True
    print("Неверный логин или пароль.")
    return False

def logout():
    global current_user
    current_user = None
    print("Вы вышли из системы. Возврат к экрану логина.")
    return True

def display_books(books):
    for book in books:
        print(f"Название: {book.title}, Автор: {book.author}, Жанр: {book.genre}")

def filter_books():
    genre = input("Введите жанр для фильтрации: ")
    filtered_books = [book for book in books if book.genre.lower() == genre.lower()] 
    if filtered_books:
        display_books(filtered_books)
    else:
        print("Книги по данному жанру не найдены.")

def sort_books():
    sort_by = input("Сортировать по (название/автор): ").lower()
    if sort_by == "название":
        sorted_books = sorted(books, key=lambda x: x.title) 
    elif sort_by == "автор":
        sorted_books = sorted(books, key=lambda x: x.author) 
    else:
        print("Некорректный выбор.")
        return
    display_books(sorted_books)

def view_users():
    for user in users:
        print(f"Имя: {user.username}, Роль: {user.role}")

def view_reserved_books():
    for user in users:
        if user.reserved_books:
            print(f"Пользователь {user.username} забронировал:")
            for book in user.reserved_books:
                print(f" - {book.title}")
        else:
            print(f"Пользователь {user.username} не имеет забронированных книг.")

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Просмотреть книги")
        print("2. Фильтрация книг")
        print("3. Сортировка книг")
        if current_user.role == "Admin":
            print("4. Добавить книгу")
            print("5. Удалить книгу")
            print("6. Обновить данные книги")
            print("7. Просмотреть пользователей")
            print("8. Просмотреть забронированные книги")
            print("9. Добавить пользователя")
            print("10. Выход из учетной записи")
            print("11. Выход")
        else:
            print("4. Забронировать книгу")
            print("5. Выйти из учетной записи")
            print("6. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                display_books(books)
            elif choice == "2":
                filter_books()
            elif choice == "3":
                sort_books()
            elif choice == "4" and current_user.role == "Admin":
                current_user.add_book(books)
            elif choice == "5" and current_user.role == "Admin":
                current_user.remove_book(books)
            elif choice == "6" and current_user.role == "Admin":
                current_user.update_book(books)
            elif choice == "7" and current_user.role == "Admin":
                view_users()
            elif choice == "8" and current_user.role == "Admin":
                view_reserved_books()
            elif choice == "9" and current_user.role == "Admin":
                current_user.add_user(users)
            elif choice == "10" and current_user.role == "Admin":
                if logout():
                    break
            elif choice == "4" and current_user.role == "User":
                current_user.reserve_book(books)
            elif choice == "5" and current_user.role == "User":
                if logout():
                    break
            elif (choice == "11" and current_user.role == "Admin") or (choice == "6" and current_user.role == "User"):
                print("Выход из системы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    while True:
        if authorize_user():
            main_menu()
        else:
            print("Попробуйте снова.")