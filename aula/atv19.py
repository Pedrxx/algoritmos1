print("""
    Menu de Opções
1. Somar 2 números
2. Potência de um número
3. Raiz de grau N
""")
print(" ")
x = int(input("escolha uma das opçoes:"))

if(x == 1):
    y = int(input("escolha um numero: "))
    z = int(input("escolha outro numero: "))
    print("a soma é", y + z)
elif(x == 2):
    y = int(input("escolha um numero: "))
    z = int(input("escolha um numero pra ser potencia: "))
    print("o numero atual é", y ** z)
else:
    y = int(input("escolha um numero: "))
    z = int(input("escolha um grau pra raiz: "))
    print("o numero atual é", y ** (1/z) )
