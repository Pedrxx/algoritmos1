a = int(input("informe um valor pra A "))
b = int(input("informe um valor pra B "))
c = int(input("informe um valor pra C "))

if(a > b):
    if(a > c):
        print("seu maior numero é o A")
    else:
        print("seu maior numero é C")


else:
    if(c > b):
        print("seu numero maior é o C")
    else:
        print("seu numero maior é o B")
