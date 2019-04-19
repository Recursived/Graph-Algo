import pprint

def create_graph(sommets, arcs):
   graphe = dict((s, list()) for s in sommets)
   for pred, succ in arcs:
      graphe[pred].append(succ)

   pprint.pprint(graphe)
   return graphe

def longest_path(graphe, but):
   start = list(graphe.keys())[0]
   visite = set()
   visite.add(start)
   path = list()
   path.append(start)
   to_return = list()
   
   longest_path_aux(graphe, start, visite, path, but, to_return)
   
   return to_return
   
def longest_path_aux(graphe, current_node, visited, path, but, to_return):

   if ( len(path) == len(graphe.keys() ) and current_node == but):
      to_return.extend(path)
      
   for succ in graphe[current_node]:
      if succ not in visited:
         visited.add(succ)
         path.append(succ)

         longest_path_aux(graphe, succ, visited, path, but, to_return)

         visited.remove(succ)
         path.pop()
         

   

                     
if __name__ ==  "__main__":
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
   path = longest_path(graphe, 5)
   print("Chemin élémentaire le plus long :", path, "Longueur du chemin :" , len(path), sep="\n")
