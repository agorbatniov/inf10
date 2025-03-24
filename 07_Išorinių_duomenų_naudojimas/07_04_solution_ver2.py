def read_numbers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]

def write_results(filename, total, average):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Сумма: {total}\nСреднее: {average}\n")

numbers = read_numbers("input.txt")
total, average = sum(numbers), sum(numbers) / len(numbers)
write_results("output.txt", total, average)