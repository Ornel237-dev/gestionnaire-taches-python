carre=[n**2 for n in range (1,11)]
print(carre)

nombres=[3,8,12,5,17,22,9,14]
pairs=[n for n in nombres if n%2==0]
print(pairs)

import math
point_a=(2,3)
point_b=(7,8)
distance= math.sqrt((point_b[0]- point_a[0])**2 + (point_b[1]- point_a[1])**2)
print(f"Distance:{distance:.2f}")

ages={"Fatou":28, "Moussa":34, "Awa":22}
for nom, age in ages.items():
    print(f"{nom} a {age} ans.")

mot="programmation"
compteur={}
for lettre in mot:
    if lettre in compteur:
        compteur[lettre]+=1
    else:
        compteur[lettre]=1
print(compteur)

def factorielle(n):
    if n<=1:
        return 1
    return n*factorielle(n - 1)
print(factorielle(5))


def saluer(nom, langue="fr"):
    messages={
        "fr":f"Bonjour{nom}!",
        "en":f"Hello{nom}!",
        "es":f"Hola{nom}!"
        }
    return messages.get(langue,f"Bonjour{nom}!")
print(saluer("Ibrahim"))
print(saluer("John", "en"))




