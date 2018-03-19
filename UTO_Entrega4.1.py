#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
from collections import Counter
from collections import deque


class SolitarioGolf:
    listaCartasDisponibles = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                              'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def generador(self, cantMontonesMesa, listaConCantCartasPorMonton):
        auxiliar = []
        listaMesa = []                  # Lista de sublistas de cartas que se encuentran en la mesa
        mazo = []
        for i in range(cantMontonesMesa):
            listaMesa.append([])

        for i in range(cantMontonesMesa):
            for j in range(listaConCantCartasPorMonton[i]): # para que arme el monton segun la lista
                if (len(listaMesa[i]) < listaConCantCartasPorMonton[i]):
                    carta = random.choice(self.listaCartasDisponibles)
                    listaMesa[i].append(carta)
                    auxiliar.append(carta)

        # Se arma el mazo en base a la diferencia entre la lista con cartas disponibles y las que se fueron agregando a la mesa
        c1 = Counter(self.listaCartasDisponibles)
        c2 = Counter(auxiliar)
        diff = c1 - c2

        # Se 'baraja' el mazo
        mazo = random.sample(list(diff.elements()), len(list(diff.elements())))
        return mazo, listaMesa

    def obtenerCartasDadasVueltaMesa(self, listaMesa):
        listaCartasALaVista = []
        for i in range(len(listaMesa)):
            if (len(listaMesa[i]) == 0):
                listaCartasALaVista.append(0)
            for j in range(len(listaMesa[i])):
                if (j == 0):
                    if (listaMesa[i][j] == 'J'):
                        carta = 11
                    elif(listaMesa[i][j] == 'Q'):
                        carta = 12
                    elif (listaMesa[i][j] == 'K'):
                        carta = 13
                    elif(listaMesa[i][j] == 'A'):
                        carta = 1
                    else:
                        carta = int(listaMesa[i][j])

                    listaCartasALaVista.append(carta)
        return listaCartasALaVista

    def resolver(self, configuracionesPorRevisar):
        resuelto = False
        while len(configuracionesPorRevisar) > 0 and not resuelto:
            configuracion = configuracionesPorRevisar.popleft()
            cartasVistas = configuracion[0]
            listaMesa = configuracion[1]
            mazo = configuracion[2]
            if ((esVacia(listaMesa)) & (len(mazo) > 0)):
                resuelto = True
            else:
                if (len(cartasVistas) == 0):
                    # El juego comienza
                    cartasVistas.insert(0, mazo[0])
                    del(mazo[0])

                cartasALaVista = self.obtenerCartasDadasVueltaMesa(listaMesa)
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
                        if (cartasALaVista[i] == cartaInicialInt + 1) or (cartasALaVista[i] == 13 and cartaInicialInt == 1):
                            cartaMayor.append((cartasALaVista[i], i))
                        if (cartasALaVista[i] == cartaInicialInt - 1) or (cartasALaVista[i] == 1 and cartaInicialInt == 13):
                            cartaMenor.append((cartasALaVista[i], i))
                for i in range(0, len(cartaMenor)):
                    vistasAux = list(cartasVistas)
                    listaMesaAux = []
                    for lista in listaMesa:
                        listaMesaAux.append(list(lista))
                    mazoAux = list(mazo)
                    vistasAux.insert(0, cartaMenor[i][0])
                    sublistaMesa = listaMesaAux[cartaMenor[i][1]]
                    del sublistaMesa[0]
                    configuracionesPorRevisar.append((vistasAux, listaMesaAux, mazoAux))
                for i in range(0, len(cartaMayor)):
                    vistasAux = list(cartasVistas)
                    listaMesaAux = []
                    for lista in listaMesa:
                        listaMesaAux.append(list(lista))
                    mazoAux = list(mazo)
                    vistasAux.insert(0, cartaMayor[i][0])
                    sublistaMesa = listaMesaAux[cartaMayor[i][1]]
                    del(sublistaMesa[0])
                    configuracionesPorRevisar.append((vistasAux, listaMesaAux, mazoAux))
                vistasAux = list(cartasVistas)
                listaMesaAux = []
                for lista in listaMesa:
                    listaMesaAux.append(list(lista))
                mazoAux = list(mazo)
                vistasAux.insert(0, mazoAux[0])
                del(mazoAux[0])
                configuracionesPorRevisar.append((vistasAux, listaMesaAux, mazoAux))
        return resuelto

def esVacia(lista):
    for item in lista:
        if not isinstance(item, list) or not esVacia(item):
            return False
    return True

def obtenerSolitarioResolvible(cantMontonesMesa, listaConCantCartasPorMonton):
    resolvible = False
    while not resolvible:
        s = SolitarioGolf()
        mazo, glistaMesa = s.generador(cantMontonesMesa, listaConCantCartasPorMonton)
        listaMesa = []
        for lista in glistaMesa:
            listaMesa.append(list(lista))

        configuracionesPorRevisar = deque([([], listaMesa, list(mazo)),])
        resolvible = s.resolver(configuracionesPorRevisar)
    return mazo, glistaMesa


configuracion = sys.argv[1].split(',')
solitario = obtenerSolitarioResolvible(len(configuracion), map(int, configuracion))

print "Cartas en stack: " + str(solitario[0])
print "Cartas en columnas: " + str(solitario[1])