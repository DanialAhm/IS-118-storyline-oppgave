
# IS-118 - Gruppeinnlevering 2

tillit = 0

print("Du er Erling, prosjektleder for kommunens nye digitale innbyggerportal.")
print("Etter seks uker begynner konfliktene i prosjektgruppen å vokse.")
print("Det er bare 3 uker igjen til prototypen skal leveres.")
print("Du må ta tre viktige beslutninger for å redde prosjektet.")


# BESLUTNING 1: SILJE OG ELIAS

print("\nSilje og Elias er uenige om teknologivalg og design.")
print("Silje mener Elias sitt valg begrenser brukervennligheten.")
print("Elias mener Siljes forslag er for dyrt og teknisk usikkert.")

print("\nHva gjør du som prosjektleder?")
print("1. Tar konflikten opp i plenum.")
print("2. Bruker dominans og bestemmer hvilken løsning teamet skal prioritere.")

valg1 = input("Velg 1 eller 2: ")

while valg1 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg1 = input("Velg 1 eller 2: ")

if valg1 == "1":
    print("\nDu samler teamet til et felles møte.")
    print("Silje og Elias får forklare sine synspunkter.")
    print("Teamet prøver å finne en løsning som ivaretar både sikkerhet og brukervennlighet.")
    tillit += 2
else:
    print("\nDu snakker med dem og bestemmer hvilken løsning som skal brukes.")
    print("Konflikten roer seg kanskje midlertidig, men begge er ikke nødvendigvis fornøyde.")
    tillit -= 1


# BESLUTNING 2: HAMDI OG HALLGEIR

print("\nHamdi ønsker en kontrollert kommunal plattform.")
print("Hallgeir ønsker en mer åpen løsning med dialog mellom innbyggerne.")
print("Uenigheten kan utvikle seg til en større konflikt.")

print("\nHva gjør du?")
print("1. Kaller inn til et møte for å finne et kompromiss.")
print("2. Avventer og lar dem prøve å løse uenigheten selv.")

valg2 = input("Velg 1 eller 2: ")

while valg2 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg2 = input("Velg 1 eller 2: ")

if valg2 == "1":
    print("\nDu arrangerer et møte mellom Hamdi og Hallgeir.")
    print("Begge får forklare hva de mener er viktig.")
    print("De forsøker å finne en løsning som kombinerer kontroll og åpenhet.")
    tillit += 2
else:
    print("\nDu velger å avvente.")
    print("Hamdi og Hallgeir får forsøke å løse problemet selv.")
    print("Samtidig øker frustrasjonen fordi konflikten ikke blir håndtert.")
    tillit -= 1


# BESLUTNING 3: MOTIVASJON I TEAMET

print("\nDet er tre uker igjen til prototypen skal leveres.")
print("Teamet er slitent, og konfliktene har påvirket motivasjonen.")

print("\nHva prioriterer du?")
print("1. Relasjonsbygging og tillit i teamet.")
print("2. Fremdrift, arbeidsoppgaver og tidsfrister.")

valg3 = input("Velg 1 eller 2: ")

while valg3 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg3 = input("Velg 1 eller 2: ")

if valg3 == "1":
    print("\nDu setter av tid til felles aktiviteter og møter.")
    print("Teamet lager felles spilleregler og jobber med å bygge tillit.")
    tillit += 2
else:
    print("\nDu lager en tydelig plan med arbeidsoppgaver og frister.")
    print("Teamet fokuserer på å få prototypen ferdig.")
    print("Relasjonene og konfliktene får mindre oppmerksomhet.")
    tillit -= 1


# AVSLUTNING: RESULTATET AV BESLUTNINGENE

print("\nTeamets tillitsscore er:", tillit)

if tillit >= 4:
    print("\nSLUTT 1: TEAMET NÅR NORMING-FASEN")
    print("Du har prioritert åpen kommunikasjon og relasjonsbygging.")
    print("Konfliktene blir håndtert, og teamet etablerer felles spilleregler.")
    print("Samarbeidet blir bedre, og prototypen leveres av et samlet team.")

elif tillit >= 1:
    print("\nSLUTT 2: KONFLIKTENE ER DELVIS LØST")
    print("Noen av konfliktene er håndtert, mens andre fortsatt skaper utfordringer.")
    print("Prototypen blir levert, men samarbeidet er fortsatt sårbart.")
    print("Det er en risiko for at konfliktene kommer tilbake.")

else:
    print("\nSLUTT 3: PROSJEKTET MISTER SAMHOLDET")
    print("Konfliktene har ikke blitt håndtert på en god måte.")
    print("Tillit og motivasjon i teamet blir svekket.")
    print("Samarbeidet bryter sammen, og prototypen blir forsinket.")   