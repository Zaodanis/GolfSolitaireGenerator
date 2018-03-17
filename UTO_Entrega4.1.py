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
            for j in range(len(listaConCantCartasPorMonton)):
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
            
    
s = SolitarioGolf()
s.generador(4, [2, 3, 5, 1])
print(s.listaMesa)
print(s.mazo)
