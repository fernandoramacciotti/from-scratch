def critical_path(k, p, graph):
  t = [0] * len(graph)
  longest_path = 0
  path = list()
  u = 0 # source
  for k in range(1, len(graph)):
    maxval = 0
    for i in p[k]:
      if (t[i] + graph[i][k]) > maxval:
        # update
        maxval = t[i] + graph[i][k]
        v = i
    
    # found new path
    if u != v:
      # path
      path.append((u, v))
      u = v
    # t[k]
    t[k] = maxval

  # last arc
  path.append((u, len(graph)))
  return t[-1], path
