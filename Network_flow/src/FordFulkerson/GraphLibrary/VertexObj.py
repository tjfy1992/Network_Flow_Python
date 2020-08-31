"""
Date: 10/08/2019
The class for VertexObj. It is the object which can
be stored within a vertex.
"""
import src.FordFulkerson.GraphLibrary.Vertex as Vertex


class VertexObj:
    def __init__(self, closedList: list, parentVertex: Vertex):
        self.closedList = closedList
        self.parentVertex = parentVertex
