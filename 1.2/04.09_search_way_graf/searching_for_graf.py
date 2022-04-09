import sys
try:
    class Graph(object):
        def __init__(self, znak, opening):
            self.znak = znak
            self.graph = self.construct_graph(znak, opening)
        def construct_graph(self, znak, opening):
            graph = {}
            for znak in znak:
                graph[znak] = {}
            graph.update(opening)
            for znak, edges in graph.items():
                for adjacent_node, value in edges.items():
                    if graph[adjacent_node].get(znak, False) == False:
                        graph[adjacent_node][znak] = value
            return graph
        def get_nodes(self):
            return self.znak
        def get_outgoing_edges(self, znak):
            connections = []
            for out_node in self.znak:
                if self.graph[znak].get(out_node, False) != False:
                    connections.append(out_node)
            return connections
        def value(self, node1, node2):
            return self.graph[node1][node2]
    def issledovatel(graph, ot_kuda):
        unvisited_nodes = list(graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        for znak in unvisited_nodes:
            shortest_path[znak] = max_value
        shortest_path[ot_kuda] = 0
        while unvisited_nodes:
            current_min_node = None
            for znak in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = znak
                elif shortest_path[znak] < shortest_path[current_min_node]:
                    current_min_node = znak
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path
    def print_result(perevorot, korotky, ot_kuda, kuda):
        path = []
        znak = kuda
        if znak == ot_kuda:
            print("<----------------------------ALERT---------------------------->")
            print('Вы допустили ошибку при вводе данных')
        while znak != ot_kuda:
            path.append(znak)
            znak = perevorot[znak]
        path.append(ot_kuda)
        print("Самый короткий путь: {}".format(korotky[kuda]))
        print(" -> ".join(reversed(path)))
    znaks = ["A", "B", "C", "D", "E", "F", "G", "H"]
    opening = {}
    for znak in znaks:
        opening[znak] = {}
    print("<-----Добавьте пути сами!----->")
    opening["A"]["B"] = int(input('Путь А-В: '))
    opening["A"]["C"] = int(input('Путь А-С: '))
    opening["B"]["D"] = int(input('Путь B-D: '))
    opening["B"]["E"] = int(input('Путь B-E: '))
    opening["E"]["F"] = int(input('Путь E-F: '))
    opening["E"]["G"] = int(input('Путь E-G: '))
    opening["G"]["F"] = int(input('Путь G-F: '))
    opening["H"]["D"] = int(input('Путь H-D: '))
    opening["H"]["G"] = int(input('Путь H-G: '))

    graph = Graph(znaks, opening)
    ot_kuda=input('От куда держишь путь, странник? : ')
    kuda=input('Куда держишь путь, странник? : ')
    perevorot, korotky = issledovatel(graph=graph, ot_kuda=ot_kuda)

    print_result(perevorot, korotky, ot_kuda=ot_kuda, kuda=kuda)
except ValueError:
    print('Вводите пожалуйста числа')