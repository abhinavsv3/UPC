parent = dict()
rank = dict()

def make_set(v):
  parent[v] = v
  rank[v] = 0

def find(v):
  if parent[v] != v:
    parent[v] = find(parent[v])
  return parent[v]

def union(v1,v2):
   r1 = find(v1)
   r2 = find(v2)
   if r1 != r2:
     if rank[r1] > rank[r2]:
       parent