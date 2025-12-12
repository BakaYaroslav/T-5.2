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

while True:
    print("4 - Nime või parooli muutmine")
    print("5 - Lõpetamine (Väljumine)")
    valik = input("Sisesta valik: ")
    if valik == "4":
        muutumine = muuda_andmeid(k, s)
        break
    elif valik == "5":
        print("Lõpetamine (Väljumine)")
        break