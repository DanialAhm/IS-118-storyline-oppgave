# - Erling og konfliktene i prosjektteamet

poeng = 0
# --- Introduksjon ---
print("Det har gått seks uker og teamet går gjennom en stormingsfase!")

print("Konflikter er tilstede og prototypen skal leveres under 3 uker.")
print("Du er prosjektleder Erling og du må ta beslutninger som påvirker teamets fremtid.")

# det 1. valget - Silje og Elias 
print("Silje mener Elias sitt teknologivalg stopper brukeropplevelsen.")
print("Elias mener Silje sitt designvalg er kostbart og urealistisk.")
print("Diskusjonen har blitt personlig, hva gjør du?")

print(" 1. Ta konflikten opp i plenum!")
print(" 2. Ta individuelle samtaler med Silje og Elias, men ta den endelige beslutningen selv!")
valg1= input("velg 1 eller 2:")

while valg1 != "1" and valg1 != "2":
    print("ugyldig valg. Velg 1 eller 2: ")
    valg1 = input("velg 1 eller 2: ")

if valg1 == "1":
    print("Elias og Silje deler sine meninger på en åpen måte:)")
    print("Teamet får en bedre forståelse for hverandres perspektiv, men konflikten kan eskalere..")
    poeng += 1
 
else:
    print("Erling tar en beslutning som teamet ikke er enige i, men prosjektet går videre!")
    print("Elias og Silje er fortsetter å bære nag mot hverandre og betro seg til sine nærmeste")

#--- Det 2. valget - Hamdi og Hallgeir 
print("Beslutning nr 2. (Hamdi og hallgeir)")
print("Diskusjonen mellom Hamdi og Hallgeir blir stadig mer intens.")
print("Hamdi ønsker en kontrollert løsning og Hallgeir ønsker en dialogbasert løsning.")

print("Det oppstår en spennig. Hva velger du å gjøre?")

print(" 1. Kalle inn til et møte for å komme frem til en felles løsning")
print(" 2. Avvente med å gripe inn og håpe at de finner en løsning selv")
valg2 = input("velg 1 eller 2: ")
while valg2 != "1" and valg2 != "2":
    print("ugyldig valg. Velg 1 eller 2: ")
    valg2 = input("velg 1 eller 2: ")

if valg2 == "1":
    print(" Møtet gir Hamdi og Hallgeir til å finne en felles løsning!")
    print("Møtet bruker tid som kunne blitt brukt på prototypen, men uenigheten dempes")
    poeng += 1

else:
    print("situasjonen blir ikke grripet inn i")
    print("Det er fortsatt spenning mellom Hamdi og Hallgeir,men prosjektet fortsetter")

#--- Det 3. valget: hvordan bevare motivasjonen i teamet? ---
print("Hva kan du gjøre for å bevare motivasjonen i teamet!")
print("Her skal du velge hvilken strategi du vil bruke for å bevare motivasjonen i teamet etter en intens periode med konflikter")
print(" 1. Prioritere fremdrift i prosjektet og fokusere på leveranse!")
print(" 2. prioritere teamets trivsel og relasjoner")
valg3 = input("velg 1 eller 2:")
while valg3 != "1" and valg3 != "2":
    print("ugyldig valg. Velg 1 eller 2: ")
    valg3 = input("velg 1 eller 2: ")

if valg3 == "1":
    print("Erling lager tydelige oppgaver med struktur og frister")
    print("Teamet får levert prototypen, men konfliktene kan komme tilbake i mer kristiske faser")
    poeng += 1

else:
    print("Her prioriteres teamets trivsel og relasjoner, med fokus på sosiale aktiviteter og møtepunkter")
    print("Teamet får bedre relasjoner, men det blir kritisk med tidsfristen for prototypeb2")


# --- Mulige utfall med poengsum ---
print("--- Utfall ---")

if poeng == 3:
    print("Gratulerer, teamet har gått over til Normingsfasen!")

elif poeng >= 1:
    print("Prototypen blir levert, men teamets samhold og relasjoner står ikke godt til:(")

else:
    print("Fristen for protoypen går ut og konflikter blir mer seriøse")
    print("Teamet kommer ikke forbi stormingsfasen:(")