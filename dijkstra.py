import heapq

def shortest_path(G, start, end):
  def flatten(L):
    while len(L) > 0:
      yield L[0]
      L = L[1]

  q = [(0, start, ())]
  visited = set()

  while True:
    (cost, v1, path) = heapq.heappop(q)
    print 'Poped: cost = %d, node = %s, path = %s'%( cost, v1, path)
    if v1 not in visited:
      visited.add(v1)
      if v1 == end:
        return list(flatten(path))[::-1] + [v1]
      path = (v1, path)
      for (v2, cost2) in G[v1].iteritems():
        if v2 not in visited:
          print 'Added: cost = %d, node = %s, path = %s'%(cost + cost2, v2, path)
          heapq.heappush(q, (cost + cost2, v2, path))

Graph = {
    's':{'u':10, 'x':5}, 
    'u':{'v':1, 'x':2}, 
    'v':{'y':4}, 
    'x':{'u':3, 'v':9, 'y':2}, 
    'y':{'s':7, 'v':6}}
print shortest_path(Graph, 's', 'v')
