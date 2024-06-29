from enum import Enum

class UserType(Enum):
    ENGINEER = 1
    MANAGER = 2

class User:
    def __init__(self, name, age, user_type, phone, phone_code):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone
        self.phone_code = phone_code

    def get_phone_number(self):
        return f"{self.phone_code}{self.phone}"

    def print_details(self):
        # Виведення інформації про користувача
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Type: {self.user_type.name}")
        print(f"Phone: {self.get_phone_number()}")

# Приклад використання класу
user = User("John", 25, UserType.ENGINEER, "9379992", "050")
user.print_details()
