import bcrypt
from cryptography.fernet import Fernet
from datetime import datetime

class User: #абстракция пользователя системы
    def __init__(self, username, password, role): #скрывает детали реализации, такие как хеширование пароля, шифрование данных и управление историей
        self.username = username
        self.password = self._hash_password(password) #Инкапсуляция
        self.role = role
        self.history = []
        self.created_at = datetime.now()
        self.reserved_books = []
        self.encryption_key = Fernet.generate_key()  # Уникальный ключ для каждого пользователя
        self.cipher_suite = Fernet(self.encryption_key)

    @staticmethod #пароль не хранится в открытом виде, и его проверка происходит через специальный метод.
    def _hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    @staticmethod
    def _check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password)

    def encrypt_data(self, data):
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()