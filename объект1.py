def fn():
    obj_const = {"name": "Marcus"}

    obj_var = {"name": "Aurelius"}

    obj_const["name"] = "Updated Marcus"
    obj_var["name"] = "Updated Aurelius"

    obj_var = {"name": "New Aurelius"}   
    
    return obj_const, obj_var

# Пример вызова
print(fn())
# Вывод: ({'name': 'Updated Marcus'}, {'name': 'New Aurelius'})
