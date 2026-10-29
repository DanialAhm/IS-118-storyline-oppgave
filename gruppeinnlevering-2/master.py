#Prosjektleder Erling - interaktiv historie medborgerportalen

poeng = 0

#--- INTRO ---
print("Dere er kommet i en vanskelig fase")
print("Det er konflikter i teamet og prototypen skal snart leveres")
print("du er prosjektleder Erling og må ta tre valg for videreutvikling av teamet")

#---- VALG 1 ---
print("--------------------------------------------")
print ("konflikt silje vs elias angående teknologi og design")
print(" A tar det opp i plenum")
print(" B individuelle samtaler")

valg1 = input ("skriv A eller B: ")

if valg1 == "A" or valg1== "a":
    print("åpenhet, men risiko for eskalering")
    poeng = poeng + 1
    print("du fikk", poeng, "poeng")

elif valg1 == "B" or valg1== "b":
    print("demper, men konflikten ulmer videre")
    print("du fikk", poeng, "poeng")
else: 
    print("ugyldig svar velg A eller B")
print("")

#--- VALG 2 ---
print("--------------------------------------------")
print("konflikt hamdi vil ha kontroll halgeir vil ha åpenhet")
print("A) felles avklaringsmøte")
print("B) avventer")
valg2 = input ("skriv A eller B: ")

if valg2 == "A" or valg2 == "a":
    print("proaktivt, kan blusse opp")
    poeng = poeng + 1
    print("du fikk", poeng, "poeng")
elif valg2 == "B" or valg2== "b": 
    print("sparer tid, fare for eskalering")
    print("du fikk", poeng, "poeng")
else:
    print("ugyldig svar velg A eller B")
print("")

#--- VALG 3 ---
print("--------------------------------------------")
print("hvordan bevarer du motivasjon i teamet?")
print("A) relasjonsbygging / sosial tid")
print ("B) prioriterer fremdrift")
valg3 = input ("skriv A eller B: ")

if valg3 == "A" or "a":
    print("bygger tillit, men koster tid")
    poeng = poeng + 1
    print("du fikk", poeng, "poeng")
elif valg3 == "B" or "b": 
    print("holder milepæl, men svekker tillit")
    print("du fikk", poeng, "poeng")
else:
    print ("ugyldig svar velg A eller B")
print("")

#--- SLUTT ---
print("--------------------------------------------")
print("du fikk", poeng, "poeng")

if poeng == 3:
    print("NORMING: teamet gjenoppbygget tillit")
elif poeng == 2:
    print("delvis løst, samarbeidet fortsatt sårbart")
else:
    print("FORSINKELSE: teamet mister samhold og prototypen forsinkes")