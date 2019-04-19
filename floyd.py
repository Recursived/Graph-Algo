import sys
import pprint

def create_graph(G):
    sommets = set()
    for pred, succ, etiq in G:
        sommets.add(pred)
        sommets.add(succ)

    
    graphe = [[sys.maxsize] * len(sommets) for _ in range(len(sommets))]
    for i in range(len(graphe)):
        graphe[i][i] = 0

    for pred, succ, etiquette in G:
        graphe[pred][succ] = etiquette

    print("graphe construit : ")
    pprint.pprint(graphe)
    return graphe

def floyd(G):
    graphe = create_graph(G)
    for k in range(len(graphe)):
        for i in range(len(graphe)):
            for j in range(len(graphe)):
                graphe[i][j] = min(graphe[i][j], graphe[i][k] + graphe[k][j])
    return graphe

if __name__ == "__main__":
    lst = [
            (0, 1, 3),
            (0, 2, 8),
            (0, 4, -4),
            (1, 3, 1),
            (1, 4, 7),
            (2, 1, 4),
            (3, 0, 2),
            (3, 2, -5),
            (4, 3, 6),            
        ]

    pprint.pprint(floyd(lst))
