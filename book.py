
class Book(object):
    def __init__(self, title, author, genre): #атрибуты объекта, но доступ к ним осуществляется через методы
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self): #абстрагирует процесс преобразования объекта книги в строку, скрывая детали форматирования.
        return f"{self.title} ({self.author}, {self.genre})"