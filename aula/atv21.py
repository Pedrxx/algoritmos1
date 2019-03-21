sal = float(input("qual o valor do seu salario?"))

if(sal <= 710):
    print("voce recebera um aumento de 20%, seu salario sera de", sal + sal*0.2)
else:
    if(sal <= 1000):
        print("voce recebera um aumento de 15%, seu salario sera de", sal + sal*0.15)
    else:
        if(sal <= 2500):
            print("voce recebera um aumento de 10%, seu salario sera de", sal + sal*0.10)
        else:
            if(sal > 2500):
                print("voce recebera um aumento de 05%, seu salario sera de", sal + sal*0.05)
