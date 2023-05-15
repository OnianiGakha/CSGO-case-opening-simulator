import random
import time

gamma2 = ["CZ75-Auto | Imprint:Blue", "Negev | Dazzle:Blue", "UMP-45 | Briefing:Blue", "G3SG1 | Ventilator:Blue" , "Five-SeveN | Scumbria:Blue", "XM1014 | Slipstream:Blue", "P90 | Grim:Blue", "SCAR-20 | Powercore:Purple", "SG 553 | Triarch:Purple", "MAG-7 | Petroglyph:Purple", "Glock-18 | Weasel:Purple", "Desert Eagle | Directive:Purple", "MP9 | Airlock:Pink", "AUG | Syd Mead:Pink", "Tec-9 | Fuel Injector:Pink", "FAMAS | Roll Cage:Red", "AK-47 | Neon Revolution:Red", "Knife:Gold"] #the case and its contents with the rarity being after ":"

#settings thing

displayinconsole = True
writeintextfile = True



def opencase(case):
    stattrak = False
    if case == "gamma2": #sorts all cases contents into diffrent rarities
        Blue = []
        Purple = []
        Pink = []
        Red = []
        Gold = []
        for index in gamma2:
            rarity = index.split(":")[1]
            item = index.split(":")[0]
            eval(rarity).append(item)
        
    
    chosennum = random.randrange(0,10000) #random number for the rarity of the item (basically like %100.00)
    chosenitem = ""
    chosenrarity = ""
    floatval = ""
    float = random.triangular(0, 1, 0.196) #tried to make a bellcurve type thing like it is in csgo to find the float of the gun
    
    if float >= 0.45: #finds the wear depending on the float
        floatval = "Battle-Scarred"
    elif float >= 0.38:
        floatval = "Well-Worn"
    elif float >= 0.15:
        floatval = "Field-Tested"
    elif float >= 0.7:
        floatval = "Minimal Wear"
    else:
        floatval = "Factory New"

    if chosennum<25: #finds rarity of number depending on the chosennum
        chosenrarity = "Gold"
    elif chosennum<64:
        chosenrarity = "Red"
    elif chosennum<319:
        chosenrarity = "Pink"
    elif chosennum<1600:
        chosenrarity = "Purple"
    else:
        chosenrarity = "Blue"
    
    chosenitem = random.choice(eval(chosenrarity)) #gets random item with the chosen rarity in the case
    stat = ""
    if random.randrange(0,10) == 1: #10% chance of the gun being StatTrak
        stattrak = True
        stat = "StatTrak™ "
    
    fullname = stat + chosenitem + "\n" + chosenrarity + "\n\n" + "Float: " + str(float) + "\n" + "Wear: " + floatval #lays out the information for printing

    if writeintextfile == True:
        inventory = open("inventory.txt","a")
        inventory.write(fullname + "\n--------------------------\n")
        

    if displayinconsole == True:
        print(fullname + "\n\n")


        
        #print(b), print(p), print(pi), print(r), print(g)



            



while True:
    inputlol = input("type 'open' to open a skin, type 'clear' to clear inventory and 'settings' to go into settings : ")

    if inputlol == "open":

        

        print("Choose a case: gamma2")
        casechosen = input("")
        while True:
            opencase(casechosen)

            

            ansr = input("open another one (1) or go back (2): ")

            if ansr == "2":
                break
    
    if inputlol == 'clear':
        open("inventory.txt","r+").truncate(0)

    if inputlol == 'settings':
        print("type which option you wanna set to 'true' or 'false' or set the number to:\ndisplay the item opened in console (1) is currently: " + str(displayinconsole) + "\nadd the items to inventory(2) is currently: " + str(writeintextfile))

        lol = input()
        thesetting = lol.split(" ")
        if thesetting[0] == "1":
            if thesetting[1] == "false":
                displayinconsole = False
            else:
                displayinconsole = True
        if thesetting[0] == "2":
            if thesetting[1] == "false":
                writeintextfile = False
            else:
                writeintextfile = True        
