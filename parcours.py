import pprint

def create_graph(G):
    sommets = set() #ensemble de sommets
    
    for pred, succ  in G:
        sommets.add(pred)
        sommets.add(succ)

    graphe = dict((s, list()) for s in sommets)
    for pred, succ in G:
        graphe[pred].append(succ)

    print("affichage du graphe: ")
    pprint.pprint(graphe)    
    return graphe

def parcours(graphe, sommet):
    pref = list() # liste des préfixes
    suff = list() # liste des suffixes
    visite = set()
    for sommet in graphe.keys():
        if sommet not in visite:
            parcours_aux(graphe, sommet, visite, pref, suff)
    return pref, suff

def parcours_aux(graphe, sommet, visite, pref, suff):
    visite.add(sommet) # On marque le sommet comme visité
    pref.append(sommet) # On l'ajoute à la liste des prefixes
    for succ in graphe[sommet]:
        if succ not in visite:
            parcours_aux(graphe, succ, visite, pref, suff)
    suff.append(sommet) # On l'ajoute à la liste des suffixes


if __name__ == "__main__":
    lst = [
            (0, 1),
            (0, 2),
            (0, 4),
            (1, 3),
            (1, 4),
            (2, 1),
            (3, 0),
            (3, 2),
            (4, 3),            
        ]

    lst2 = [
        ("A", "B"),
        ("A", "C"),
        ("A", "E"),
        ("B", "D"),
        ("B", "F"),
        ("C", "G"),
        ("F", "E")
        ]

    graphe = create_graph(lst)
    pref, suff = parcours(graphe, 0)
    print("Liste prefixe : ", pref)
    print("Liste suffixe : ", suff)

    graphe = create_graph(lst2)
    pref, suff = parcours(graphe, "A")
    print("Liste prefixe : ", pref)
    print("Liste suffixe : ", suff)
    
