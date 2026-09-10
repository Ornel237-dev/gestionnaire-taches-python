a=float(input("entrer un premier nombre:"))
b=float(input("entrer un deuxieme nombre:"))
addition= a + b
print(f"l'addition de {a} et {b} est: {addition}")
difference= a - b
print(f"la difference de {a} et {b} est: {difference}")
multiplication= a * b
print(f"la multiplication de {a} et {b} est: {multiplication}")
if b==0:
    print("la division de a et b est impossible")
else:
    division=a/b
    print(f"la division de {a} et {b} est: {division}")  