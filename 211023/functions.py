from random import randint as rng


# Checking any user input
def check_input(msg, choices):
    answ = int(input(msg))
    if answ in choices:
        return answ
    else:
        print("Please choose one of the given options.")
        return check_input(msg, choices)


def check_date(msg, range1, range2):
    date = int(input(msg))
    if date < range1 or date > range2:
        print("Please choose a valid date.")
        return check_date(msg, range1, range2)
    else:
        return date


def check_validity(msg, size):
    value = int(input(msg))
    if value > size:
        print("Insert a valid value.")
        return check_validity(msg, size)
    else:
        return value


def print_date(year, month, day, current_year, current_month, current_day):
    # Month = 30 Days
    # Year = 12 Months = 360 Days

    # Daycounts in variables for legibility
    current_daycount = (current_year * 360) + (current_month * 30) + current_day
    birthday_daycount = (year * 360) + (month * 30) + day

    print(f"You lived for {current_daycount - birthday_daycount} days on your life!")


def catch_percentage(value, percentage):
    percent = (value * percentage) / 100
    return percent


def catch_percentual(value, total):
    percent = (value / total) * 100
    return percent


def print_multiples(number, size):
    multiplier = 0
    while multiplier < size:
        multiplier += 1
        print(f"{number} x {multiplier} = {number * multiplier}")


def check_multiples(number, size):
    checking = -1
    while checking < size:
        checking += 1
        if checking % number == 0:
            print(f"{checking}")


def check_speed(msg):
    speed = input(msg)
    if speed == '':
        speed = rng(1, 120)
        print(f"As you chose no value, the speed was defined as {speed} Km/h.\n")
        return speed
    else:
        return int(speed)
