"""
Study of the Depth First Search algorithm.
Undirected network.
Can easily be changed into directed.
"""



class Vertex():
    """Vertex data structure.

    Variables:
    self.name: [string] name
    self.neighbors: [list] neighbors name

    methods:
    __init__()
    add_neighbors(self, n)
    """

    def __init__(self, name, neighbors):

        self.name = name
        self.neighbors = []

        # ???
        self.distance = 9999
        self.status = 0
        # ??? visiting status
        # status meaning:
        # 0: undiscovered
        # 1: discovered
        # 2: visited


    def add_neighbors(self, n):

        if n not in self.neighbors:
            # ?? the complexity of such methods?

            self.neighbors.append(n)
            self.neighbors.sort() # why need sort?

class Graph():
    """Graph data structure.

    Variables:
    vertices: [dict] name and reference to the corresponding vertex.

    method:
    __init__()
    add_vertex()
    print_graph()
    bfs()
    """

    def __init__(self):

        vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # make the code more reliable
            # avoid duplication
            self.vertices[vertex.name] = vertex
            # confirm the success of the operation
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices)):
            print(key+" | "+ str(self.vertices[key].neighbors))


    def bfs(self, start):
        """
        Breadth first search.
        Parameters:
        start: the name of the starting vertex.

        Print the process of the bfs.
        """



















