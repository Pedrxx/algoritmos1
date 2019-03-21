a = float(input("quantos quilos de maça voce comprou?"))
b = float(input("quantos quilos de mrango voce comprou?"))

# acima de 5 kg o preço vai de 8,90 pra 7,90 e de 3,90 pra 3,50
if(a > 5):
    if(b > 5):
        print("voce pagara",a*7.90 + b*3.50)
        c =a*7.90 + b*3.50
        if(a+b > 8):
            print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
        else:
            if(c > 25):
                print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
    else:
        print("voce pagara",a*7.90 + b*3.90)
        c = a*7.90 + b*3.90
        if(a+b > 8):
            print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
        else:
            if(c > 25):
                print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
else:
    if(b > 5):
        print("voce pagara",a*8.90 + b*3.50)
        c = a*8.90 + b*3.50
        if(a+b > 8):
            print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
        else:
            if(c > 25):
                print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
    else:
        print("voce pagara",a*8.90 + b*3.90)
        c = a*8.90 + b*3.90
        if(a+b > 8):
            print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
        else:
            if(c > 25):
                print("voce tera mais 7% de desconto,o preço sera",c - c*0.07)
