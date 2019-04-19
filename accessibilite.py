import pprint

def create_graph(sommets, arcs):
    # Création d'une liste d'adj
    graphe = dict((s, list()) for s in sommets)

    for pred, succ in arcs:
        graphe[pred].append(succ)
    pprint.pprint(graphe)
    return graphe

def accessibilite(graphe, debut, but):
    return accessibilite_aux(graphe, debut, but, set(), list())
    

def accessibilite_aux(graphe, s, but, visite, chemin):
    visite.add(s)
    chemin.append(s)
    if s == but:
        return chemin
    else:
        for succ in graphe[s]:
            if succ not in visite:
                return accessibilite_aux(graphe, succ, but, visite, chemin)

    chemin.pop()


if __name__ == "__main__":
     sommets  = list(range(6))
     arcs = [
          (0, 1),
          (0, 3),
          (1, 3),
          (2, 5),
          (3, 4),
          (4, 2),
          (5, 1),
          ]

     graphe = create_graph(sommets, arcs)
     print(accessibilite(graphe, 0, 5))
        
    
        
