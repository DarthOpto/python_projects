target = int(input("Please enter a target number between 1 and 1000. \n"))
total = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        total += number

print(total)