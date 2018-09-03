T = int(input("adjon meg egy evszamot:"))
if T%1 == 0:
    if 1799<T and T<2100:
        A = T%29
        B = T%4
        C = T%7
        D = (19*A + 24)%30
        E = (2*B + 4*C + 6*D + 5)%7
        if E==6 and D==29:
            H = 50
        elif E==6 and D==28 and A>10:
            H = 49
        else:
            H = 22+D+E
        if H <= 31:
            print ("Marcius") and print(H)
        else:
            print ("Aprilis") and print (H-31)
    else:
        print ("Rossz evszamot adott meg. Az evszamnak 1800 és 2099 kozott kell lennie!")
else:
    print ("Nem egesz szamot adtal meg. Evszam csak egesz szam lehet!")
