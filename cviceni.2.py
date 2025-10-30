def prace_se_seznamem():

    seznam = [100, 5, 3, 21]
    print(seznam)
    
    seznam[2] *= 2
    print(seznam)
   
    seznam.append(55)
    print(seznam)
   
    seznam.sort()
    print(seznam)
   
    seznam.reverse()
    print(seznam)
    
    
def vrat_treti_prvek(seznam):
    if len(seznam) >= 3:
    return seznam[2]
else:
    return None

def prumer(cisla):
    return sum(cisla) / len(cisla)

def naformatuj_text(zak):
    return "student: Marie Süssová, Vek: 20, Obor: AEFP, Prumer: 1.8"



if __name__ == "__main__":

   
    student = (
       "jmeno": "Marie",
       "prijmeni": "Süssová",
       "vek": 20,
       "znamky": [1,2,1,2,3,1]
   )
   student["vek"] +=1
   student["obor"] = "AEFP"
   print (naformatuj_text(student))