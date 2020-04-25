# need to create a graph and utilize bfs?
#  but upon adding new current only add the smallest of the "parents" aka neighbors
# need to setup so tha as making the dict for verticies makes all the verticies
# but sets up so that the "neighbors" are the parents of the vertices to use in
# that similar manner as our graph is used in graphs directory file graph.py
# will need to make some small adjustments to the way its queued/
# seeing as this only returns a single integer an not a list
# then it could be just the simple watchfull movement until there are not parents from child
# aka no neighbors of last integer/vertex
#
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    print(ancestors, starting_node)
    graph_A = Graph()
    for each in graph_A.vertices:
        print(each)
    for i in ancestors:
        graph_A.add_vertex(i[0])
        graph_A.add_vertex(i[1])
    for each in graph_A.vertices:
        print("in graph", each)


if __name__ == '__main__':
    testA = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    starting_node = 6
    earliest_ancestor(testA, starting_node)

    for vertex in testA:
        print(vertex[1])
