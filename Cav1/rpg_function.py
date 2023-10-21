from random import randint as rng


# Checking player input on simple choices
def check_input(msg, choices):
    answ = int(input(msg))
    if answ in choices:
        return answ
    else:
        print("Please choose one of the given options.")
        return check_input(msg, choices)


# Checking player class choice and assigning status
def class_choice():
    p_class = int(input("Welcome to the Deep Dark, choose your class:\n"
                        "[1] Warrior\n"
                        "[2] Mage\n"))
    if p_class == 1:
        p_class = "warrior"
        maxpower = rng(5, 10)
        maxatk = 10
        minatk = 5
        heal = 1
        def_cost = 0
        player_maxhealth = 20
    elif p_class == 2:
        p_class = "mage"
        maxpower = rng(7, 15)
        maxatk = 8
        minatk = 0
        heal = 4
        def_cost = 1
        player_maxhealth = 15
    else:
        print("Choose one of the presented classes!")
        return class_choice()
    return p_class, maxpower, maxatk, minatk, heal, def_cost, player_maxhealth


# Updating monster after his defeat
def update_monster(m_atk, m_hp, plusatk, plushp):
    m_atk += plusatk
    m_hp += plushp
    return m_atk, m_hp


# Updating player stats when starting a new turn
def update_player(p_maxhp, p_maxatk, plushp, plusatk):
    p_maxhp += plushp
    p_maxatk += plusatk
    return p_maxhp, p_maxatk


# Player attacks monster
def player_attack(p_minatk, p_maxatk, m_hp, m_intention):
    if m_intention == 1:
        damage = rng(p_minatk, p_maxatk)
        m_hp -= damage
        print(f"You dealt {damage} damage!\n")
    else:
        print("Foul creature! It has defended against your attack, which bounces off harmlessly.\n")
    return m_hp


# Player defends against the monster
def player_defend(p_pwr, def_cost, m_intention, p_class):
    if m_intention == 1:
        p_pwr -= def_cost
        print("You have defended against the creature incoming attack! It dealt you no damage!\n"
              f"As a {p_class}, this has cost you {def_cost} power.")
    else:
        print("The monster has also tried to defend... How awkward.")
    return p_pwr


# Player heals his HP
def player_heal(p_hp, p_maxhp, p_heal):
    if p_hp + p_heal > p_maxhp:
        p_hp = p_maxhp
        print(f"You healed for {p_heal} HP, leaving you at your peak physique!\n")
    else:
        p_hp += p_heal
        print(f"You healed for {p_heal} HP, leaving you at {p_hp}/{p_maxhp} HP.\n")
    return p_hp


# Player recovers his power
def player_rest(p_pwr, p_maxpwr):
    recover = rng(1, 5)
    if (p_pwr + recover) > p_maxpwr:
        p_pwr = p_maxpwr
        print(f"You rested, regaining {recover} power. You are currently at maximum power!\n")
    else:
        p_pwr += recover
        print(f"You rested, regaining {recover} power. You are currently at {p_pwr} power!\n")
    return p_pwr
