import random
import string 
k = ["yarik"]
s = ["Yarik*123"]
UserParool = False
def reg(k, s)->str:
    while True:
        login = input("Sisesta kasutajanimi: ")
        if login not in k:
            k.append(login)
            break
        else:
            print("Sellise nimega kasutaja on juba olemas")
    while True:
        ask = input("kas te tahate generida parool? (jah/ei): ")
        if ask.lower() == "jah":
            randparool = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*[]-_+=', k=12))
            print(f"Teie genereeritud parool on: {randparool}")
            s.append(randparool)
            return "Registreerimine õnnestus"
        else:
            UserParool = True
            while UserParool:
                parool = input("Sisesta parool: ")
                if len(parool) < 8:
                    print ("Parool peab olema vähemalt 8 märki pikk")
                elif not any(char.isdigit() for char in parool):
                    print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
                elif not any(char.isupper() for char in parool):
                    print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
                elif not any(char in '!@#$%^&*()-_+=' for char in parool):
                    print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
                else:
                    print("Registreerimine õnnestus")
                    s.append(parool)    
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
        Ask = True
        while Ask:
            ask = input("kas te tahate generida parool? (jah/ei): ")
            if ask.lower() == "jah":
                randparool = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*[]-_+=', k=12))
                print(f"Teie genereeritud parool on: {randparool}")
                s.append(randparool)
                return
        uus_parool = input("Sisesta uus parool: ")
        if len(uus_parool) < 8:
            print ("Parool peab olema vähemalt 8 märki pikk")
        elif not any(char.isdigit() for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        elif not any(char.isupper() for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        elif not any(char in '!@#$€%^&*()-_+=/' for char in uus_parool):
            print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
        else:
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
        Ask = True
    while Ask:
        ask = input("kas te tahate generida parool? (jah/ei): ")
        if ask.lower() == "jah":
            randparool = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*[]-_+=', k=12))
            print(f"Teie genereeritud parool on: {randparool}")
            s.append(randparool)
            return
        else:
            break

    while True:
        
        if login in k and s[k.index(login)] == parool:
            indeks = k.index(login)
            uus_parool = input("siseta uus parool: ")
            if len(uus_parool) < 8:
                print ("Parool peab olema vähemalt 8 märki pikk")
            elif not any(char.isdigit() for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            elif not any(char.isupper() for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            elif not any(char in '!@#$€%^&*()-_+=/' for char in uus_parool):
                print("Parool peab sisaldama vähemalt ühte suurtähte, ühte numbrit ja ühte erimärki")
            else:
                s[indeks] = uus_parool
                print(f"parool muutmine õnnetus: {uus_parool}")
                break
        else: 
            print("Kasutajat või parool ei leitud")

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
        uus_parool = input("siseta uus parool: ")
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
            k[indeks] = uus_login
            s[indeks] = uus_parool
            print(f"kasutanimi muutmine õnnestus: {uus_login}; parool muutmine õnnestus: {uus_parool}")
            break