class BFSNode:
    def __init__(self, pos):
        self.previous = None
        self.neighbours = list()
        self.pos = pos

    def add_neighbour(self,node):
        self.neighbours.append(node)