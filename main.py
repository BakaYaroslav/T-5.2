from MyModule import *
while True:
    print("Vali tegevus:")
    print("1 - Registreeri kasutaja")
    print("2 - Autoriseerimine (Sisselogimine)")
    print("3 - Unustatud parooli taastamine")
    valik = input("Sisesta valik: ")
    if valik == "1":
        registreerimine = reg(k, s)
        print(registreerimine) 
        break
    elif valik == "2":
        autoriseerimine = auth(k, s)
        print(autoriseerimine)
        break
    elif valik == "3":
        parooli_taastamine = unustanud_parool(k, s)
        print(parooli_taastamine)
        break
    '''elif
        print("Vali tegevus:")
        print("1 - Nime või parooli muutmine")
        print("2 - Unustatud parooli taastamine")
        print("Lõpetamine (Väljumine)")
        sissevalik = input("Sisesta valik: ")
        if sissevalik == "1":'''


while True:
    print("3 - Nime või parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Lõpetamine (Väljumine)")

    if valik == "3":
        print("Nime või parooli muutmine")
    elif valik == "4":
        print("Unustatud parooli taastamine")
    elif valik == "5":
        print("Lõpetamine (Väljumine)")