"""
Date: 10/08/2019
The class for Directed Edge. It extends class Edge.
"""

from src.FordFulkerson.GraphLibrary.Edge import Edge
import src.FordFulkerson.GraphLibrary.Vertex as Vertex
from src.FordFulkerson.GraphLibrary.EdgeObj import EdgeObj


class DirectedEdge(Edge):
    """
    constructor. adds two attributes: from_vertex and to_vertex
    from_vertex: the origin vertex of the edge
    to_vertex: the destination of the edge
    """
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, label: str = None,
                 weight: float = None, obj: EdgeObj = None):
        super().__init__(label, weight, obj)
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex

    """
    get the from vertex
    """
    def get_from_vertex(self) -> Vertex:
        return self.from_vertex

    """
    get the to vertex
    """
    def get_to_vertex(self) -> Vertex:
        return self.to_vertex
