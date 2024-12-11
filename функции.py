def average(a, b):
    return (a + b) / 2

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def calculate():
    results = []
    for i in range(10):  # Цикл от 0 до 9
        sq = square(i)  # Квадрат числа
        cb = cube(i)    # Куб числа
        avg = average(sq, cb)  # Среднее квадрата и куба
        results.append(avg)
    return results

# Пример вызова
print(calculate())  # Выводит массив средних значений
