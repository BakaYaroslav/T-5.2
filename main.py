from MyModule import *
while True:
    print(k, s)
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
        print("mida te tahate muudata : 1 - login ; 2 - parool ; 3 - login ja parool")
        muda_valik = input("Sisesta valik: ")
        if muda_valik == '1' :
            log = muuda_login(k, s)
            break
        elif muda_valik == '2':
            par = muuda_parool(k, s)
            break
        elif muda_valik == '3':
            k, s = muuda_login_parool(k, s) 
            break
    elif valik == "5":
        print("Lõpetamine (Väljumine)")
        break