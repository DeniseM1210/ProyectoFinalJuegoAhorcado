import random


class JuegoAhorcado:


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



class Oportunidades:
    oportunidades = 0

    def iniciarOportunidades(self):
        self.oportunidades = 10

    def reducirOp(self):
        if(self.oportunidades > 0):
            self.oportunidades -= 1

    def getOportunidades(self):
        return self.oportunidades







