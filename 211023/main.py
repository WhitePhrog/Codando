import functions as fnct

choice = fnct.check_input("Bem vindo! Que exercício deseja checar?\n"
                          "[1] Checking age in days.\n"
                          "[2] Final price from factory price.\n"
                          "[3] Percentual votes in an election.\n"
                          "[4] Exchanging reais and dollars.\n"
                          "[5] Calculating hypothenuse.\n"
                          "[6] Multiples of a number.\n"
                          "[7] Multiples between 0 and 500.\n"
                          "[8] Radar simulation.\n", [1, 2, 3, 4, 5, 6, 7, 8])

if choice == 1:
    # Exercise 1 - Checking age in days.
    # Checking birthday
    year = int(input(("Welcome to our date calculator!\n"
                      "Please, tell me the year at which you were born!\n")))

    month = fnct.check_date("Now, tell me the number of the month your were born.\n", 1, 12)

    day = fnct.check_date("Thank you! Now tell me the day at which you were born.\n", 1, 30)

    # Checking current year
    while True:
        current_year = int(input("Now tell me what year are we in.\n"))
        if current_year > year:
            break
        else:
            print("Choose a valid year.")
            continue

    current_month = fnct.check_date("Now tell me the number of the month we are currently in.\n", 1, 12)
    current_day = fnct.check_date("Now tell me what day are we in.\n", 1, 30)

    # Printing days
    fnct.print_date(year, month, day, current_year, current_month, current_day)

elif choice == 2:
    # Exercise 2 - Final price from factory price.
    factory_price = int(input("Welcome to our price calculator!\n"
                              "What is the factory price for the product you are analyzing?\n"))
    # Final price in variable for legibility.
    final_price = factory_price + fnct.catch_percentage(factory_price, 28) + fnct.catch_percentage(factory_price, 45)
    print(f"The consumer price of this product is of R${final_price}.")

elif choice == 3:
    # Exercise 3 - Percentual votes in an election.
    voters = int(input("How many voters are there in this election?\n"))

    while True:
        blank = fnct.check_validity("How many blanks are in this election?\n", voters)
        null = fnct.check_validity("How many null votes are there in this election?\n", voters)
        invalid = fnct.check_validity("How many votes were invalidated?\n", voters)
        if blank + null + invalid > voters:
            print("These values are invalid, as they surpass the total number of voters. Trying again...")
            continue
        else:
            break

    print(f"In this election, there were {voters} voters.\n"
          f"{fnct.catch_percentual(blank, voters)}% were blanks...\n"
          f"{fnct.catch_percentual(null, voters)}% were null votes...\n"
          f"{fnct.catch_percentual(invalid, voters)}% were invalidated...\n"
          f"And {fnct.catch_percentual((voters - blank - null - invalid), voters)}% were valid votes!")

elif choice == 4:
    # Exercise 4 - Exchanging reais and dollars.
    reais = float(input("What is the value you wish to exchange?\n"))

    # Current exchange rate
    exchange_rate = 5.03

    print(f"According to the current exchange rate (US$1.00 -> R${exchange_rate}), R${round(reais, 2)} is valued in "
          f"US${round(round(reais, 2) / exchange_rate, 2)}.")

elif choice == 5:
    # Exercise 5 - Calculando hipotenusa.
    c_adj = int(input("Bem vindo à calculadora de hipotenusa. Diga-me o cateto adjacente.\n"))
    c_opt = int(input("Excelente, agora diga-me o cateto oposto.\n"))
    print(f"A hipotenusa é igual a {round((c_adj**2 + c_opt**2)**.5, 2)}")

elif choice == 6:
    # Exercise 6 - Multiples from 1 to 10.
    number = int(input("Choose a number on which I'll show you its multiples from 1 to 10.\n"))
    fnct.print_multiples(number, 10)

elif choice == 7:
    # Exercise 7 - Mutiples from 1 to 500.
    # Obs.: Changed script so that it works with whatever number the user chooses, not only 6.
    num = int(input("Choose a number to print its multiples from 1 to 500.\n"))
    print(f"The following numbers are multiples of {num}")
    fnct.check_multiples(num, 500)
    print("Thank you!")

else:
    # Exercise 8 - Radar Simulation
    speed = fnct.check_speed("Welcome to our radar system. At what speed is your vehicle? (It will be read as Km/h)\n\n"
                             "Keep in mind that, be it that you do not select a value, one will be randomly chosen "
                             "between 1 and 120.\n")

    if speed < 30:
        print("Your vehicle is too slow, please change lanes.")

    elif speed > 90:
        print("Your vehicles it too fast!\n"
              f"You will now be fined for R${(speed - 90) * 7}")

    else:
        print("You are driving at an adequate speed! Congratulations and safe travels.")