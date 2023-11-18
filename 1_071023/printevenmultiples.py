num = int(input("Choose a number: "))
multiple = 0
multiplier = 1

while multiple != (num * 100):
    multiple = num * multiplier
    if multiple % 2 == 0:
        print(f"{num} * {multiplier} = {multiple}")
    multiplier += 1
