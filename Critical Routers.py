import collections

def get_critical_nodes(num_nodes, num_edges, edges):
    def build_graph(conns):
        g = collections.defaultdict(list)
        for conn in conns:
            a, b = conn
            g[a].append(b)
            g[b].append(a)
        return g

    def dfs(rank, prev_v, cur_v):
        visited[cur_v] = True
        lowest_ranks[cur_v] = rank
        for next_v in graph[cur_v]:
            if next_v == prev_v:
                continue
            if not visited[next_v]:
                dfs(rank + 1, cur_v, next_v)
            lowest_ranks[cur_v] = min(lowest_ranks[cur_v], lowest_ranks[next_v])
            if lowest_ranks[next_v] > rank:
                res.append(cur_v)
    graph = build_graph(edges)
    visited = [False for _ in range(num_nodes)]
    lowest_ranks = [i for i in range(num_nodes)]
    res = []
    dfs(0, -1, 0)
    return res


numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print (get_critical_nodes(numNodes, numEdges, edges))
