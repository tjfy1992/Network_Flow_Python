"""
Date: 10/08/2019
The class for Graph.
"""


from src.FordFulkerson.GraphLibrary.Vertex import Vertex
from src.FordFulkerson.GraphLibrary.DirectedEdge import DirectedEdge
from src.FordFulkerson.GraphLibrary.UndirectedEdge import UndirectedEdge
from src.FordFulkerson.GraphLibrary.Edge import Edge


class Graph:
    """
    constructor
    is_directed_graph: whether this graph is directed/undirected
    """
    def __init__(self, is_directed_graph):
        self.vertices = []
        self.edges = []
        self.is_directed_graph = is_directed_graph

    """
    insert a vertex into the graph
    """
    def insert_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    """
    insert a directed edge into the graph
    """
    def insert_directed_edge(self, from_vertex: Vertex, to_vertex: Vertex, edge: DirectedEdge):
        assert self.is_directed_graph
        assert self.vertices.count(from_vertex) == 1
        assert self.vertices.count(to_vertex) == 1
        from_vertex.add_directed_edge(edge)
        self.edges.append(edge)

    """
    insert an undirected edge into the graph
    """
    def insert_undirected_edge(self, vertex1: Vertex, vertex2: Vertex, edge: UndirectedEdge):
        assert not self.is_directed_graph
        assert self.vertices.count(vertex1) == 1
        assert self.vertices.count(vertex2) == 1
        vertex1.add_undirected_edge(edge)
        self.edges.append(edge)

    """
    remove a directed edge from the graph
    """
    def remove_directed_edge(self, edge: DirectedEdge):
        assert self.is_directed_graph
        assert self.edges.count(edge) == 1
        for vertex in self.vertices:
            if vertex.directed_edges.count(edge) == 1:
                vertex.remove_directed_edge(edge)
        self.edges.remove(edge)

    """
    remove an undirected edge from the graph
    """
    def remove_undirected_edge(self, edge: UndirectedEdge):
        assert not self.is_directed_graph
        assert self.edges.count(edge) == 1
        for vertex in self.vertices:
            if vertex.undirected_edges.count(edge) == 1:
                vertex.remove_directed_edge(edge)
        self.edges.remove(edge)

    """
    check if the edge is directed
    """
    @staticmethod
    def is_directed_edge(edge: Edge) -> bool:
        return isinstance(edge, DirectedEdge)

    """
    return the number of vertices in the graph
    """
    def get_vertices_number(self) -> int:
        return len(self.vertices)

    """
    return the list of the vertices in the graph
    """
    def get_vertices(self) -> []:
        return self.vertices

    """
    return the number of edges in the graph
    """
    def get_edges_number(self) -> int:
        return len(self.edges)

    """
    return the list of the edges in the graph
    """
    def get_edges(self) -> []:
        return self.edges

    """
    return a vertex with the label specified by the user
    """
    def get_vertex_by_label(self, label) -> Vertex or None:
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex
        return None

    """
    return the set of incoming edges of a vertex
    for directed graph only.
    """
    def get_incoming_edges(self, vertex: Vertex) -> set:
        assert self.is_directed_graph
        incoming_edges = set([])
        for vertex2 in self.vertices:
            for directed_edge in vertex2.directed_edges:
                if directed_edge.get_to_vertex() == vertex:
                    incoming_edges.add(directed_edge)
        return incoming_edges

    """
    return the set of outgoing edges of a vertex
    for directed graph only.
    """
    def get_outgoing_edges(self, vertex: Vertex) -> set:
        assert self.is_directed_graph
        outgoing_edges = set([])
        for directed_edge in vertex.directed_edges:
            outgoing_edges.add(directed_edge)
        return outgoing_edges

    """
    return all the adjacent vertices of a given vertex
    """
    def get_adjacent_vertices(self, vertex: Vertex) -> set:
        adjacent_vertices = set([])
        if self.is_directed_graph:
            out_edges = self.get_outgoing_edges(vertex)
            for d_edge in out_edges:
                adjacent_vertices.add(d_edge.get_to_vertex())
            in_edges = self.get_incoming_edges(vertex)
            for d_edge in in_edges:
                adjacent_vertices.add(d_edge.get_from_vertex())
            return adjacent_vertices
        else:
            for ud_edge in self.edges:
                if ud_edge.get_vertex_1() == vertex:
                    adjacent_vertices.add(ud_edge.get_vertex_2())
                elif ud_edge.get_vertex_2() == vertex:
                    adjacent_vertices.add(ud_edge.get_vertex_1())
            return adjacent_vertices

    """
    return the in-degree of a vertex
    for directed graph only.
    """
    def get_in_degree(self, vertex: Vertex) -> int:
        assert self.is_directed_graph
        return len(self.get_incoming_edges(vertex))

    """
    return the out-degree of a vertex
    for directed graph only.
    """
    def get_out_degree(self, vertex: Vertex) -> int:
        assert self.is_directed_graph
        return len(self.get_outgoing_edges(vertex))

    """
    return the total degree of a vertex
    if the graph is undirected and there is a self loop, the degree of self loop is 2.
    """
    def get_degree(self, vertex: Vertex) -> int:
        incident_edges = self.get_incident_edges(vertex)
        incident_edges_size = len(incident_edges)
        if self.is_directed_graph:
            for d_edge in incident_edges:
                if d_edge.get_from_vertex() == d_edge.get_to_vertex():
                    incident_edges_size += 1
            return incident_edges_size
        else:
            for ud_edge in incident_edges:
                if ud_edge.get_vertex_2() == ud_edge.get_vertex_1():
                    incident_edges_size += 1
            return incident_edges_size

    """
    return all the incident edges of a given vertex
    """
    def get_incident_edges(self, vertex: Vertex) -> set:
        incident_edges = set([])
        if self.is_directed_graph:
            incident_edges.update(self.get_incoming_edges(vertex))
            incident_edges.update(self.get_outgoing_edges(vertex))
            return incident_edges
        else:
            for ud_edge in self.edges:
                if ud_edge.get_vertex_1() == vertex or ud_edge.get_vertex_2() == vertex:
                    incident_edges.add(ud_edge)
            return incident_edges

    """
    remove a vertex and all its incident edges
    """
    def remove_vertex(self, vertex: Vertex):
        removed_edges = set([])
        if self.is_directed_graph:
            removed_edges.update(self.get_incoming_edges(vertex))
            removed_edges.update(self.get_outgoing_edges(vertex))
        else:
            for vertex2 in self.vertices:
                for undirected_edge in vertex2.undirected_edges:
                    if undirected_edge.get_vertex_1() == vertex:
                        removed_edges.add(undirected_edge)
                    if undirected_edge.get_vertex_2() == vertex:
                        removed_edges.add(undirected_edge)
        self.vertices.remove(vertex)
        for edge in removed_edges:
            self.edges.remove(edge)

    """
    return the two end vertices of an edge 
    """
    @staticmethod
    def get_end_vertices(edge: Edge) -> tuple:
        if isinstance(edge, DirectedEdge):
            return edge.get_from_vertex(), edge.get_to_vertex()
        elif isinstance(edge, UndirectedEdge):
            return edge.get_vertex_1(), edge.get_vertex_2()

    """
    return True if the two vertices are adjacent
    """
    def are_adjacent(self, vertex1: Vertex, vertex2: Vertex) -> bool:
        return vertex1 in self.get_adjacent_vertices(vertex2)

    """
    return the the adjacent vertices of a vertex, along with its incoming edges
    for directed graph only.
    """
    def get_adjacent_vertices_and_incoming_edges(self, vertex):
        assert self.is_directed_graph
        vertices = self.get_adjacent_vertices(vertex)
        incoming_edges = self.get_incoming_edges(vertex)
        return vertices, incoming_edges

    """
    return the the adjacent vertices of a vertex, along with its outgoing edges
    for directed graph only.
    """
    def get_adjacent_vertices_and_outgoing_edges(self, vertex):
        assert self.is_directed_graph
        vertices = self.get_adjacent_vertices(vertex)
        outgoing_edges = self.get_outgoing_edges(vertex)
        return vertices, outgoing_edges
