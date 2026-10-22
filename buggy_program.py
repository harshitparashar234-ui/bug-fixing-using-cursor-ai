
# Buggy program: calculate the average of numbers

numbers = [10, 20, 30, 40, 50]

total = 0
for i in range(len(numbers) + 1):
    total = total + numbers[i]

average = total / len(numbers)
print("Average:", average)
