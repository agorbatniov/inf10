numbers = [5, 10, 3, 8, 15]
max_num = numbers[0]  # Предполагаем, что 
                      # первый элемент – 
					  # максимальный
for num in numbers:
    if num > max_num:
        max_num = num

print("Максимальное число:", max_num)