peso = float(input("qual o seu peso:"))
altura = float(input("qual sua altura"))

imc = peso / (altura ** 2)

if(imc < 18.5):
    print("abaixo do peso")
else:
    if(imc < 24.9):
        print("peso normal")
    else:
        if(imc < 29.9):
            print("pre obesidade")
        else:
            if(imc < 34.9):
                print("obesidade grau 1")
            else:
                if(imc < 39.9):
                    print("obesidade grau 2")
                else:
                    if(imc > 40.0):
                        print("obesidade grau 3")
