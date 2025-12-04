# 12345678901234567890123456789012345678901234567890123456789012345678901234567890
def find_path(graph: list[list[int]], source: int, target: int):
    """Return a path -- any path -- from source to target in the graph"""

    # Initialize return item
    path: list[int] = None

    # Make sure inputs are ok
    if graph is not None:
        n: int = len(graph)
        if n > 0 and (0 <= source < n) and (0 <= target < n):

            # Initialize DFS tools
            no_edge: int = graph[0][0]  # absence of edge
            marked: list[int] = [source]  # vertices already processed
            found: bool = False  # Flags detection of path

            # What vertex to explore next and what is the path
            # to it. The information is stored as a tuple in
            # the form:
            #  (vertex, path_to_this_vertex)
            # with path_to_this_vertex being a list of the
            # vertices alonγ the path.
            stack: list[(int, list[int])] = [(source, [source])]

            while len(stack) > 0 and not found:
                # Explore the next vertex from the stack
                (u, path_from_source_to_u) = stack.pop()
                found = (u == target)
                if found:
                    # u is the end of the path, so we got what we are 
                    # looking for
                    path = path_from_source_to_u
                else:
                    # Explore the neighbors of u, hopefully one of them
                    # will get us a stop closer to the target vertex.
                    v: int = n - 1
                    while v >= 0:
                        if graph[u][v] != no_edge and v not in marked:
                            marked.append(v)
                            stack.append((v, path_from_source_to_u + [v]))
                        v -= 1
    return path

def copy_matrix(M):
    return [row[:] for row in M]

def ford_fulkerson(graph, source, target):
    n = len(graph)
    residual_graph = copy_matrix(graph)
    max_flow = 0
    path = find_path(residual_graph, source, target)
    
    while path is not None:
        flow_path = float('inf')
        i = 0
        while i < len(path) -1:
            u  = path[i]
            v = path[i+1]
            if residual_graph[u][v] < flow_path:
                flow_path = residual_graph[u][v]
            i += 1

        max_flow += flow_path

        # Update residual graph
        i = 0
        while i < len(path) - 1:
            u = path [i]
            v = path [i+1]
            residual_graph[u][v] -= flow_path
            residual_graph[v][u] += flow_path
            i += 1
            # need to get the next path
        path = find_path(residual_graph, source, target)

    is_Reachable = set([source])
    stack = [source]

    while len(stack) > 0:
        u = stack.pop()
        v = 0
        while v < n:
            if residual_graph[u][v] > 0 and v not in is_Reachable:
                is_Reachable.add(v)
                stack.append(v)
            v += 1

# make the minimum cut
    min_cut = []
    u_set = list(is_Reachable)
    i = 0
    while i < len(u_set):
        u = u_set[i]
        v = 0
        while v < n:
            if v not in is_Reachable and graph[u][v] > 0:
                min_cut.append((u,v))
            v += 1
        i += 1
    return (max_flow, min_cut)

if __name__ == "__main__":
    G = [  #  A   B   C   D   E
        [0, 20, 0, 0, 0],  # A
        [0, 0, 5, 6, 0],  # B
        [0, 0, 0, 3, 7],  # C
        [0, 0, 0, 0, 8],  # D
        [0, 0, 0, 0, 0],  # E
]
    (max_flow, min_cut) = ford_fulkerson(G, 0, 4)
    print("Max flow:", max_flow)
    print("Min cut:", min_cut)
   
