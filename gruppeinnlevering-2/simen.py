# IS-118 - Gruppeinnlevering 2
# Interaktiv historie: Erling og medborgerportalen

print ("Velkommen til Erling og medborgerportalen") 
print ("Du er Erling, prosjektleder, og dine valg påvirker teamets framtid") 
print ("Teamet er nå i en storming-fase, og prototypen skal leveres om tre uker")

poeng = 0

#beslutningspunkt 1: Elias og Silje sin konflikt
print ("BESLUTNING 1 - Elias og Silje")
print ("Elias og Silje er uenig om design og teknisk sikkerhet")
print("1: Ta konflikten opp i plenum og forsøke å finne en felles løsning.")
print("2: Snakke med dem hver for seg og deretter bestemme løsningen selv.")
valg1 = input("Hva velger du? (1/2): ")
while valg1 != "1" and valg1 != "2":
    valg1 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg1 == "1":
    print("\nBegge får forklare sine synspunkter. De forstår hverandre bedre,")
    print("men møtet tar tid fra prototypearbeidet.\n")
    poeng += 1
else:
    print("\nErling bestemmer raskt hvilken løsning som skal brukes.")
    print("Prosjektet går videre, men misnøyen mellom Silje og Elias består.\n")

#Beslutningspunkt 2: Uenigheten mellom Hamdi og Hallgeir
print("BESLUTNING 2 - HAMDI OG HALLGEIR")
print("Hamdi ønsker kontroll over digitale folkemøter, mens Hallgeir ønsker åpen dialog.")
print("1: Arrangere et møte for å finne et kompromiss.")
print("2: Avvente og håpe at de finner en løsning selv.")
valg2 = input("Hva velger du? (1/2): ")
while valg2 != "1" and valg2 != "2":
    valg2 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg2 == "1":
    print("\nHamdi og Hallgeir diskuterer et kompromiss.")
    print("Uenigheten dempes, men møtet bruker verdifull tid.\n")
    poeng += 1
else:
    print("\nErling griper ikke inn, slik at arbeidet med prototypen fortsetter.")
    print("Frustrasjonen mellom Hamdi og Hallgeir vokser.\n")

#Beslutningspunkt 3: Motivasjon i teamet
print("BESLUTNING 3 - TEAMETS MOTIVASJON")
print("Erling må velge hvordan han vil lede teamet frem mot prototypen.")
print("1: Prioritere relasjonsbygging, felles spilleregler og tillit.")
print("2: Prioritere fremdrift med tydelige oppgaver og frister.")
valg3 = input("Hva velger du? (1/2): ")
while valg3 != "1" and valg3 != "2":
    valg3 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg3 == "1":
    print("\nTeamet bruker tid på å bygge tillit og etablere felles spilleregler.")
    print("Samarbeidet bedres, men det blir mindre tid til prototypen.\n")
    poeng += 1
else:
    print("\nErling lager en tydelig plan med oppgaver og frister.")
    print("Arbeidet får struktur, men de uløste konfliktene kan svekke motivasjonen.\n")

#Avslutningen bygger på summen av de tre valgene
print("RESULTAT")
if poeng == 3:
    print("Teamet gjenoppretter tilliten og går videre til norming-fasen.")
    print("Uenighetene håndteres konstruktivt, og prototypen leveres av et samlet team.")
elif poeng >= 1:
    print("Konfliktene blir delvis løst, men relasjonene er fortsatt sårbare.")
    print("Prototypen blir levert, men nye uenigheter kan fortsatt oppstå.")
else:
    print("Konfliktene forverres, og samholdet i prosjektteamet svekkes.")
    print("Teamet blir værende i storming-fasen, og prototypen blir forsinket.")

print("\nTakk for at du spilte!")