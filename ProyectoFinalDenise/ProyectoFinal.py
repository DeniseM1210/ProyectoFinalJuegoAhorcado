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

    


class JuegoAhorcado:
    op = Oportunidades()

    def cargarPalabras(self):
        cont = False

        while(cont != True):
            palabras = open("Palabras.txt")
            listaPalab = []

            for linea in palabras.read().rsplit():
                listaPalab.append(linea.upper())

            if(len(listaPalab) == 0):
                print("Archivo de palabras vacio, favor de ingresar palabras")
                self.ma.ingresarPalabras()
            else:
                cont = True

        return listaPalab

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
                












