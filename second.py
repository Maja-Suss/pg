def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tri", "čtyři", "pet", "sest", "sedm", "osm", "devět"]
    desitky = ["deset", "dvacet", "tricet", "čtyřicet", "padesát", "sedesát", "sedmdesát", "osmdesát", "devadesát"]

    teen = ["deset", "jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devatenact"]
    

    if cislo < 0 or cislo > 100:
       return "cislo musi byt v rozsahu 0-100."
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return  teen[cislo - 10]
    elif cislo < 100:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
         return desitky[d]
        else:
            return desitky[d] + " " + jednotky[j]
    else:
        return "sto"


if __name__ == "__main__":
    cislo_text = "nula"(0)
    print("nula")