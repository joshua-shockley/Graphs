"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 in self.vertices and v1 in self.vertices:
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def get_ancestor(self, starting_vertex):
        parents = self.get_neighbors(starting_vertex)
        print("parents: ", parents)
        theP = []
        print('length of parents array before doing anything:', len(theP))
        for thing in parents:
            theP.append(thing)
        if len(parents) == 0:
            theP.append(None)
            print('if no neighbors to add', theP[0])
            return theP[0]
        if len(theP) == 1:
            print(theP[0])
            smallest = theP[0]
            print(smallest)
            return smallest
        if len(theP) == 2:
            item1 = theP[0]
            item2 = theP[1]
            print(item1, item2)
            if item1 < item2:
                smallest = item1
                print("smallest parent: ", smallest)
            else:
                smallest = item2
                print("smallest parent: ", smallest)
            return smallest

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex from the stack
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex in
            breath-first order.
            """
        # create a empty queue, and enqueue a PATH to the starting vertex
        # create a set for visited vertices
        visited_vertices = set()

        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            print(f"current_path: {current_path}")
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex == destination_vertex:
                    return current_path
                    # Return the path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)
    pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
            Return a list containing a path from
            starting_vertex to destination_vertex in
            depth-first order.
            """
        # This solution takes a slightly different approach as to how we are storing the path
        # Now, we always queue up the next vertex we want to see, and a list of all the vertices we looked at to get here
        # so if we are queueing up vertex 3 from our example, the tuple we create will be (3, [1,2])
        # because we had to go through 1 and 2 to get here
        visited_vertices = set()

        neighbors_to_visit = Stack()
        # add the first vertex, and an empty list indicating that we have not been to any other vertices yet
        neighbors_to_visit.push((starting_vertex, []))
        # loop through the stack
        while neighbors_to_visit.size() > 0:
            # This will have (current_vertex, path)
            current_vertex_plus_path = neighbors_to_visit.pop()
            # pull out the current vertex so its easier to read
            current_vertex = current_vertex_plus_path[0]
            # pull out the path so its easier to read
            current_path = current_vertex_plus_path[1]
            # make sure the vertex isnt something we have seen already
            if current_vertex not in visited_vertices:

                # if the vertex is the destination return it plus the path we took to get here
                if current_vertex == destination_vertex:
                    # eg: if the vertex was 6, and we went through 1, 2, 4 to get here, add that to complete the full path
                    updated_path = current_path + [current_vertex]
                    print(
                        f"updated path: {updated_path}, last vertex{updated_path[-1]}")
                    return updated_path

                # mark the vertex as visited
                visited_vertices.add(current_vertex)
                # add neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_path + [current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))

    # def dfs_ancestor(self, starting_vertex):
    #     visited_vertices = set()

    #     pc = Queue()
    #     pc.enqueue([starting_vertex])

    #     while pc.size() > 0:
    #         current_path = ''


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(4, 5)
    graph.add_edge(4, 8)
    graph.add_edge(8, 9)
    graph.add_edge(11, 8)
    graph.add_edge(10, 1)

    '''
        Should print:
            {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
        '''
    print("print vertices: ", graph.vertices)

    '''
        Valid BFT paths:
            1, 2, 3, 4, 5, 6, 7
            1, 2, 3, 4, 5, 7, 6
            1, 2, 3, 4, 6, 7, 5
            1, 2, 3, 4, 6, 5, 7
            1, 2, 3, 4, 7, 6, 5
            1, 2, 3, 4, 7, 5, 6
            1, 2, 4, 3, 5, 6, 7
            1, 2, 4, 3, 5, 7, 6
            1, 2, 4, 3, 6, 7, 5
            1, 2, 4, 3, 6, 5, 7
            1, 2, 4, 3, 7, 6, 5
            1, 2, 4, 3, 7, 5, 6
        '''
    graph.bft(6)
    print("DFT")

    '''
        Valid DFT paths:
            1, 2, 3, 5, 4, 6, 7
            1, 2, 3, 5, 4, 7, 6
            1, 2, 4, 7, 6, 3, 5
            1, 2, 4, 6, 3, 5, 7
        '''
    graph.dft(6)

    '''
        Valid BFS path:
            [1, 2, 4, 6]
        '''
    print(graph.bfs(6, 10))
    print("DFS")

    '''
        Valid DFS paths:
            [1, 2, 4, 6]
            [1, 2, 4, 7, 6]
        '''
    print(graph.dfs(6, 10))

    print('get ancestor fn')
    print(graph.get_ancestor(6))
