"""
Date: 10/08/2019
The class for Edge. It is the parent class of
Directed edge and Undirected edge.
"""

from src.FordFulkerson.GraphLibrary.EdgeObj import EdgeObj


class Edge:
    """
    constructor.
    label: the label of the edge
    weight: the weight of the edge
    obj: an instance of EdgeObj
    """
    def __init__(self, label: str = None, weight: float = None, obj: EdgeObj = None):
        self.label = label
        self.weight = weight
        self.obj = obj
