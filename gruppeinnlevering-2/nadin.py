# IS-118 Gruppe innlevering
# Erlings team er i storming-fasen 


poeng = 0
# --- introduksjon ---
print("===========================")
print("Velkomen til Erlings team")
print("============================")
print("Teamet er i storming-fasen")
print("Erling er prosjektleder for en digital portal.")
print("Etter seks uker går teamet inn i storming-fasen.")
print(" Du må ta gode valg for å hjelpe teamet videre.")
print("")

# --- VALG 1 ---
print("Konflikt 1:")
print("Silje og Elias har en konflikt")
print("Silje mener løsningen er ikke brukervennlig")
print("Elias mener forslaget er for dyrt")
print("")

print("A: Ingorere konflikten")
print("B: Ha individuelle samtaler og deretter et felles møte")

Valg1 = input("Velg A eller B: ")

if Valg1 == "A" or Valg1 == "a":
    print("Risiko: Konflikten vokser, samarbeidet svekkes og prosjektet kan bli forsinket.")
    poeng = poeng + 1
    print("Du fikk", poeng, "poeng") 

elif "valg1" == "B" or Valg1 == "b":
    print("Erling tar individuelle samtaler og holder deretter et felles møte.")
    print("Dette kan bidra til bedre samarbeid i teamet.")
    poeng = poeng + 2
    print("Du fikk", poeng, "poeng")

else:
    print("Ugyldig svar. Velg A eller B")

print("")


# --- Valg 2 ---
print("Konflikt 2: Hamdi og Hallgeir")
print("Hamdi ønsker kommunal kontroll over plattformen.")
print("Hallgeir ønsker et mer åpent system.")
print("")

print("A: Velge én av sidene")
print("B: Kombinere begge forslagene")

valg2 = input("Velg A eller B: ")

if valg2 == "A" or valg 2 == "a":
    print("Den ene parten blir fornøyd, men den andre føler seg overkjørt.")
    poeng = poeng + 1
    print("Du fikk" , poeng, "poeng")

elif valg2 == "B" or valg 2 == "b":
    print("Kommunen beholder kontrollen.")
    print("Brukerne får gi tilbakemeldinger gjennom en offisiell kanal.")
    poeng = poeng + 2
    print("Du fikk", poeng, "poeng")

else:
    print("Ugyldig svar. Velg A eller B")

print("")

# Teamets motivasjon
print("Konflikt 3: Teamets motivasjon")
print("Teamet er stresset før prototypen skal være klar.")
print("")

print("A: Fokusere bare på arbeidet")
print("B: Arrangere team building og lage milepæler")

valg 3 = input("Velg A eller B: ")

if valg 3 == "A" or valg 3 == "a":
    print("Arbeidet fortsetter, men motivasjonen synker.")
    poeng = poeng + 1
    print("Du fikk", poeng, "poeng")

elif valg 3 == "B" or valg 3 == "b":
    print("Teamet blir mer motivert og samarbeider bedre.")
    poeng = poeng + 2
    print("Du fikk", poeng, "poeng")

else:
    print("Ugyldig svar. Velg A eller B") 

# --- Avslutning ---
print("Sluttresultat") 
print("Totalt antall poeng:", poeng)

if poeng >= 5:
    print("Positiv slutt:")
    print("Teamet løser konfliktene og går videre til norming-fasen.")
else:
    print("Negativ slutt:")
    print("Teamet sliter fortsatt med konflikter og samarbeidsproblemer.")
