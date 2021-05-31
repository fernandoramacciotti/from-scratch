def kruskal(dist, nodes, edges):
  # init
  tree = list()
  tree_length = 0
  c = set()
  c.add(nodes[0])
  c_prime = set(nodes).difference(c)

  # loop until all nodes are visited
  while c_prime:
    # init vars of interest
    k = None
    j = None
    ckj = float("inf")

    # min c(r,s)
    for r, s in edges:
      # check (r, s) and (s, r) since it is an undiredcted graph
      if ((r in c) and (s in c_prime)) or\
         ((s in c) and (r in c_prime)):
        # candidate
        candidate = dist[r][s]
        if candidate < ckj:
          ckj = candidate
          # convention: k be in set C
          k = r if (r in c) else s     
          j = s if (s not in c) else r
    # update  
    c.add(j)
    c_prime.remove(j)
    tree.append((k, j))
    tree_length += ckj
  
  return tree, tree_length
