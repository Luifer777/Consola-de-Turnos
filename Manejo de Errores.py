'''def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))

    print(n1 + n2)
    print("Gracias por sumar" + n1)



try:
    suma()
except TypeError:
    print("Estas esquivocado cv")
except ValueError:
    print("Ese no es un numero cachon")
else:
    print("Hiciste todo bien")
finally:
    print("Abrete de esta monda eso fue todo")'''

def pedir_nuemro():

    while True:
        try:
            nuemro = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {nuemro}")
            break
pedir_nuemro()



