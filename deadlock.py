def store_file(file_name):
    """
        This is a function to retrieve information from the file provided by the user.
    """

    lst = []
    # Read through the file line by line
    with open(file_name, 'r') as f:
        for line in f:
            # If it starts with a % or if it's an empty line (weird formatting in file) then continue
            if line[0] == "%" or len(line) <= 1:
                continue
            else:
                # If it is a valid line, then shove it into our list
                lst.append(line.strip())

    # Parse through list to recover information we need to solve problem
    num_processes = lst[0].split("=")[1] 
    num_resources = lst[1].split("=")[1]
    each_resource = lst[2].split(",")
    matrix = []
    for row in lst[3:]:
        r = row.split(",")
        matrix.append(r)
    # Returns a set of tuples for each parameter we need
    return num_processes, num_resources, each_resource, matrix

class Graph:
    """
        Class to do graph algorithms.
    """


    def __init__(self, processes, resources, each_resource, matrix):
        self.number_processes = processes
        self.number_resources = resources
        self.number_each_resource = each_resource
        self.matrix = matrix
        self.resource_neighbors = {}
        self.process_neighbors = {}
        self.node_queue = []


    def sanity_check(self):
        print(f'{self.number_processes}')
        print(f'{self.number_resources}')
        print(f'{self.number_each_resource}')
        print(f'{self.matrix}')


    def create_dictionaries(self):
        # Find the resources that are connected to a process
        position = 1
        for resource in self.matrix[:3]:
            self.process_neighbors['r' + str(position)] = resource
            position += 1

        # Find the processes that are connected to a resource
        position = 1
        for process in self.matrix[3:]:
            self.resource_neighbors['p' + str(position)] = process
            position += 1


    def create_queue(self):
        for r, p in zip(self.resource_neighbors, self.process_neighbors):
            r_node = Node(r, self.resource_neighbors[r])
            p_node = Node(p, self.process_neighbors[p])
            self.node_queue.append(r_node)
            self.node_queue.append(p_node)

        self.node_queue.sort(key = lambda x: x.name, reverse = False)

    def check_queue_contents(self):
        print('Printing queue contents...')
        for item in self.node_queue:
            print(item.name , item.adjacency_list)


class Node:
    """
        Helper class to store information about a particular node.
    """
    def __init__(self, name, adjacency_list):
        self.name = name
        self.adjacency_list = adjacency_list

    



if __name__ == "__main__":
    # Change s to be a CLI in the future with a prompt to user.
    file_name  = "Project-2-input-example.txt"

    # Can recover data like this,
    num_processes, num_resources, each_resource, matrix = store_file(file_name)
    g = Graph(num_processes, num_resources, each_resource, matrix)
    g.create_dictionaries()
    g.create_queue()
    g.check_queue_contents()
