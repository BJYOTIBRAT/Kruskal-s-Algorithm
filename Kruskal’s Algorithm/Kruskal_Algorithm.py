class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.

        :param vertices: int, number of vertices in the graph
        """
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        """
        Add an edge between vertices u and v with weight w.

        :param u: int, vertex u
        :param v: int, vertex v
        :param w: int, weight of the edge
        """
        self.graph.append([u, v, w])

    def search(self, parent, i):
        """
        Recursively find the root of vertex i.

        :param parent: list, parent vertex of each vertex
        :param i: int, vertex i
        :return: int, root of vertex i
        """
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        Union the connected components of vertices x and y.

        :param parent: list, parent vertex of each vertex
        :param rank: list, rank of each connected component
        :param x: int, vertex x
        :param y: int, vertex y
        """
        x_root = self.search(parent, x)
        y_root = self.search(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        """
        Implement Kruskal's algorithm to find the minimum spanning tree of the graph.
        """
        result = []
        i, e = 0, 0

        # Sort the edges in ascending order of weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x!= y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        for u, v, weight in result:
            print("Edge: ", u, v, end=" ")
            print("-", weight)

g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)

print("Kruskal's Algorithm:")
g.kruskal()