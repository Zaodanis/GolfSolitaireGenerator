import random
from collections import Counter

class SolitarioGolf:
    listaMesa = []                  # Lista de sublistas de cartas que se encuentran en la mesa
    mazo = []
    listaCartasDisponibles = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def generador(self, cantMontonesMesa, listaConCantCartasPorMonton):
        auxiliar = []
        for i in range(cantMontonesMesa):
            self.listaMesa.append([])
        
        for i in range(cantMontonesMesa):
            for j in range(listaConCantCartasPorMonton[i]): # para que arme el monton segun la lista
                if (len(self.listaMesa[i]) < listaConCantCartasPorMonton[i]):
                    carta = random.choice(self.listaCartasDisponibles)
                    self.listaMesa[i].append(carta)
                    auxiliar.append(carta)

        # Se arma el mazo en base a la diferencia entre la lista con cartas disponibles y las que se fueron agregando a la mesa
        c1 = Counter(self.listaCartasDisponibles)
        c2 = Counter(auxiliar)
        diff = c1 - c2

        # Se 'baraja' el mazo
        self.mazo = random.sample(list(diff.elements()), len(list(diff.elements())))

    def obtenerCartasDadasVueltaMesa(self):
        listaCartasALaVista = []
        for i in range(len(self.listaMesa)):
            if (len(self.listaMesa[i]) == 0):
                listaCartasALaVista.append(0)
            for j in range(len(self.listaMesa[i])):
                if (j == 0):
                    if (self.listaMesa[i][j] == 'J'):
                        carta = 11
                    elif(self.listaMesa[i][j] == 'Q'):
                        carta = 12
                    elif (self.listaMesa[i][j] == 'K'):
                        carta = 13
                    elif(self.listaMesa[i][j] == 'A'):
                        carta = 1
                    else:
                        carta = int(self.listaMesa[i][j])
                        
                    listaCartasALaVista.append(carta)
        return listaCartasALaVista

    def resolver(self, cartasVistas):
        print("Mesa: ", self.listaMesa)
        
        if ((esVacia(self.listaMesa) == True) & (len(self.mazo) > 0)):
            print("WIN *******")
        elif(len(self.mazo) == 0):
            print("LOOSE *******")
        else:
            if (len(cartasVistas) == 0):
                # El juego comienza
                cartasVistas.insert(0, self.mazo[0])
                del(self.mazo[0])            
            
            cartasALaVista = self.obtenerCartasDadasVueltaMesa()
            
            print('Carta Inicial: ', cartasVistas[0])

            cartaMayor = []
            cartaMenor = []
            for i in range(len(cartasALaVista)):                
                cartaInicial = cartasVistas[0]
                if (cartaInicial == 'J'):
                    cartaInicialInt = 11
                elif(cartaInicial == 'Q'):
                    cartaInicialInt = 12
                elif (cartaInicial == 'K'):
                    cartaInicialInt = 13
                elif(cartaInicial == 'A'):
                    cartaInicialInt = 1
                else:
                    cartaInicialInt = int(cartaInicial)


                if (cartasALaVista[i] != 0):
                    if (cartasALaVista[i] == cartaInicialInt + 1 | (cartasALaVista[i] == 13 & cartaInicialInt == 1)):
                        cartaMayor.append(cartasALaVista[i])
                        cartaMayor.append(i)
                    if (cartasALaVista[i] == cartaInicialInt - 1 | (cartasALaVista[i] == 1 & cartaInicialInt == 13)):
                        cartaMenor.append(cartasALaVista[i])
                        cartaMenor.append(i)
                    
            if (len(cartaMenor) > 0):
                print("Cambia ", cartasVistas[0], " por ", cartaMenor[0])
                cartasVistas.insert(0, cartaMenor[0])

                sublistaMesa = self.listaMesa[cartaMenor[1]]
                del(sublistaMesa[0])
                
            elif (len(cartaMayor) > 0):
                print("Cambia ", cartasVistas[0], " por ", cartaMayor[0])
                cartasVistas.insert(0, cartaMayor[0])

                sublistaMesa = self.listaMesa[cartaMayor[1]]
                del(sublistaMesa[0])
                
            else:
                cartasVistas.insert(0, self.mazo[0])
                del(self.mazo[0])

            print("*************** Terminó jugada ********************** \n \n")    
            self.resolver(cartasVistas)

def esVacia(lista):
    for item in lista:
        if not isinstance(item, list) or not esVacia(item):
            return False
    return True
                
s = SolitarioGolf()
s.generador(4, [4, 3, 5, 1])
s.resolver([])




