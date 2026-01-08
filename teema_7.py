def kirjuta_failisse(failinimi:str, loend:list):
    while True:
        reziim = input("mis reziimis soovite faili avada? (lisa - a, kirjuta - w): ").lower()
        if reziim not in ['a', 'w']:
            print("Vale reziim, kasutame kirjutamisreziimi (w)")
        else:
            break
    
    while True:
        element = input("Sisesta element, mida soovid faili lisada: (lõpeta - STOP) ").lower()
        loend.append(f"{element}")
        with open(failinimi+".txt", reziim, encoding='utf-8') as f:
            for rida in loend:
                f.write(rida+"\n")
        if element.upper() == "STOP":
            break
        # või for rida in loend: f.write(rida)

def loe_failist(failinimi:str):
    loend = []
    with open(failinimi+".txt", "r", encoding='utf-8') as f:
        for rida in f:
            loend.append(rida.strip())
    return loend


failinimi = input("Sisesta faili nimi: ")
loend = [""]
kirjuta_failisse(failinimi, loend)    
sisu = loe_failist(failinimi)
# 1 variant
print(sisu)
# 2 variant
for rida in sisu:
    print(rida)