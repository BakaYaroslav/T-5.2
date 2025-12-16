k = ["yarik"]
s = ["Yarik*123"]
def reg(k, s)->str:
    while True:
        login = input("Sisesta kasutajanimi: ")
        if login not in k:
            k.append(login)
            break
        else:
            print("Sellise nimega kasutaja on juba olemas")
    while True:
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
            s.append(parool)    
            break 
           
        return "Registreerimine õnnestus"
def auth(k, s)->str:
    login = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if login in k:
        indeks = k.index(login)
        if s[indeks] == parool:
            return "Sisselogimine õnnestus"
    else:
        print("Vale kasutajanimi või parool")


def unustanud_parool(k, s) -> str:
    while True:
        login = input("Sisesta kasutajanimi: ")
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
    
def muuda_andmeid(k, s) -> str:
    Valik2 = True
    while Valik2:
        ask = input("mida sa tahad muutuda '1 - login' , ' 2 - parool' , '3 - login ja parool': ")
        if ask == '1':
            login = input('sisesta vana login: ')
            parool = input("sisesta parool: ")   
              
            if login in k and s[k.index(login)] == parool:
                indeks = k.index(login)
                uus_login = input("sisesta uus login: ")
                k[indeks] = uus_login
                print(f"kasutajanimi muutmine õnnestus:{uus_login}")
                return
            else: 
                print("Kasutajat või parool ei leitud")
            
        elif ask == '2':
            login = input('sisesta login: ')
            parool = input("sisesta parool: ")
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
                        return
                else: 
                    print("Kasutajat või parool ei leitud")
            
        elif ask == '3':
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
                    k[indeks] = uus_login
                    s[indeks] = uus_parool
                    print(f"parool muutmine õnnestus: {uus_parool}; kasutanimi muutmine õnnestus: {uus_login}")
                    return
                

        else:
            print("vali '1, 2, 3': ")