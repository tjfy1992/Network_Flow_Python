"""
Date: 10/08/2019
The class for Vertex
"""

from src.FordFulkerson.GraphLibrary.VertexObj import VertexObj
import src.FordFulkerson.GraphLibrary.DirectedEdge as DirectedEdge
import src.FordFulkerson.GraphLibrary.UndirectedEdge as UndirectedEdge


class Vertex:
    def __init__(self, label: str = None, obj: VertexObj = None):
        self.label = label
        self.obj = obj
        self.directed_edges = []
        self.undirected_edges = []

    """
    add a directed edge which starts from the vertex
    """
    def add_directed_edge(self, edge: DirectedEdge):
        self.directed_edges.append(edge)

    """
    add an undirected edge which takes the vertex as an end
    """
    def add_undirected_edge(self, edge: UndirectedEdge):
        self.undirected_edges.append(edge)

    """
    remove a directed edge from the vertex's directed edges
    """
    def remove_directed_edge(self, edge: DirectedEdge):
        self.directed_edges.remove(edge)

    """
    remove an undirected edge from the vertex's undirected edges.
    """
    def remove_undirected_edge(self, edge: UndirectedEdge):
        self.undirected_edges.remove(edge)
