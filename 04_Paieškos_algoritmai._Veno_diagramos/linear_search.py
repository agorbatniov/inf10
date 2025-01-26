array = [3, 5, 7, 9, 11]
x = int(input("Введите число для поиска: "))
found = False
for i in array:
    if i == x:
        found = True
        break
if found:
    print("Число найдено")
else:
    print("Число не найдено")