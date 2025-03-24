with open("input.txt", "r", encoding="utf-8") as file:
    numbers = []
    for line in file:
        numbers.append(int(line))

# calculate sum
sum = 0
for num in numbers:
    sum += num
   
# average
avg = sum / len(numbers)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Сумма: " + str(sum) + "\n")
    file.write("Среднее: " + str(avg) + "\n")    



