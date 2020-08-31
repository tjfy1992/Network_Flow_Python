"""
Date: 11/27/2019
The class which implements the functions in Ford-Fulkerson algorithm
"""


from src.FordFulkerson.GraphLibrary.Graph import Graph
from src.FordFulkerson.GraphLibrary.Vertex import Vertex
from src.FordFulkerson.GraphLibrary.VertexObj import VertexObj


class FordFulkersonAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph

    """
    The entrance of the algorithm
    """
    def get_max_flow(self):
        paths = self.find_all_paths()
        stop = False
        while not stop:
            result = self.augment_path_exist(paths)
            if not result[0]:
                stop = True
                continue
            aug_path = paths[result[1]]
            delta = result[2]
            for index in range(len(aug_path) - 1):
                vertex_1_label = aug_path[index]
                vertex_2_label = aug_path[index + 1]
                edge = self.get_edge_between_two_vertices(vertex_1_label, vertex_2_label)
                # a forward path
                if edge.get_from_vertex().label == vertex_1_label:
                    edge.weight = edge.weight + delta
                # a backward path
                else:
                    edge.weight = edge.weight - delta
        return self.graph

    """
    Use dfs to find all simple paths in the graph
    """
    def find_all_paths(self):
        paths = []
        vertex_start = self.graph.get_vertex_by_label("s")
        dfs_stack = [vertex_start]
        while len(dfs_stack) != 0:
            vertex = dfs_stack.pop()
            if vertex.label == "t":
                path_arr = ['t']
                while vertex.obj.parentVertex is not None:
                    vertex = vertex.obj.parentVertex
                    path_arr.insert(0, vertex.label)
                paths.append(path_arr)
                continue
            for adjacent_vertex in self.graph.get_adjacent_vertices(self.graph.get_vertex_by_label(vertex.label)):
                if adjacent_vertex.label in vertex.obj.closedList:
                    continue
                new_vertex = Vertex(adjacent_vertex.label)
                closed_list = []
                for item in vertex.obj.closedList:
                    closed_list.append(item)
                closed_list.append(new_vertex.label)
                vertex_obj = VertexObj(closed_list, vertex)
                new_vertex.obj = vertex_obj
                dfs_stack.append(new_vertex)
        return paths

    """
    Check if a path is an augment path. returns a tuple of two elements
    If so, returns True and the residual capacity of the path
    If not, returns False and the residual capacity of the path
    """
    def is_augment_path(self, path: str) -> tuple:
        smallest_residual_cap = float('inf')
        for index in range(len(path)-1):
            vertex_1_label = path[index]
            vertex_2_label = path[index + 1]
            edge_between_two_vertices = self.get_edge_between_two_vertices(vertex_1_label, vertex_2_label)
            # a forward path
            if edge_between_two_vertices.get_from_vertex().label == vertex_1_label:
                residual_cap = edge_between_two_vertices.obj - edge_between_two_vertices.weight
            # a backward path
            else:
                residual_cap = edge_between_two_vertices.weight
            if smallest_residual_cap > residual_cap:
                smallest_residual_cap = residual_cap
        return smallest_residual_cap != 0, smallest_residual_cap

    """
    Check if an augment path exists in the graph. returns a tuple of three elements.
    If so, returns True, the index of the path in paths, and the residual capacity of the path
    If not, returns False, -1, -1.
    """
    def augment_path_exist(self, paths) -> tuple:
        for index in range(len(paths)):
            result = self.is_augment_path(paths[index])
            if result[0]:
                return True, index, result[1]
        return False, -1, -1

    """
    Given the two vertices' labels, find the edge in the graph which uses the two vertices as end points.
    If no edge is found, return None
    """
    def get_edge_between_two_vertices(self, from_vertex_label: str, to_vertex_label: str):
        from_vertex = self.graph.get_vertex_by_label(from_vertex_label)
        incident_edges = list(self.graph.get_incident_edges(from_vertex))
        for index in range(len(incident_edges)):
            if incident_edges[index].from_vertex.label == to_vertex_label \
                    or incident_edges[index].to_vertex.label == to_vertex_label:
                return incident_edges[index]
        return None
