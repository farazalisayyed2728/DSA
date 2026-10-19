adj = [[1,2],[0,2,3],[0,1,3],[1,2]]

src = 0
dest = 1

temp = adj[1]
print("adjacency list of vertex 1   :", temp)

adj[src].append(dest)
adj[dest].append(src)

print("updated adjacency list:")
for i in range(len(adj)):
    print(f"Vertex {i}: {adj[i]}")