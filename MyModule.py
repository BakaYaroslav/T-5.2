import random
import string 
k = ["yarik"]
s = ["Yarik*123"]
def reg(k, s)->str:
    while True:
        login = input("Sisesta kasutajanimi: ")
        uus_parool = input("Sisesta parool: ")
        if len(uus_parool) < 8:
            print ("Parool peab olema vähemalt 8 märki pikk")
        elif not any(char.isdigit() for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        elif not any(char.isupper() for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        elif not any(char in '!@#$€%^&*()-_+=/' for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        else:
            print("Muutmine õnnestus")
        if login not in k:
            k.append(login)
            print("Registreerimine õnnestus")
            break
        else:
            print("Sellise nimega kasutaja on juba olemas")
            s.append(uus_parool)    
            break 
           
def auth(k, s)->str:
    login = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if login in k:
        indeks = k.index(login)
        if s[indeks] == parool:
            return "Sisselogimine õnnestus"
    else:
        print("Vale kasutajanimi või parool")


def unustanud_parool(k, s):
    while True:
        login = input("Sisesta kasutajanimi: ")
        uus_parool = randparool(s)
       
        if login in k:
            indeks = k.index(login)
            s[indeks] = uus_parool
            return "Parooli muutmine õnnestus"
        else:
            print("Kasutajat ei leitud")
    
def muuda_login(k, s):
    while True:  
        login = input('sisesta vana login: ')
        parool = input("sisesta parool: ")   
            
        if login in k and s[k.index(login)] == parool:
            indeks = k.index(login)
            uus_login = input("sisesta uus login: ")
            k[indeks] = uus_login
            print(f"kasutajanimi muutmine õnnestus: {uus_login}")
            break
        else: 
            print("Kasutajat või parool ei leitud")
def muuda_parool(k, s):
    login = input('sisesta login: ')
    parool = input("sisesta parool: ")
    if login in k and s[k.index(login)] == parool:
        indeks = k.index(login)
    

    while muuda_parool:
        if login in k and s[k.index(login)] == parool:
            indeks = k.index(login)
            uus_parool = randparool(s)
            
            s[indeks] = uus_parool
            print(f"parool muutmine õnnetus: {uus_parool}")
            break
        else: 
            print("Kasutajat või parool ei leitud")
            break

def muuda_login_parool(k, s):           
    index = True
    while index:
        login = input('sisesta vana login: ')
        parool = input("sisesta parool: ")
        if login in k and s[k.index(login)] == parool:
            indeks = k.index(login)
            index = False
        else: 
            print("Kasutajat või parool ei leitud")
    while True:
        uus_login = input("siseta uus login: ")
        uus_parool = randparool(s)
        
        k[indeks] = uus_login
        s[indeks] = uus_parool
        print(f"kasutanimi muutmine õnnestus: {uus_login}; parool muutmine õnnestus: {uus_parool}")
        break
    return k, s

def randparool(s):
    Ask = True
    while Ask:
        ask = input("kas te tahate generida parool? (jah/ei): ")
        if ask.lower() == "jah":
            randparool = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*[]-_+=', k=12))
            print(f"Teie genereeritud parool on: {randparool}")
            s.append(randparool)
            return s
        else:
            uus_parool = input("Sisesta parool: ")
            if len(uus_parool) < 8:
                print ("Parool peab olema vähemalt 8 märki pikk")
            elif not any(char.isdigit() for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            elif not any(char.isupper() for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            elif not any(char in '!@#$€%^&*()-_+=/' for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            else:
                print("Muutmine õnnestus")
            return uus_parool