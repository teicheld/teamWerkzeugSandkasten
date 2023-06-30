spieler_eins = input("Spieler Eins dein Name bitte: ")
spieler_zwei = input("Spieler Zwei dein Name bitte: ")
#Hier kommt die Abfrage nach dem namen des Spielers#

spieler_eins_punkte = 0
spieler_zwei_punkte = 0
#Dies Definiert die gewonnene Punktzahl des jeweiligen Spielers#

options = ["Schere", "Stein", "Papier", "schere", "stein", "papier"] 
#Schere: 0, Stein: 1, Papier: 2#
#Durch: ["...", "...", "..."]  wird jede eingabe mit diesen worten in "options" darin überprüft#


while True:
    #Die "while-Schleife" ermöglicht die wiederholte Ausführung von diesem code solange nicht der Befehl "break" ausgelöst wird#

    Spieler_eins_input = input("{}, Schere, Stein, Papier oder Q zum Verlassen?: " .format(spieler_eins))
    if Spieler_eins_input == "q":                                                    #.format(Variabel) fügt eine erstellte Variabel in einen input() Befehl ein.# 
        break
            #break bricht das Spiel ab#

    Spieler_zwei_input = input("{}, Schere, Stein, Papier oder Q zum Verlassen?: " .format(spieler_zwei))#.lower()
    if Spieler_zwei_input == "q":                                                                         #.lower() wandelt Großbuchstaben in Kleinbuchstaben um#
        break

    if Spieler_eins_input not in options or Spieler_zwei_input not in options:
        print("Ungültige Eingabe. Bitte wähle eine der folgenden Optionen: Schere, Stein, Papier.")
        continue
            #continue bei falscher eingabe wird erneut hinterfragt welche option man wählt#

    if Spieler_eins_input == Spieler_zwei_input:
        print("Unentschieden!")
    elif (Spieler_eins_input == "schere" and Spieler_zwei_input == "papier") or \
         (Spieler_eins_input == "stein" and Spieler_zwei_input == "schere") or \
         (Spieler_eins_input == "papier" and Spieler_zwei_input == "stein"):
        print("{} gewinnt!".format(spieler_eins))
        spieler_eins_punkte += 1
    else:
        print("{} gewinnt!".format(spieler_zwei))
        spieler_zwei_punkte += 1

    if spieler_eins_punkte == 3 :
        print("{} Du hast das Spiel Gewonnen! " .format(spieler_eins))
        break
    elif spieler_zwei_punkte == 3 :
        print("{} Du hast das Spiel Gewonnen! " .format(spieler_zwei))
        break


print("Spiel beendet.")
print("Punktestand:")
print("{}: {}".format(spieler_eins, spieler_eins_punkte))
print("{}: {}".format(spieler_zwei, spieler_zwei_punkte))
print("PISZDATION")
