import random
imię = input("imię postaci: ")
siła = int(input("podaj silę"))
zręczność = int(input("podaj zręczność"))
wytrzymałość = int(input("podaj wytrzymałość"))
inteligencja = int(input("podaj inteligencję"))
mądrość = int(input("mądrość"))
charyzma = int(input("podaj charyzmę"))

hp = wytrzymałość * 6 + 10 + wytrzymałość 
ac = zręczność + 12 

imię_Goblina = "szadi"
siła_Goblina = -1
zręczność_Goblina = 2
wytrzymałość_Goblina = 0
inteligencja_Goblina = 0
mądrość_Goblina = -1
charyzma_Goblina = -1

hp_Goblina = 9
ac_Goblina = 15

run = True

while run:
    akcja_postaci = input("podaj akcję postaci,do wyboru: atak długim mieczem, atak pięścią, fire bolt, atak długim łukiem, atak krótkim łukiem, Thunderclap, Poison Spray, Ray of Frost, Absorb Elements, Magic Stone, Acid Splash: ")
    if akcja_postaci == "atak krótkim mieczem":
        rzut_na_trafienia = random.randint(1, 21) + zręczność
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - zręczność:
                rzut_na_obrażenia = random.randint(1,6) + random.randint(1,6) + zręczność
            else:
                rzut_na_obrażenia = random.randint(1,6) + zręczność
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if akcja_postaci == "atak długim mieczem":
        rzut_na_trafienia = random.randint(1, 21) + siła
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - siła:
                rzut_na_obrażenia = random.randint(1,11) + random.randint(1,11) + siła
            else:
                rzut_na_obrażenia = random.randint(1,11) + siła
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if akcja_postaci == "atak pięścią":
        rzut_na_trafienia = random.randint(1, 21) + siła
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - siła:
                rzut_na_obrażenia = random.randint(1,5) + random.randint(1,5) + siła
            else:
                rzut_na_obrażenia = random.randint(1,5) + siła
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")    
    if akcja_postaci == "fire bolt":
        rzut_na_trafienia = random.randint(1, 21) + inteligencja
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - inteligencja:
                rzut_na_obrażenia = random.randint(1,11) + random.randint(1,11) + inteligencja
            else:
                rzut_na_obrażenia = random.randint(1,11) + inteligencja
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")   
    if akcja_postaci == "atak długim łukiem":
        rzut_na_trafienia = random.randint(1, 21) + zręczność
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - zręczność:
                rzut_na_obrażenia = random.randint(1,9) + random.randint(1,9) + zręczność
            else:
                rzut_na_obrażenia = random.randint(1,9) + zręczność
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if akcja_postaci == "atak krótkim łukiem":
        rzut_na_trafienia = random.randint(1, 21) + zręczność
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - zręczność:
                rzut_na_obrażenia = random.randint(1,6) + random.randint(1,6) + zręczność
            else:
                rzut_na_obrażenia = random.randint(1,6) + zręczność
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if akcja_postaci == "Thunderclap":
        rzut_na_trafienia = random.randint(1, 21) + wytrzymałość
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - wytrzymałość:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + wytrzymałość
            else:
                rzut_na_obrażenia = random.randint(1,7) + wytrzymałość
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")   
    if akcja_postaci == "Poison Spray":
        rzut_na_trafienia = random.randint(1, 21) + mądrość
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - mądrość:
                rzut_na_obrażenia = random.randint(1,8) + random.randint(1,8) + mądrość
            else:
                rzut_na_obrażenia = random.randint(1,8) + mądrość
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło") 
    if akcja_postaci == "Ray of Frost": 
        rzut_na_trafienia = random.randint(1, 21) + inteligencja
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - inteligencja:
                rzut_na_obrażenia = random.randint(1,9) + random.randint(1,9) + inteligencja
            else:
                rzut_na_obrażenia = random.randint(1,9) + inteligencja
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia)) 
        else:
            print("pudło")
    if akcja_postaci == "Absorb Elements": 
        rzut_na_trafienia = random.randint(1, 21) + mądrość
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - mądrość:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + mądrość
            else:
                rzut_na_obrażenia = random.randint(1,7) + mądrość
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia)) 
        else:
            print("pudło")
    if akcja_postaci == "Magic Stone": 
        rzut_na_trafienia = random.randint(1, 21) + siła
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - siła:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + siła
            else:
                rzut_na_obrażenia = random.randint(1,7) + siła
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia)) 
        else:
            print("pudło")
    if akcja_postaci == "Acid Splash": 
        rzut_na_trafienia = random.randint(1, 21) + charyzma
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - charyzma:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + charyzma
            else:
                rzut_na_obrażenia = random.randint(1,7) + charyzma
            hp_Goblina = hp_Goblina - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia)) 
        else:
            print("pudło") 
    #Tura Goblina
    print('Tura Goblina')
    losowa_akcja = random.randint(1,12)
    if losowa_akcja == 1:
        print("atak szablą")
        rzut_na_trafienia = random.randint(1, 21) + zręczność_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - zręczność_Goblina:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + zręczność_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,7) + zręczność_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 2:
        print("atak długim łukiem")
        rzut_na_trafienia = random.randint(1, 21) + zręczność_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - zręczność_Goblina:
                rzut_na_obrażenia = random.randint(1,9) + random.randint(1,9) + zręczność_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,9) + zręczność_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 3:
        print("atak krótkim łukiem")
        rzut_na_trafienia = random.randint(1, 21) + zręczność_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - zręczność_Goblina:
                rzut_na_obrażenia = random.randint(1,6) + random.randint(1,6) + zręczność_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,6) + zręczność_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 4:
        print("Ray of Frost")
        rzut_na_trafienia = random.randint(1, 21) + inteligencja_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - inteligencja_Goblina:
                rzut_na_obrażenia = random.randint(1,9) + random.randint(1,9) + inteligencja_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,9) + inteligencja_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 5:
        print("Fire bolt")
        rzut_na_trafienia = random.randint(1, 21) + inteligencja_Goblina
        if rzut_na_trafienia> ac_Goblina:
            if rzut_na_trafienia == 20 - inteligencja_Goblina:
                rzut_na_obrażenia = random.randint(1,11) + random.randint(1,11) + inteligencja_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,11) + inteligencja_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło") 
    if losowa_akcja == 6:
        print("Poison Spray")
        rzut_na_trafienia = random.randint(1, 21) + mądrość_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - mądrość_Goblina:
                rzut_na_obrażenia = random.randint(1,13) + random.randint(1,13) + mądrość_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,13) + mądrość_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 7:
        print("Thorn Whip")
        rzut_na_trafienia = random.randint(1, 21) + charyzma_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - charyzma_Goblina:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + charyzma_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,7) + charyzma_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 8:
        print("Frostbite")
        rzut_na_trafienia = random.randint(1, 21) + mądrość_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - mądrość_Goblina:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + mądrość_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,7) + mądrość_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 9:
        print("Magic Stone")
        rzut_na_trafienia = random.randint(1, 21) + siła_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - siła_Goblina:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + siła_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,7) + siła_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 10:
        print("Green-Flame Blade")
        rzut_na_trafienia = random.randint(1, 21) + charyzma_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - charyzma_Goblina:
                rzut_na_obrażenia = random.randint(1,9) + random.randint(1,9) + charyzma_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,9) + charyzma_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia))
        else:
            print("pudło")
    if losowa_akcja == 11:
        print("Acid Splash")
        rzut_na_trafienia = random.randint(1, 21) + charyzma_Goblina
        if rzut_na_trafienia> ac:
            if rzut_na_trafienia == 20 - charyzma_Goblina:
                rzut_na_obrażenia = random.randint(1,7) + random.randint(1,7) + charyzma_Goblina
            else:
                rzut_na_obrażenia = random.randint(1,7) + charyzma_Goblina
            hp = hp - rzut_na_obrażenia        
            print("zadano obrażenia: "+ str(rzut_na_obrażenia)) 
        else:
            print("pudło")
    
    if hp_Goblina< 0 and hp< 0:
        print("Goblin nieżyje, ale bohater też nie")
        break
    if hp_Goblina< 0:
        print("Goblin pokonany")
        break
    if hp< 0:
        print("zostałeś pokonany")
        break