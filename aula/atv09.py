nt = int(input("qual sua nota de trabalho (entre 0 a 100)?"))
np = int(input("qual sua nota de prova (entre 0 a 100)?"))

if( (np + nt) / 2 >= 60):
    print("Aprovado")
else:
    print("Reprovado")
