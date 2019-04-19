import pprint

compteur, compteur2 = 0, 0

def create_graph(sommets, arcs):
    graphe = dict((s, list()) for s in sommets)
    for pred, succ in arcs:
        graphe[pred].append(succ)

    print("Affichage du graphe : ")
    pprint.pprint(graphe)
    return graphe


def aller_retour(graphe):
    debut = list(graphe.keys())[0]
    visite = set()
    for sommet in graphe.keys():
        if sommet not in visite:
            aller_retour_aux(graphe, sommet, visite)

def aller_retour_aux(graphe, sommet, visite):
    global compteur
    visite.add(sommet)
    for succ in graphe[sommet]:
        if succ != sommet and sommet in graphe[succ]:
            compteur += 1
        if succ not in visite:
            aller_retour_aux(graphe, succ, visite)

    
if __name__ == "__main__":
    lst = list(range(4))
    arcs = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 2),
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 2),
        (3, 3)
        ]

    graphe = create_graph(lst, arcs)
    aller_retour(graphe)
    print("Nombre d'aller retour :", compteur//2)
                            
