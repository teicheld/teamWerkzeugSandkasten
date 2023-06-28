###### programm berechnet den urlaubstageanspruch
alter = int(input("alter in jahren?: "))
zeitImBetrieb = int(input("anzahl der jahre im betrieb?: "))
gradDerBehinderung = int(input("wie viel prozent behindert?: "))
urlaubstage = 26
if  alter < 18:
    urlaubstage = urlaubstage + 4
elif alter > 55:
    urlaubstage = urlaubstage + 2
if zeitImBetrieb >= 10:
    urlaubstage = urlaubstage + 2
if gradDerBehinderung >= 50:
    urlaubstage = urlaubstage + 5
print(urlaubstage)
