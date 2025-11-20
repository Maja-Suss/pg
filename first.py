 
def sudy_nebo_lichy(cislo):
    if cislo % 2:
        return "liche"
    else:
        return "sude"

def main():
    promena = 1
    vysledek = sudy_nebo_lichy(promena)
    print(vysledek)

if __name__ == "__main__":
    main()
