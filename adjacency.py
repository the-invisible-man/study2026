
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # O(|V|)
edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'd'),
    ('b', 'e'),
    ('b', 'f'),
    ('c', 'g'),
    ('d', 'h'),
    ('e', 'h'),
    ('f', 'h'),
    ('g', 'h')
]

class Edge:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end
