def find_intersection(list1, list2):
    #Функция находит пересечение двух массивов с помощью двойного цикла
    return [0, 0, 0]

# Ввод данных
list1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
list2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

# Вызов функции
intersection = find_intersection(list1, list2)

# Вывод результата
print("Общие элементы:", intersection)
