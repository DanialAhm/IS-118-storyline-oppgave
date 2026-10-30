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

print(" 1. Blande inn HR, siden Elias og Silje ikke inngår kompromiss. Erlend kan ikke bruke tid på slike problemer!")
print(" 2. Ta individuelle samtaler med Silje og Elias, og ønske at de må skjerpe seg og fokusere på å finne en løsning sammen!")
valg1= input("velg 1 eller 2:")

while valg1 != "1" and valg1 != "2":
    print("ugyldig valg. Velg 1 eller 2: ")
    valg1 = input("velg 1 eller 2: ")

if valg1 == "1":
    print("HR ordner dette på en fin måte, men Elias og Silje føler at Erlend bare bryr seg om prosjektet og ikke om det problemet de har:)")
    print("Erlend får tid til å fokusere på prototypen istedet for konflikten")
    poeng += 1
 
else:
    print("Erlend tar individuelle samtaler. Elias og Silje skjønner at de må skjerpe seg og fokusere på andre ting som er vikitg!")
    print("Konflikten blir skyvet vekk, men den kan fyre opp igjen når som helst")

#--- Det 2. valget - Hamdi og Hallgeir 
print("Beslutning nr 2. (Hamdi og hallgeir)")
print("Diskusjonen mellom Hamdi og Hallgeir blir stadig mer intens.")
print("Hamdi ønsker en kontrollert løsning og Hallgeir ønsker en dialogbasert løsning.")

print("Det oppstår en spennig. Hva velger du å gjøre?")

print(" 1. Erlend presentere et vinnervalg for Hamdi og Hallgeir. De må konkurrere om hvem sin løsning som vinner!!")
print(" 2. Siden dette bare er en diskusjon, kan Erlend ignorere dette og heller fokusere på fremdrift!!")
valg2 = input("velg 1 eller 2: ")
while valg2 != "1" and valg2 != "2":
    print("ugyldig valg. Velg 1 eller 2: ")
    valg2 = input("velg 1 eller 2: ")

if valg2 == "1":
    print(" Hamdi tar valget fordi hun vant!, Yaaay!!")
    print(" Hallgeir er bitter, men skjønner at vinneren er vinnerene til slutt og sist!")
    poeng += 1

else:
    print("situasjonen blir ikke grripet inn i")
    print("Hamdi og Erlend bærer nag mot hverandre, men Erlend får i hvertfall gjort fremdrift i prototypen! ")

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
    print("Erling lager tydelige oppgaver med struktur og frister, og alle følger dem!")
    print("Teamet får levert prototypen, men konfliktene kan komme tilbake i mer kristiske faser")
    poeng += 1

else:
    print("Her prioriteres teamets trivsel og relasjoner, med fokus på sosiale aktiviteter og møtepunkter")
    print("Teamet får bedre relasjoner, men det blir kritisk med tidsfristen for prototypen!")


# --- Mulige utfall med poengsum ---
print("--- Utfall ---")

if poeng == 3:
    print("Gratulerer, teamet har gått over til Normingsfasen!")

elif poeng >= 1:
    print("Prototypen blir levert, men teamets samhold og relasjoner står ikke godt til:(")

else:
    print("Fristen for protoypen går ut og konflikter blir mer seriøse")
    print("Teamet kommer ikke forbi stormingsfasen:(")
print("du fikk", poeng, "poeng!")