k = ["yarik"]
s = ["parool123"]
def reg(k, s)->str:
    login = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    while True:
        if login not in k:
            k.append(login)
            s.append(parool)    
            break 
        else:
            return "Sellise nimega kasutaja on juba olemas"
    return "Registreerimine õnnestus"
def auth(k, s)->str:
    login = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if login in k:
        indeks = k.index(login)
        if s[indeks] == parool:
            return "Sisselogimine õnnestus"
    else:
        return "Vale kasutajanimi või parool"


def unustanud_parool(k, s) -> str:
    login = input("Sisesta kasutajanimi: ")
    if login in k:
        indeks = k.index(login)
        uus_parool = input("Sisesta uus parool: ")
        s[indeks] = uus_parool
        return "Parooli muutmine õnnestus"
    else:
        return "Kasutajat ei leitud"