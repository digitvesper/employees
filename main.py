# Программа для управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь с таким ID не найден.")

    def display_users(self):
        print("Список пользователей:")
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Создаем пользователей
user1 = User(1, "Иван")
user2 = User(2, "Петр")
user3 = User(3, "Мария")

# Создаем администратора
admin = Admin(100, "Admin")

# Добавляем пользователей в список администратора
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Выводим список пользователей
admin.display_users()

# Удаляем пользователя с ID=2
admin.remove_user(2)

# Выводим обновленный список пользователей
admin.display_users()
