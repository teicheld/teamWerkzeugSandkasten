import time

''' age=alter
    disability=Behinderung
    seniority=Betrieszugehörigkeit'''
#################################################################################################################################################
#                                                              Bekomme Informationen
def get_inf():
    while True:
        try:
            age = int(input("Wie viele Jahre sind sie Alt? "))
            break
        except ValueError:
            print("Verwenden sie nur ganze Zahlen")
    
    while True:
        try:    
            disability = int(input("Wie hoch ist ihr Behinderungsgrad in %(Falls nicht vorhanden tragen sie 0 ein) "))
            break
        except ValueError:
            print("Verwenden sie nur ganze Zahlen")
    return age, disability  

#################################################################################################################################################
#                                                              Grundurlaub
def check_holiday(age):
    if age < 18:
        holiday = 30
    elif age > 55:
        holiday = 28
    else:
        holiday = 26

    #print(holiday)
    return holiday

#################################################################################################################################################
#                                                              Urlaubszusätze
def check_boni(holiday, disability, age):
    seniority = 0               # variable muss hier deklariert(erschaffen) werden, weil du die deklaration inerhalb der while schleife gemacht hast und du den wert auserhalb dieser abfragst, wo ihre gueltigkeit bereits beendet ist (dies passiert oefter in dem programm, aber python programmiert des um bei jeder ausfuehrung des programmes, damits trotzdem functioniert. siehe warnungen in thonny oder deiner ide)
    if disability >= 50:
        holiday +=5

    if age > 25:
        while True:
            try:
                seniority = int(input("Wie viel Jahre sind sie beriets im Betrieb "))
                break
            except ValueError:
                print("Verwenden sie nur ganze Zahlen")

    if seniority >= 10:
        holiday +=2
    return holiday
    
#################################################################################################################################################
#                                                       Fancy GluecksradAnzeige
def fancyAnzeige(zahl):

    for i in range(zahl):
        print(i, end='')                        # end='' verhindert neue zeile zeichen
        time.sleep(0.03)
        if i/10 < 1:
            print("\b", end='')                 # '\b' ist die taste ueber der enter taste (tippe "man ascii" in die websuchmaschine)
        else:
            print("\b\b", end='')
    print(i, end='')            


#################################################################################################################################################


age, disability = get_inf()
holiday = check_holiday(age)
holiday = check_boni(holiday, disability, age)

print("Sie haben ", end='')
fancyAnzeige(holiday)
print(" Tage an Urlaub")
