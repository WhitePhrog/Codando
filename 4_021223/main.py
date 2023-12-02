def checkinput(msg, array):
    choic = int(input(msg))
    if choic in array:
        return choic
    print("Please, choose one of the offered numerical values.\n")
    return checkinput(msg, array)


options = ['female', 'male']
people = {}
choice = 0
adults = 0
g_males = 0
y_females = 0


print("Welcome to our registering system. Let's register our first person.")

while choice != 2:
    name = input("Tell us the person's name: ")
    age = int(input("Now tell us the person's age: "))
    gender = checkinput("What is the person's gender?\n"
                        "1- Female\n"
                        "2- Male\n", [1, 2])

    if name in people.keys():
        namelist = list(people.keys())
        ocurrences = namelist.count(name)
        name = name + str(ocurrences)
        print(name)

    people[name] = [age, options[gender - 1]]
    choice = checkinput(f"You registered '{name}', a {age} year old {options[gender - 1]}.\n"
                        f"Do you wish to register anyone else?\n"
                        f"1- Yes.\n"
                        f"2- No.\n", [1, 2])

for k in people.keys():
    if people[k][0] >= 18:
        adults += 1
    if people[k][1] == "male":
        g_males += 1
    elif people[k][0] < 20:
        y_females += 1

print("Understood! Here's some random, arbitrary information required by the gods above:\n"
      f"There are {adults} adults!\n"
      f"There are {g_males} males!\n"
      f"There are {y_females} females under 20 years of age!\n\n"
      f"And here are all the people registered:\n\n")

for k in people.keys():
    print(f"Name: {k}\n"
          f"Age: {people[k][0]}\n"
          f"Gender: {people[k][1]}\n\n")

print("Thank you for participating!")
