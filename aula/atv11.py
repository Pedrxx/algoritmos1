a = int(input("informe um valor pra A "))
b = int(input("informe um valor pra B "))
c = int(input("informe um valor pra C "))

if(a > b):
    if(a > c):
        if(c > b):
            print("sua ordem crescente é B, C e A")
        else:
            print("sua ordem é C, B e A ")
    else:
        print("sua ordem crescente é B, A e C")



else:
    if(c > a):
        if(c > b):
            print("sua ordem crescente é A, B e C")
        else:
            print("sua ordem crescente é A, C e B")
    else:
        print("sua ordem crescente e C, A e B")
