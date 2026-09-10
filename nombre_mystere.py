import random

nombre_secret=random.randint(1,100)
max_tenatives=7
tentatives=0
proposition=0
print("je pense a un nombre entre 1 et 100, devine lequel!")

while proposition!=nombre_secret and tentatives<max_tenatives:
    try:
        proposition=int(input("entrez votre proposition:"))
        tentatives=tentatives + 1
        if proposition<nombre_secret:
         print("C'est plus")
        elif proposition>nombre_secret:
         print("C'est moins")
        else:
         print(f"BRAVO! trouve en {tentatives} coups.")
    except ValueError:
         print("Oups! il faut entrer un nombre entier")
         print("Fin de la partie")     