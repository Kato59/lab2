def range_odd(start, end):
    return [x for x in range(start, end + 1) if x % 2 != 0]

# Пример вызова
print(range_odd(15, 30))  # [15, 17, 19, ..., 29]
