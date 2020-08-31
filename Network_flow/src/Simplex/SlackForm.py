"""
Date: 11/26/2019
The class of slack form
"""


class SlackForm:
    def __init__(self, N, B, A, b, c, v):
        self.N = N
        self.B = B
        self.A = A
        self.b = b
        self.c = c
        self.v = v

    def get_N(self):
        return self.N

    def get_B(self):
        return self.B

    def get_A(self):
        return self.A

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_v(self):
        return self.v
