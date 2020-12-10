import random

class Oportunidades:
    oportunidades = 0

    def iniciarOportunidades(self):
        self.oportunidades = 10

    def reducirOp(self):
        if(self.oportunidades > 0):
            self.oportunidades -= 1

    def getOportunidades(self):
        return self.oportunidades

class ManipulacionDeArchivos:
    def verificarArchivo(self):
        palabras = open("Palabras.txt")
        listaPalab = []

        for linea in palabras.read().rsplit():
            listaPalab.append(linea.upper())
        palabras.close()
        return len(listaPalab)

    def ingresarPalabras(self):
        cont = False
        op = 0

        while(cont != True):
            palabras = open("Palabras.txt", "a")
            print("Ingrese una palabra: ")
            nuevaPalab = input()

            palabras.write('\n' + nuevaPalab)
            palabras.close()
            print("Se agrego correctamente la palabra :)")
            salida = False

            while(salida != True):
                print("Desea ingresar otra palabra? ")
                print("1.- Si")
                print("2.- No")
                op = input()
                if(op == "1" or op == "2"):
                    salida = True
                else:
                    print("Opcion invalida, unicamente numeros del 1 al 2")
                    salida = False
            if(int(op) == 1):
                cont = False
            else:
                cont = True

    def borrarPalabras(self):
        open("Palabras.txt", "w").write("")

    def obtenerPalabrasArchivo(self):
        if(self.verificarArchivoVacio() == False):
            palabrasArch = ""
            palabras = open("Palabras.txt")
            palabrasArch = palabras.read()
            palabras.close()
            return palabrasArch
        else:
            return '!'

    def juego(self):
        if(self.verificarArchivoVacio()):
            return True
        else:
            return False

    def ordenShellSort(self, palabras):
        n = len(palabras)
        intervalo = n / 2

        while(intervalo > 0):
            for i in range(int(intervalo), n):
                val = palabras[i]
                j = i

                while((j >= int(intervalo)) and (palabras[j - int(intervalo)] > val)):
                    palabras[j] = palabras[j - int(intervalo)]
                    j -= int(intervalo)

                palabras[j] = val

            intervalo /= 2

        ma.borrarPalabras(self)
        palabras = open("Palabras.txt", "a")
        for i in range(len(palabras)):
            palabras.write('\n' + str(palabras[i]))
        palabras.close()
ma = ManipulacionDeArchivos


class JuegoAhorcado:
    op = Oportunidades()
    ma = ManipulacionDeArchivos

    def cargarPalabras(self):
        cont = False
        while (cont != True):

            palabras = open("Palabras.txt")
            listaPalabras = []

            for linea in palabras.read().rsplit():
                listaPalabras.append(linea.upper())

            if (len(listaPalabras) == 0):
                print("Archivo vacio, porfavor ingresa algunas palabras")
                self.ma.ingresarPalabras()
            else:
                cont = True

        return listaPalabras

    def elegirPalabra(self, listaPalab):
        return (listaPalab[int(random.randrange(len(listaPalab)))])

    def inicioAhorcado(self, palabra):
        print("--- Bienvenido al juego del Ahorcado ---")
        print("Estoy pensando en una palabra de " + str(len(palabra)) + " letras")
        print("¿Puedes adivinarla?")

        abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        letra = ""
        letrasIng = []
        self.op.iniciarOportunidades()

        while(juegoA.seAdivinoLaPalabra(palabra, letrasIng) != True):
            print("--------------------")
            print("Te quedan " + str(self.op.getOportunidades()) + " oportunidades restantes")
            print("Letras disponibles: ")
            print(abecedario)

            valido = False
            while(valido != True):
                print("Ingrese una letra: ")
                letra = input().lower()

                if(letra in letrasIng):
                    print("Ya has ingresado esa letra")
                elif(len(letra) > 1):
                    print("Ingresa una letra a la vez :)")
                elif((letra).isalpha and not letra.isalnum()):
                    print("Ingresa unicamente letras :)")
                elif(letra.isnumeric()):
                    print("Ingresa unicamente letras :)")
                else:
                    valido = True
            letrasIng.append(letra)
            if((juegoA.busquedaLineal(palabra, letra.upper())) != True):
                print("La letra ingresada no se encuentra en la palabra :(")
                self.op.reducirOp()

            juegoA.obtenerPalabraAdivinada(palabra, letrasIng)
            juegoA.obtenerLetrasDisponibles(letrasIng, abecedario)


    def seAdivinoLaPalabra(self, palabra, letrasIng):
        for letra in palabra.lower():
            if(letra not in letrasIng):
                while(self.op.getOportunidades() > 0):
                    return False

        if(self.op.getOportunidades() == 0):
            print("No se ha adivinado la palabra :(")
            print("La palabra secreta era: " + palabra)
        else:
            print("Felicidades has ganado el juego del Ahorcado! :)")

        salida = False

        while(salida != True):
            print("Desea jugar de nuevo?")
            print("1.- Si :)")
            print("2.- No :(")
            opcion = input()

            if(opcion == "1" or opcion == "2"):
                salida = True
            else:
                print("Opcion invalida, unicamente numeros del 1 al 2")
                salida == False

        if(int(opcion) == 2):
            print("Gracias por jugar! :)")

        return True

    def obtenerPalabraAdivinada(self, palabra, letrasIng):
        palabraSecreta = ""

        for letra in palabra.lower():
            if(letra in letrasIng):
                palabraSecreta += " " + letra
                continue
            palabraSecreta += " _"
        print(palabraSecreta)

    def obtenerLetrasDisponibles(self, letrasIng, abecedario):
        i = 0

        for letra in abecedario:
            for letra2 in letrasIng:
                if(letra == letra2):
                    abecedario[i] = ""
            i += 1

        return abecedario


    def busquedaLineal(self, palabra, letra2):
        for letra in palabra:
            if(letra == letra2):
                return True
        return False

juegoA = JuegoAhorcado()

juegoA = JuegoAhorcado()
ma = ManipulacionDeArchivos()

salir = False

while(salir != True):
    salida = False

    while(salida != True):
        print("Elija una opcion: ")
        print("1.- Verificar Archivo")
        print("2.- Llenar el archivo")
        print("3.- Borrar archivo")
        print("4.- Jugar")
        print("5.- Salir")
        op = str(input())

        if(op == "1" or op == "2" or op == "3" or op == "4" or op == "5" or op == "6"):
            salida = True
        else:
            print("Opcion invalida, unicamente numeros del 1 al 6")
            salida = False

        if(op == "1"):
            ma.verificarArchivo()
            print("Hay " + str(ma.verificarArchivo()) + " palabras")

        if(op == "2"):
            ma.ingresarPalabras()
        if(op == "3"):
            ma.borrarPalabras()
            print("Las palabras han sido borradas del archivo!")
        if(op == "4"):
            palabras = juegoA.cargarPalabras()
            palabra = juegoA.elegirPalabra(palabras)
            juegoA.inicioAhorcado(palabra)
        if(op == "5"):
            print("Gracias por jugar! :)")
            salir = True
            



















