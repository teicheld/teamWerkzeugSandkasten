import random
User_wins= 0
bot_wins = 0
options = ["schere", "stein", "papier", "echse", "spock"]

while True:

    player_choice = input("Wähle Schere,Stein, Papier, Echse oder Spock. Drücke 'Q' zum beenden oder 'P' für den aktuellen Punktestand : ").lower()

    if player_choice == "q":
        break
    if player_choice == "p":
        print("Aktueller Punktestand")
        print("Spieler", User_wins)
        print("Bot", bot_wins)
        continue

    if player_choice not in options:
        print("!!Fehlerhafte eingabe!!")
        continue

    bot_random = random.randint(0,4)
    bot_choice = options[bot_random]
    print("Peter bot wählt",bot_choice)

    if player_choice == bot_choice:
        print("Unentschieden")
    elif (player_choice == "schere" and bot_choice in ["papier", "echse"]) or \
         (player_choice == "stein" and bot_choice in ["schere", "echse"]) or \
         (player_choice == "papier" and bot_choice in ["stein", "spock"]) or \
         (player_choice == "echse" and bot_choice in ["papier", "spock"]) or \
         (player_choice == "spock" and bot_choice in ["schere", "stein"]):
            User_wins += 1
            print("Sie haben gewonnen")





    else:
        bot_wins +=1
        print("Du hast verloren!")

print("Aktueller Punktestand")
print("Spieler", User_wins)
print("Bot", bot_wins)