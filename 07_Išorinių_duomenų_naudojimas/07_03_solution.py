with open("input.txt", "r", encoding="utf-8") as file:
    numbers = [int(line.strip()) for line in file]

total = sum(numbers)
average = total / len(numbers)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"Сумма: {total}\n")
    file.write(f"Среднее: {average}\n")