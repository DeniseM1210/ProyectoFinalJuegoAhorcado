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







