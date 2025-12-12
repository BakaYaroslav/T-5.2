k = ["yarik"]
s = ["123"]
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
    
def muuda_andmeid(k, s) -> str:
    while True:
        ask = input("mida sa tahad muutuda '1 - login' , ' 2 - parool' , '3 - login ja parool': ")
        if ask == '1':
            login = input('sisesta vana login: ')
            parool = input("sisesta parool: ")   
              
            if login in k and s[k.index(login)] == parool:
                indeks = k.index(login)
                uus_login = input("sisesta uus login: ")
                k[indeks] = uus_login
                return f"kasutajanimi muutmine õnnestus:{uus_login}"
            else: 
                return "Kasutajat või parool ei leitud"
        elif ask == '2':
            login = input('sisesta vana login: ')
            parool = input("sisesta parool: ")
            
            if login in k and s[k.index(login)] == parool:
                indeks = k.index(login)
                uus_parool = input("siseta uus parool: ")
                s[indeks] = uus_parool
                return f"parool muutmine õnnetus: {uus_parool}"
            else: 
                return "Kasutajat või parool ei leitud"
        elif ask == '3':
            login = input('sisesta vana login: ')
            parool = input("sisesta parool: ")
            
            if login in k and s[k.index(login)] == parool:
                indeks = k.index(login)
                uus_login = input("siseta uus login: ")
                uus_parool = input("siseta uus parool: ")
                k[indeks] = uus_login
                s[indeks] = uus_parool
                return f"parool muutmine õnnestus: {uus_parool}; kasutanimi muutmine õnnestus: {uus_login}"
            else: 
                print("Kasutajat või parool ei leitud")
        else:
            print("vali '1, 2, 3': ")