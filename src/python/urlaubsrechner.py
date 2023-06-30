
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

    print(holiday)
    return holiday

#################################################################################################################################################
#                                                              Urlaubszusätze
def check_boni(holiday, disability, age):
    if disability >= 50:
        holiday +=5

    if age > 25:
        while True:
            try:
                seniority = 0
                seniority = int(input("Wie viel Jahre sind sie beriets im Betrieb "))
                break
            except ValueError:
                print("Verwenden sie nur ganze Zahlen")

    if seniority >= 10:
        holiday +=2
    return holiday
    
#################################################################################################################################################

age, disability = get_inf()
holiday = check_holiday(age)
holiday = check_boni(holiday, disability, age)

print("Sie haben",holiday ,"Tage an Urlaub")