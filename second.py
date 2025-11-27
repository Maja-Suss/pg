def cislo_text(cislo):
    try:
        n = int(cislo)
    except ValueError:
        return "Neplatný vstup (není číslo)"

    if not (0 <= n <= 100):
        return "Číslo je mimo povolený rozsah (0-100)"

    jednotky = {
        0: "nula", 1: "jedna", 2: "dvě", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }

    nact = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct",
        14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct",
        18: "osmnáct", 19: "devatenáct"
    }

    desitky = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát",
        6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
    }

    if 0 <= n <= 9:
        return jednotky[n]

    elif 10 <= n <= 19:
        return nact[n]

    elif 20 <= n <= 99:
        d = n // 10
        j = n % 10
        
        vysledek = desitky[d]
        
        if j > 0:
            vysledek += " " + jednotky[j]
            
        return vysledek

    elif n == 100:
        return "sto"

    return "Chyba"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)