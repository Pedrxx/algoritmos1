sal = float(input("qual o valor do seu salario? "))

if(sal > 3000):
    print("seu salario bruto é", sal)
    print("o imposto é de 15%, entao seu salario liquido é de", sal - sal *0.15)
else:
    
    print("seu salario bruto é", sal)
    print("o imposto é de 7,5, entao seu salario liquido é de", sal - sal *0.075)
