import pprint as pp
from copy import deepcopy

class Graph:
  def __init__(self, graph):
      self.graph = graph
      self.original_graph = deepcopy(graph)

  # path source to sink
  def path_source_sink(self, source, sink, p=None):
    # iteratively visit the next node until reach sink
    # if sink is not visited, then there is no path from source to sink
    if not p:
      p = [-1] * len(self.graph) # parent, for path reconstruction
    visited = [False] * len(self.graph)
    buffer = list()

    # init
    visited[source] = True
    buffer.append(source)

    while buffer:
      # remove first element from buffer
      i = buffer.pop(0)

      # iterate over (current) possible links
      for j, val in enumerate(self.graph[i]):
        if (not visited[j]) and (val > 0):
          # there is a link not explored yet
          buffer.append(j)
          visited[j] = True
          p[j] = i
    return True if visited[sink] else False

  def ford_fulkerson(self, source, sink, verbose=False, print_zeroed=True):
    # init
    p = [-1] * len(self.graph) # parent, for path reconstruction
    y = 0 # max flow

    # while there is a path from source to sink
    iteration = 0
    while self.path_source_sink(source, sink, p):
      iteration += 1
      if verbose:
        print(f'Iteration {iteration}')
        pp.pprint(self.graph)

      # current path
      ypath = float("inf")
      j = sink
      path = list()
      while j != source:
        # reconstruct path
        ypath = min(ypath, self.graph[p[j]][j])
        path.append((p[j], j))
        j = p[j]
      if verbose:
        print('Path:', list(reversed(path)))

      # add flow to total flow
      y += ypath

      # residual graph
      j = sink
      while j != source:
        i = p[j]
        self.graph[i][j] -= ypath # same arc
        self.graph[j][i] += ypath # return arc
        j = p[j]


    # print zeroed edges
    if print_zeroed:
      for i in range(len(self.original_graph)): 
        for j in range(len(self.original_graph[0])): 
          if (self.graph[i][j] == 0) and (self.original_graph[i][j] > 0): 
            current = self.graph[i][j]
            orig = self.original_graph[i][j]
            print(f'Edge ({i}, {j}): {orig} -> {current}')

    return y
