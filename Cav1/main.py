# GUERREIRO
# 5, 10 PWR
# 3, 10 ATK (2 PWR COST)
# 1 HEAL
# Não consume PWR para defender.

# MAGO
# 7, 15 PWR
# 0, 8 ATK (2 PWR COST)
# 4 HEAL

import rpg_function as rpg
from random import randint as rng

# Variáveis de seleção de classe.
(player_class, player_maxpower, player_maxatk,
 player_minatk, player_heal, def_cost, player_maxhp) = rpg.class_choice()

# Status iniciais do inimigo.
monster_atk, monster_maxhp = rpg.update_monster(0, 0, 3, 20)

# Monstros derrotados para resumo final
defeated_monsters = 0

print(f"\nYou are a {player_class}! These are your stats:\n"
      f"{player_maxpower} [PWR]\n"
      f"{player_minatk} - {player_maxatk} [ATK]\n"
      f"{player_heal} [HEAL]\n"
      f"{def_cost} [DEF COST]\n"
      f"We'll now begin the exploration to the Deep Dark.\n")

while True:
    print("You've met a monster!")

    # Resetting current monster and player health
    monster_hp = monster_maxhp
    player_hp = player_maxhp
    player_power = player_maxpower

    while monster_hp > 0 and player_hp > 0:
        print("PLAYER:\n"
              f"HP: {player_hp}/{player_maxhp}\n"
              f"PWR: {player_power}/{player_maxpower}\n"
              f"ATK: {player_minatk} - {player_maxatk}\n"
              f"HEAL: {player_heal}\n\n"
              f"MONSTER:\n"
              f"HP: {monster_hp}/{monster_maxhp}\n"
              f"ATK: {monster_atk}\n")

        # Checking player action
        choice = rpg.check_input("Do you want to...\n"
                                 "[1] Attack!\n"
                                 "[2] Defend!\n"
                                 "[3] Heal!\n"
                                 "[4] Rest!\n", [1, 2, 3, 4])
        monster_intention = rng(1, 2)

        # Attack
        if choice == 1:
            monster_hp = rpg.player_attack(player_minatk, player_maxatk, monster_hp, monster_intention)

        # Defend
        elif choice == 2:

            # Checking player defense
            if player_power - def_cost > -1:
                player_power = rpg.player_defend(player_power, def_cost, monster_intention, player_class)

            # Player unable to defend
            else:
                print("You do not have enough power to defend! Choose another option.")
                continue

        # Heal
        elif choice == 3:
            player_hp = rpg.player_heal(player_hp, player_maxhp, player_heal)

        # Rest
        else:
            player_power = rpg.player_rest(player_power, player_maxpower)

        # Monster attack (If chosen and not defended against)
        if monster_intention == 1 and choice != 2:
            player_hp -= monster_atk
            print(f"You were hit by the creature! It caused {monster_atk} damage!")

    # Checking player death
    if player_hp <= 0:
        print("You were defeated...\n"
              "Better luck next time.\n"
              f"You defeated {defeated_monsters} monsters.\n"
              f"Goodbye, and may you find you way to the Deep Dark once again!")
        break

    # Checking player victory
    else:
        defeated_monsters += 1
        choice = rpg.check_input("Congratulations! You have felled the creature!\n"
                                 f"With this, you have defeated {defeated_monsters} monsters.\n"
                                 f"Do you wish to...\n"
                                 f"[1] Continue your expedition?\n"
                                 f"[2] Exit the deep dark?\n", [1, 2])
        if choice == 1:
            print("Great! Both you and your foes just got stronger!")
            player_maxhp, player_maxatk = rpg.update_player(player_maxhp, player_maxatk, 5, 3)
            monster_maxhp, monster_atk = rpg.update_monster(monster_atk, monster_maxhp, 10, 3)
        else:
            print("Better luck next time then!\n"
                  "Goodbye, and may you find")
            break
