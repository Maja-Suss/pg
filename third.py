import math

def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    
    if cislo == 2:
        return True

    if cislo % 2 == 0:
        return False
    
    limit = int(math.sqrt(cislo))
    
    for i in range(3, limit + 1, 2):
        if cislo % i == 0:
            return False
            
    return True


def vrat_prvocisla(maximum):
    try:
        max_cislo = int(maximum)
    except ValueError:
        return "Chyba: Zadaný vstup není platné číslo."
        
    seznam_prvocisel = []
    
    for i in range(1, max_cislo + 1):
        if je_prvocislo(i):
            seznam_prvocisel.append(i)
            
    return seznam_prvocisel


if __name__ == "__main__":
    
    cislo_vstup = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo_vstup)
    
    
    print(f"vrat_prvocisla(1): {vrat_prvocisla(1)}")
    print(f"vrat_prvocisla(2): {vrat_prvocisla(2)}")
    print(f"vrat_prvocisla(3): {vrat_prvocisla(3)}")
    print(f"vrat_prvocisla(10): {vrat_prvocisla(10)}")
    
    print(f"\nPrvočísla do {cislo_vstup}: {prvocisla}")