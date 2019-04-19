import pprint
import sys


def create_graph(sommets, arcs):
    graphe = dict((s, list()) for s in sommets)
    for pred, succ, etiq in arcs:
        graphe[pred].append((succ, etiq))

    print("Affichage du graphe : ")
    pprint.pprint(graphe)
    return graphe

def dijkstra(graphe, debut):
    sommets = set(graphe.keys())
    poids = [sys.maxsize for _ in sommets] # Liste contenant les poids
    predecesseur = [debut for _ in sommets]

    poids[debut] = 0

    while len(sommets) > 0:
        s1 = None
        mini = sys.maxsize
        for sommet in sommets:
            if poids[sommet] < mini:
                mini = poids[sommet]
                s1 = sommet
        sommets.difference_update({s1})

        for succ, etiq, in graphe[s1]:
            if poids[succ] > poids[s1] + etiq:
                poids[succ] = poids[s1] + etiq
                predecesseur[succ] = s1

    return poids, predecesseur

if __name__ == "__main__":
    sommets = list(range(6))
    arcs = [
        (0, 4, 4),
        (1, 0, 4),
        (2, 1, 2),
        (2, 5, 3),
        (3, 2, 9),
        (3, 4, 2),
        (3, 5, 6),
        (4, 1, 9),
        (4, 3, 2),
        (4, 5, 3),
        (5, 1, 6),
        (5, 2, 3),
        (5, 3, 6)
        ]

    graphe = create_graph(sommets, arcs)
    d, pred = dijkstra(graphe, 3)
    print("Liste des poids: ", d)
    print("Liste des prédécesseur: ", pred)
