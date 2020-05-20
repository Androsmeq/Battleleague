
import time
import random
import secrets
def line():
    print("-------------------------------------------")


linie = 119
class fiinta:
    def __init__(self):
        self.hp = 100
        self.damage = 10
        self.crit = self.damage * 1.5
        self.items = []
        self.bani=10
    def luptator(self):
            self.items=["Armura_LVL_1", "Sabie_LVL_1"]
    def boost(self):
        if "Armura_LVL_1" in self.items:
            self.hp+= 20
        if "silver_armor" in self.items:
            self.hp+= 40
        if "diamond_armor" in self.items:
            self.hp+= 60
        if "Sabie_LVL_1" in self.items:
            self.damage+= 20
        if "silver_sword" in self.items:
            self.damage+= 40
        if "diamond_sword" in self.items:
            self.damage+= 60
    def default_chest(self):
        r = input("You found a bronze chest !, would you like to open it?(y/n)")
        line()
        if r == "y":
            input("Press <entrt> to open your chest!")
            time.sleep(1)
            nr = random.randint(1, 3)
            line()
            if nr == 1:
                print("Ai Primit Sabie LVL 2!")
                if "Sabie_LVL_2" in self.items:
                    print("Din pacate deja ai acest item :(")
                    print("Ti s-au oferit 10 bani pe acest item! ")
                    self.bani += 10
                else:
                    self.items.append("Sablie_LVL_2")
                    self.damage += 20
            if nr == 2:
                print("Ai primit armura lvl 2!")
                self.items.append("Armura_LVL_2")
                if "Armura_LVL_2" in self.items:
                    print("Din pacate deja ai acest item :(")
                    print("Ti s-au oferit 10 bani pe acest item! ")
                    self.bani += 10
                else:
                    self.items.append("Armura_LVL_2")
                    self.hp += 20
            if nr == 3:
                print("Din pacate nu ai primit nimic, dar ai primit 5 bani :)")
                self.bani+=5
            line()
            time.sleep(4)
            line()
            print("Current stats:")
            print("HP: " + str(character.hp))
            print("Damage: " + str(character.damage))
            print("Items: " + str(character.items))
            line()
            input("Press <enter> to continue.")

        time.sleep(1)

    #def easyspin(self):
       # nr = random.randint(1,10)
    def easy(self):
        print("Welcome to easy mode!")
        print("You will fight with 3 low characters! Good lock!")
        line()
        viata = self.hp
        damage= self.damage
        w = 0
        l = 0
        for i in range(1,4):
            if l== 1:
                break
            print("Opponent "+ str(i))
            d=[25, 30, 40]
            h= [50, 60, 70]
            odam = secrets.choice(d)
            ohealth = secrets.choice(h)
            print("HP: "+str(ohealth))
            print("Damage: "+str(odam))
            line()
            time.sleep(1)
            print("Battle Time!")
            time.sleep(1.5)

            while True:
                att = ohealth - damage
                ohealth -= damage
                line()
                print("You attack: opponent remaining health: "+str(att))
                time.sleep(.5)
                if att <= 0:
                    time.sleep(1.5)
                    line()
                    print("You won the fight!")
                    line()
                    input("Press <enter> to continue.")
                    line()
                    time.sleep(1)
                    w+=1
                    break
                deff = viata- odam
                viata -=odam
                line()
                sviata = 0
                sviata -= odam
                print("You defend: Your remaining HP:"+str(deff))
                time.sleep(.5)
                if viata <= 0:
                    time.sleep(1.5)
                    line()
                    print("You lost :(")
                    line()
                    input("Press <enter> to continue.")
                    l +=1
                    line()
                    time.sleep(1)
                    line()
                    break
        if w==3:
            time.sleep(1)
            w -= 3
            print("Felicitari, ai castigat toate cele trei luple!")
            line()
            r = input("You found a silver chest !, would you like to open it?(y/n)")
            line()
            if r == "y":
                input("Press <entrt> to open your chest!")
                line()
                time.sleep(1)
                nr = random.randint(1, 4)
                line()
                if nr == 1:
                    print("Ai Primit o sabie LVL 3!")
                    if "Sabie_LVL_3" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 20 bani pe acest item! ")
                        self.bani += 20
                    else:
                        self.items.append("Sabie_LVL_3")
                        self.damage += 30
                if nr == 2:
                    print("Ai primit armura LVL 3!")
                    if "Armura_LVL_3" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 20 bani pe acest item! ")
                        self.bani += 20
                    else:
                        self.items.append("Armura_LVL_3")
                        self.damage += 30
                if nr == 3:
                    print("Ai primit armura LVL 2!")
                    if "Armura_LVL_2" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 10 bani pe acest item! ")
                        self.bani += 10
                    else:
                        self.items.append("Armura_LVL_2")
                        self.hp += 20
                if nr == 4:
                    print("Ai primit sabie LVL 2!")
                    if "Sabie_LVL_2" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 10 bani pe acest item! ")
                        self.bani += 10
                    else:
                        self.items.append("Sabie_LVL_2")
                        self.hp += 20
                line()
                input("Apasa <enter> pentru a contunua!")
                line()


                print("Current stats:")
                print("HP: " + str(character.hp))
                print("Damage: " + str(character.damage))
                print("Items: " + str(character.items))
            time.sleep(1.5)
    def medium(self):
        print("Welcome to medium mode!")
        print("You will fight with 3 low characters! Good lock!")
        line()
        viata = self.hp
        damage= self.damage
        w = 0
        l = 0
        for i in range(1,4):
            if l== 1:
                break
            print("Opponent "+ str(i))
            d=[40, 50, 60]
            h= [60, 70, 80, 90, 100]
            odam = secrets.choice(d)
            ohealth = secrets.choice(h)
            print("HP: "+str(ohealth))
            print("Damage: "+str(odam))
            line()
            time.sleep(1)
            print("Battle Time!")
            time.sleep(1.5)

            while True:
                att = ohealth - damage
                ohealth -= damage
                line()
                print("You attack: opponent remaining health: "+str(att))
                time.sleep(.5)
                if att <= 0:
                    time.sleep(1.5)
                    line()
                    print("You won the fight!")
                    line()
                    input("Press <enter> to continue.")
                    line()
                    time.sleep(1)
                    w+=1
                    break
                deff = viata- odam
                viata -=odam
                line()
                sviata = 0
                sviata -= odam
                print("You defend: Your remaining HP:"+str(deff))
                time.sleep(.5)
                if viata <= 0:
                    time.sleep(1.5)
                    line()
                    print("You lost :(")
                    line()
                    input("Press <enter> to continue.")
                    l +=1
                    line()
                    time.sleep(1)
                    line()
                    break
        if w==3:
            time.sleep(1)
            w -= 3
            print("Felicitari, ai castigat toate cele trei luple!")
            line()
            r = input("You found a silver chest !, would you like to open it?(y/n)")
            line()
            if r == "y":
                input("Press <entrt> to open your chest!")
                line()
                time.sleep(1)
                nr = random.randint(1, 4)
                line()
                if nr == 1:
                    print("Ai Primit o sabie LVL 4!")
                    if "Sabie_LVL_4" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 30 bani pe acest item! ")
                        self.bani += 30
                    else:
                        self.items.append("Sabie_LVL_4")
                        self.damage += 40
                if nr == 2:
                    print("Ai primit armura LVL 4!")
                    if "Armura_LVL_4" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 30 bani pe acest item! ")
                        self.bani += 30
                    else:
                        self.items.append("Armura_LVL_4")
                        self.damage += 40
                if nr == 3:
                    print("Ai primit armura LVL 5!")
                    if "Armura_LVL_5" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 50 bani pe acest item! ")
                        self.bani += 50
                    else:
                        self.items.append("Armura_LVL_5")
                        self.hp += 50
                if nr == 4:
                    print("Ai primit 20 banutzi")
                    self.bani += 20
                line()
                input("Apasa <enter> pentru a contunua!")
                line()


                print("Current stats:")
                print("HP: " + str(character.hp))
                print("Damage: " + str(character.damage))
                print("Items: " + str(character.items))
            time.sleep(1.5)

    def hard(self):
        print("Welcome to hard mode!")
        print("You will fight with 3 low characters! Good lock!")
        line()
        viata = self.hp
        damage= self.damage
        w = 0
        l = 0
        for i in range(1,4):
            if l== 1:
                break
            print("Opponent "+ str(i))
            d=[60, 70, 80, 90]
            h= [90, 100, 110, 120, 130]
            odam = secrets.choice(d)
            ohealth = secrets.choice(h)
            print("HP: "+str(ohealth))
            print("Damage: "+str(odam))
            line()
            time.sleep(1)
            print("Battle Time!")
            time.sleep(1.5)

            while True:
                att = ohealth - damage
                ohealth -= damage
                line()
                print("You attack: opponent remaining health: "+str(att))
                time.sleep(.5)
                if att <= 0:
                    time.sleep(1.5)
                    line()
                    print("You won the fight!")
                    line()
                    input("Press <enter> to continue.")
                    line()
                    time.sleep(1)
                    w+=1
                    break
                deff = viata- odam
                viata -=odam
                line()
                sviata = 0
                sviata -= odam
                print("You defend: Your remaining HP:"+str(deff))
                time.sleep(.5)
                if viata <= 0:
                    time.sleep(1.5)
                    line()
                    print("You lost :(")
                    line()
                    input("Press <enter> to continue.")
                    l +=1
                    line()
                    time.sleep(1)
                    line()
                    break
        if w==3:
            time.sleep(1)
            w -= 3
            print("Felicitari, ai castigat toate cele trei luple!")
            line()
            r = input("You found a diamind chest !, would you like to open it?(y/n)")
            line()
            if r == "y":
                input("Press <entrt> to open your chest!")
                line()
                time.sleep(1)
                nr = random.randint(1, 4)
                line()
                if nr == 1:
                    print("Ai Primit o sabie LVL 10!")
                    if "Sabie_LVL_10" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 100 bani pe acest item! ")
                        self.bani += 100
                    else:
                        self.items.append("Sabie_LVL_10")
                        self.damage += 100
                if nr == 2:
                    print("Ai primit armura LVL 10!")
                    if "Armura_LVL_10" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 100 bani pe acest item! ")
                        self.bani += 100
                    else:
                        self.items.append("Armura_LVL_10")
                        self.damage += 100
                if nr == 3:
                    print("Ai primit armura LVL 7!")
                    if "Armura_LVL_7" in self.items:
                        print("Din pacate deja ai acest item :(")
                        print("Ti s-au oferit 60 bani pe acest item! ")
                        self.bani += 60
                    else:
                        self.items.append("Armura_LVL_7")
                        self.hp += 70
                if nr == 4:
                    print("Ai primit 69 banutzi")
                    self.bani += 69
                line()
                input("Apasa <enter> pentru a contunua!")
                line()


                print("Current stats:")
                print("HP: " + str(character.hp))
                print("Damage: " + str(character.damage))
                print("Items: " + str(character.items))
            time.sleep(1.5)


###############################################################################################################################################################
line()
print("Welcome To Battleleague")
line()

while True:
    rr = input("Do you already have an account? (y/n): ")
    if rr=="y":
        line()
        usr = input("Username: ")
        r = open("load.txt", "r")
        if usr in r:
            line()
            print("Succsesfully logged in as "+ usr)
            r.close()
            break
        else:
            print("Invalid Username!")
            continue
    else:
        rr = input("Username")
        w = open("load.txt", "a")
        w.write(str("\n"+rr))
        line()
        print("Succsesfully created an account!")
        w.close()
        break

time.sleep(.5)
line()
print("Character created!")
character = fiinta()
character.luptator()
character.boost()
time.sleep(1)
line()
print("Current stats:")
print("HP: " + str(character.hp))
print("Damage: "+ str(character.damage))
print("Bani: "+ str(int(character.bani)))
print("Items: "+ str(character.items))
line()
time.sleep(1)
character.default_chest()

while True:
    line()
    print("Meniu")
    r = input("""
PRESS 1 To play game!
PRESS 2 To see your stats
PRESS 3 For Shop
PRESS 4 To Save
PRESS 5 To quit
-------------------------------------------
    """)
    line()
    if r =="1":
        r = input("""
Choose your gamemode:
PRESS 1 For Easy
PRESS 2 For Medium
PRESS 3 For Hard
-------------------------------------------
        """)
        line()
        if r=="1":
            character.easy()
            line()

        elif r=="2":
                character.medium()
                line()
        elif r=="3":
            character.hard()
            line()
        else:
            print("ERROR: Invalid request")

    elif r=="4":
        rr = open("load.txt", "a")
        rr.write("\nHP: ")
        rr.write("\n"+ str(character.hp))
        rr.write("\nDamage: ")
        rr.write("\n"+ str(character.damage))
        rr.write("\nItems: ")
        rr.write("\n"+ str(character.items))
        rr.close()
    elif r =="2":
        line()
        print("Current stats:")
        print("HP: " + str(character.hp))
        print("Damage: "+ str(character.damage))
        print("Bani: " + str(int(character.bani)))
        print("Items: "+ str(character.items))

        line()
        input("Press <enter> to continue.")
        time.sleep(1)
    elif r=="3":
        line()
        print("Bine ai venit in magazin!")
        line()
        print("Ai: " + str(character.bani)+ " Bani")
        line()
        input("Press <enter> to continue.")
        line()
        sh = input("""
----------------------------------------
Produse valabile:
----------------------------------------
PRESS 1:  Armura LVL 1 ...... 1 Banutz
PRESS 2:  Armura LVL 2 ...... 20 Banutzi
PRESS 3:  Armura LVL 3 ...... 30 Banutzi
PRESS 4:  Armura LVL 4 ...... 40 Banutzi
PRESS 5:  Armura LVL 5 ...... 50 Banutzi
PRESS 6:  Armura LVL 6 ...... 60 Banutzi
----------------------------------------
PRESS 7:  Sabie LVL 1 ....... 1 Banutzi
PRESS 8:  Sabie LVL 2 ....... 20 Banutzi
PRESS 9:  Sabie LVL 3 ....... 30 Banutzi
PRESS 10: Sabie LVL 4 ....... 40 Banutzi
PRESS 11: Sabie LVL 5 ....... 50 Banutzi
PRESS 12: Sabie LVL 6 ....... 60 Banutzi
---------------------------------------- 
        """)
        if sh=="1":
            if character.bani < 10:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_1" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 1")
                character.items.append("Armura_LVL_1")
                character.hp += 10
                character.bani-=10
        elif sh=="2":
            if character.bani < 20:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_2" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 2")
                character.items.append("Armura_LVL_2")
                character.hp += 20
                character.bani-=20
        elif sh=="3":
            if character.bani < 30:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_3" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 3")
                character.items.append("Armura_LVL_3")
                character.hp += 30
                character.bani -= 30
        elif sh =="4":
            if character.bani < 40:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_4" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 4")
                character.items.append("Armura_LVL_1")
                character.hp += 40
                character.bani-=40

        elif sh == "5":
            if character.bani < 50:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_5" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 5")
                character.items.append("Armura_LVL_5")
                character.hp += 50
                character.bani-=50

        elif sh == "6":
            if character.bani < 60:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Armura_LVL_6" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Armura LVL 6")
                character.items.append("Armura_LVL_6")
                character.hp += 60
                character.bani-=60

        elif sh == "7":
            if character.bani < 10:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_1" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 1")
                character.items.append("Sabie_LVL_1")
                character.damage += 10
                character.bani-=10

        elif sh == "8":
            if character.bani < 20:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_1" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 2")
                character.items.append("Sabie_LVL_2")
                character.damage += 20
                character.bani-=20
        elif sh == "9":
            if character.bani < 30:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_3" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 3")
                character.items.append("Sabie_LVL_3")
                character.damage += 30
                character.bani-=30
        elif sh == "9":
            if character.bani < 40:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_4" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 4")
                character.items.append("Sabie_LVL_1")
                character.damage += 40
                character.bani-=40
        elif sh == "13":
            if character.bani < 50:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_5" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 5")
                character.items.append("Sabie_LVL_5")
                character.damage += 50
                character.bani-=50
        elif sh == "12":
            if character.bani < 60:
                print("ERROR: Nu ai destui bani!")
                input("Press <enter> to continue.")
                continue
            if "Sabie_LVL_6" in character.items:
                print("ERROR: Din pacate deja ai acest item :(")
            else:
                print("Felicitari! Ai cumparat o Sabie LVL 6")
                character.items.append("Sabie_LVL_6")
                character.damage += 60
                character.bani-=60
        else:
            "ERROR: Invalid request!"
        line()
        time.sleep(2)
    else:
        quit()

