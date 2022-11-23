def monster_encounter():
print(f"incontri {monster_name}")
while monster_hp > and player_hp > 0
    moveChoice = get_int("Cosa fai?\n1 attacchi\n2 difendi\n3 oggetti\n")
    if moveChoice == 1:
        attaccoplayer()
    elif monster_hp > 0:
        attacco_monster()
    else:
        print(f"{monster_name} muore")