def dijkstra(start, end, dist, nodes, edges):
  # init
  R = set([start]) # first node
  nodes_set = set(nodes)
  NR = nodes_set.difference(R) # {second_node, ..., end}
  d = [float("inf")] * (end+1)
  p = [float("inf")] * (end+1)
  
  d[start] = 0
  p[start] = -1
  a = start 
  total_dist = 0

  # loop
  while a != end:
    any_finite_di = False
    for i in NR:
      # minimum d(i)
      d[i] = min(d[i], d[a] + dist[a][i])
      if d[i] < float("inf"):
        any_finite_di = True
        if (d[i] == d[a] + dist[a][i]):
          p[i] = a
          # exists any d[i] < inf?
    
    if not any_finite_di:
      # no path from start to any node in NR
      return False, total_dist
    
    # k in NR which d[k] = min{d[i] for i in NR}
    k = None
    minval = float("inf")
    for i in NR:
      if d[i] < minval:
        k = i
        minval = d[i]
    # update
    R.add(k)
    NR.remove(k)
    a = k
  
  # recover path
  path = list()
  ki = end
  while ki != 0:
    path.append((p[ki], ki))
    total_dist += dist[p[ki]][ki]
    ki = p[ki]
    
  return path, total_dist
