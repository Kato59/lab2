# Хеш-таблица для хранения телефонных номеров
phone_book = {
    "Marcus Aurelius": "+380445554433",
    "Julius Caesar": "+380505554433",
    "Cleopatra": "+380935554433"
}

# Функция для поиска телефона по имени
def findPhoneByNameHash(name):
    return phone_book.get(name, None)

# Пример вызова
print(findPhoneByNameHash("Marcus Aurelius"))  # Вывод: +380445554433
print(findPhoneByNameHash("Unknown"))          # Вывод: None
