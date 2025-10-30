import math

def je_prvocislo(cislo):
    try:
        n = int(cislo)
    except ValueError:
        return False
        
    if n <= 1:
        return False
        
    if n % 2 == 0:
        return n == 2
        
    limit = int(math.sqrt(n))
    
    for delitel in range(3, limit + 1, 2):
        if n % delitel == 0:
            return False
            
    return True

def vrat_prvocisla(maximum):
    prvocisla = []
    
    try:
        max_num = int(maximum)
    except ValueError:
        return []

    for cislo in range(1, max_num + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla

if __name__ == "__main__":
    while True:
        cislo = input("Zadej maximum: ")
        
        try:
            int(cislo)
            break
        except ValueError:
            print("Neplatný vstup. Zadejte prosím celé číslo.")

    prvocisla = vrat_prvocisla(cislo)
    
    print(prvocisla)

def vrat_prvocisla(maximum):
    prvocisla = []
    
    try:
        max_num = int(maximum)
    except ValueError:
        return []

    for cislo in range(1, max_num + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla

if __name__ == "__main__":
    while True:
        cislo = input("Zadej maximum: ")
        
        try:
            int(cislo)
            break
        except ValueError:
            print("Neplatný vstup. Zadejte prosím celé číslo.")

    prvocisla = vrat_prvocisla(cislo)
    
    print(prvocisla)