from cs50 import get_int

player_hp_start_stats = 10
player_atk_start_stats = 3
player_def_start_stats = 0

bandit_hp_stats = 5
bandit_atk_stats = 1

spider_hp_stats = 12
spider_atk_stats = 2

sword_atk_stats = 2
shield_def_stats = 2
shield_use_limit_stats = 3

playerHP: int = 10
playerATK = 2
playerDEF = 0

bandit_hp: int = 8
bandit_atk = 3


def mortebandito(playerhp):
    print("il bandito muore")
    print(f"ti rimangono {playerhp}hp")
    return playerhp


def attaccobandito(bandit_hp, player_hp):
    print(f"al bandito rimane {bandit_hp}hp", )
    print("il brigante ti colpisce a sua volta")
    player_hp = player_hp - bandit_atk
    print(f"il suo colpo ha successo. subisci {bandit_atk}hp")
    print(f"hai ancora {player_hp}hp")
    return bandit_hp, player_hp


def attaccoplayer(bandit_hp):
    print("colpisci il bandito con un fendente")
    bandit_hp = bandit_hp - playerATK
    print(f"il bandito subisce {playerATK}hp di danno")
    return bandit_hp


doorChoice = get_int("quale porta apri?\n 1 sinistra\n 2 destra \n 3 centro\n")

if doorChoice == 1:
    print("incontri un bandito")
    while bandit_hp > 0 and playerHP > 0:
        if playerHP > 0:
            moveChoice = get_int("Cosa fai?\n 1 attacchi\n 2 pari\n 3 oggetto\n")
            if moveChoice == 1:
                attaccoplayer(bandit_hp)
                if bandit_hp > 0:
                    attaccobandito(playerHP, bandit_hp)
                else:
                    mortebandito(playerHP)
