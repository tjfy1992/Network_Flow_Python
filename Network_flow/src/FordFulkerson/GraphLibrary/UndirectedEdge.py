"""
Date: 10/08/2019
The class for Undirected Edge. It extends class Edge.
"""

from src.FordFulkerson.GraphLibrary.Edge import Edge
import src.FordFulkerson.GraphLibrary.Vertex as Vertex
from src.FordFulkerson.GraphLibrary.EdgeObj import EdgeObj


class UndirectedEdge(Edge):
    """
    constructor. adds two attributes: vertex1 and vertex2
    vertex1: one end vertex of the edge
    vertex2: the other end vertex of the edge
    """
    def __init__(self, vertex1: Vertex, vertex2: Vertex, label: str = None,
                 weight: float = None, obj: EdgeObj = None):
        super().__init__(label, weight, obj)
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    """
    get the vertex1 of the edge
    """
    def get_vertex_1(self) -> Vertex:
        return self.vertex1

    """
    get the vertex2 of the edge
    """
    def get_vertex_2(self) -> Vertex:
        return self.vertex2
