def floyd_warshall(i, j, size, dist):
  # logic
  min_dist = dist[i][j]
  algo_path = list()
  last = i # last visited node
  for k in range(size):
    if min_dist > (dist[i][k] + dist[k][j]):
      # update
      min_dist = dist[i][k] + dist[k][j]
      algo_path.append((last, k))
      last = k
  # final path
  algo_path.append((last, j))
  
  return min_dist, algo_path
