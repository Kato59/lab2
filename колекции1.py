# Массив объектов с полями name и phone
contacts = [
    {"name": "Marcus Aurelius", "phone": "+380445554433"},
    {"name": "Julius Caesar", "phone": "+380505554433"},
    {"name": "Cleopatra", "phone": "+380935554433"}
]

# Функция для поиска телефона по имени
def findPhoneByName(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact["phone"]
    return None

# Пример вызова
print(findPhoneByName("Marcus Aurelius"))  # Вывод: +380445554433
print(findPhoneByName("Unknown"))          # Вывод: None
