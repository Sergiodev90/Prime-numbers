message = '''
        hola como estas, este es un programa para saber si un numero es primo o no lo es

        si quieres darme una lista y saber si hay numeros primos en tu lista oprime 5 
        pero recuerda si esa lista no tiene comas no podre ayudarte

        mientras si solamente quieres darme un numero y seguir preguntandome solo oprime 4
        
        y si quieres salir de la consola solo basta con poner "exit"
'''
print(message)

UserAnswer = input("=>  ")
def numeroPrimo():
    while UserAnswer == "4":
        esprimo = True
        userNumber = input("coloca aqui el numero: ")
        if userNumber == "exit":
            break

        userNumber = int(userNumber)
        for x in range(2,userNumber):
            if userNumber % x == 0:
                esprimo = False
        if esprimo:
            print("es primo")
        else:
            print("no es primo")
    while UserAnswer == "5":
        userNumbers =   input("coloca aqui los numeros: ")
        userEXIT = input("justo aqui si quieres acabar el programa: ")
        if userEXIT == "exit":
            break
        if "," in userNumbers in userNumbers:
            replace  =  userNumbers.replace(",","  ")
            convert = replace.split()
            MynewList = [int(x) for x in convert]
            print(MynewList)
            for y in MynewList:
                esprimo=True
                for x in range(2,y):
                    if y % x == 0:
                        esprimo = False
                        
                if esprimo:
                    print(f'{y} es primo')
                else:
                    print(f'{y} no es primo')

        else:
            print("tu lista no tiene comas agregalas por favor")
            
if __name__ == "__main__":
    numeroPrimo()