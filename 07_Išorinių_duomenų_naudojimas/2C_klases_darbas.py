with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read()
lines = data.split("\n")

sum = 0
for i in lines:
    sum += int(i)
avg = sum / len(lines)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Сумма: " + str(sum) + "\n")
    file.write("Среднее: " + str(avg))