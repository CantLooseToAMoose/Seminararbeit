class BFSNode:
    def __init__(self, pos):
        self.previous = None
        self.neighbours = list()
        self.pos = pos

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def reset_prev(self):
        self.previous = None


def reset_list_of_list_of_nodes_previous(node_list_of_lists):
    for node_list in node_list_of_lists:
        for node in node_list:
            node.reset_prev()


def breadth_first_search(node_list_of_lists, start, goal):
    visited = []
    queue = []
    queue.append(node_list_of_lists[start[0]][start[1]])
    node = None
    while len(queue) != 0:
        prev = node
        node = queue.pop(0)
        node.previous = prev
        if node == node_list_of_lists[goal[0]][goal[1]]:
            break
        visited.append(node)
        for neighbour in node.neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    path = []
    while node.previous != None:
        path.append(node.previous)
        node = node.previous
    return path
