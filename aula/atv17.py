a = int(input("informe um valor pra A "))
b = int(input("informe um valor pra B "))
c = int(input("informe um valor pra C "))
d = int(input("informe um valor pra D "))

if((a > b and a > c and a > d) and (b > d and c > d) ):
    print("seu maior numero é o A e o menor é D")
elif((a > b and a > c and a > d) and (c > b  and d > b) ):
    print("seu meior numero é o A e o menor o B")
elif((a > b and a > c and a > d) and (b > c  and d > c) ):
    print("seu meior numero é o A e o menor o C")
elif((b > a and b > c and b > d) and (c > a  and d > a) ):
    print("seu maior numero é o B e o menor é o A")
elif((b > a and b > c and b > d) and (a > c  and d > c) ):
    print("seu maior numero é o B e o menor é o C")
elif((b > a and b > c and b > d) and (a > d  and c > d) ):
    print("seu maior numero é o B e o menor é o D")
elif((c > a and c > b and b > d) and (d > a  and b > a) ):
    print("seu maior numero é o C e o menor é o A")
elif((c > a and c > b and b > d) and (a > b  and d > b) ):
    print("seu maior numero é o C e o menor é o B")
elif((c > a and c > b and b > d) and (a > d  and b > d) ):
    print("seu maior numero é o C e o menor é o D")
elif((d > a and d > b and d > c) and (c > a  and b > a) ):
    print("seu maior numero é o D e o menor é o A")
elif((d > a and d > b and d > c) and (a > b  and c > b) ):
    print("seu maior numero é o D e o menor é o B")
else:
    print("seu maior numero é o D e o menor é o C")
