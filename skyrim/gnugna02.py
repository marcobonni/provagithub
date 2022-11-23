from time import sleep
from cs50 import get_int
import random


def attacco_monster():
    global player_hp
    if monster_hp > 0:
        print(f"{monster_name} ti attacca a sua volta ")
        player_hp -= monster_atk
        print(f"ti infligge {monster_atk} di danno")
        print(f"ti rimangono {player_hp}hp")


def monster_encounter():
    print(f"incontri {monster_name}")
    while monster_hp > 0 and player_hp > 0:
        move_choice = get_int("Cosa fai?\n1 attacchi\n2 difendi\n3 oggetti\n")
        if move_choice == 1:
            attaccoplayer()


def bandit_encounter():
    global monster_name
    monster_name = "bandito"
    global monster_hp
    monster_hp = bandit_hp
    global monster_atk
    monster_atk = bandit_atk


def spider_encounter():
    global monster_name
    monster_name = "ragno"
    global monster_hp
    monster_hp = spider_hp
    global monster_atk
    monster_atk = spider_atk


def attaccoplayer():
    global monster_hp
    global monster_name
    print(f"colpisci {monster_name} con un fendente")
    sleep(1)
    roll_atk = player_atk + random.randint(0, player_luck)
    print(roll_atk)
    monster_hp -= roll_atk
    print(f"il mostro subisce {roll_atk} di danno")
    sleep(1)
    print(f"{monster_name} ha ancora {monster_hp}hp")
    if monster_hp > 0:
        attacco_monster()


def ottenimento_spada():
    global player_atk
    print("ottieni spada! +2 al tuo attacco")
    swordstat = 2
    player_atk += swordstat
    print(f"adesso hai {player_atk} d'attacco")


def ottenimento_cura():
    global player_hp
    print("ottieni cura! +2 ai tuoi hp")
    cura = 2
    player_hp += cura
    print(f"adesso hai {player_hp}hp")


def ottenimento_ciondolo():
    global player_luck
    print("ottieni ciondolo fortunato! +2 fortuna")
    ciondolo_fortunato = 2
    player_luck += ciondolo_fortunato
    print(f"adesso hai {player_luck} di fortuna")


def treasure_chest():
    numero_oggetto = random.randint(0, 2)
    print("trovi un forziere")
    if numero_oggetto == 0:  # fare funzione
        ottenimento_spada()
    elif numero_oggetto == 1:  # fare funzione
        ottenimento_cura()
    elif numero_oggetto == 2:  # fare funzione
        ottenimento_ciondolo()


def mutagens():
    global player_atk
    global player_hp
    player_atk = player_atk + 2
    player_hp = player_hp - 1


def gameover():
    print("sei morto, game over bro.")
    return -1


global monster_name
global monster_hp
global monster_atk
player_hp = 10
player_atk, player_luck = 3, 1
bandit_hp, bandit_atk = 6, 2
spider_hp, spider_atk = 2, 3
for i in range(3):
    doorChoice = get_int("quale porta apri?\n1 sinistra\n2 destra\n3 centro\n")
    doorRandom = random.randint(0, 2)
    if doorRandom == 0:
        bandit_encounter()
        monster_encounter()
        treasure_chest()
    elif doorRandom == 1:
        spider_encounter()
        monster_encounter()
        treasure_chest()
    else:
        treasure_chest()
print("A man with an eyepatch and a devilish grin strides up to you.")
sleep(1)
print(
    "Shady Man: Hey there, stranger. Interested in advancing science? I can make you stronger than any training or blessing. You're gonna need it if you're one of those heroes with a death wish.")
sleep(3)
print("Whad'ya say?")
sleep(1)
jax_choice = get_int("1 test J.A.X\n2 Become Test subject\n3 ingest mutagens\n")
if jax_choice == 1:
    print(
        "Shady man: Excellent.\n The man hands over a dangerous looking syringe filled with a glowing liquid before skulking off into a shadowy alleyway.")
    print("ottieni un nuovo oggetto: J.A.X. = perdi 2 hp ma ottieni 2 di danno ")
elif jax_choice == 2:
    print("Shady man: Superb")
    sleep(1)
    print(
    "The man injects you with three unknown substances and pulls out a notepad. As you begin to feel light-headed, "
    "he starts to frantically write down notes.")
    sleep(1)
    print("ti senti molto meglio. le tue ferite guariscono completamente")
    if player_hp < 10:
        player_hp == 10
    print(f"adesso hai {player_hp}hp")
else:
    print("Shady man: Marvelous.")
    sleep(1)
    print("You quaff the mysterious substance. Immediately, you are invigorated and feel your muscle fibers twitch.")
    print("ottieni +2 forza ma perdi 1hp ogni turno")
    mutagens = 1
