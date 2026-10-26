class Node:
    def __init__(self, label: str, neighbors: dict["Node", int] | None = None):
        self.label = label
        self.neighbors = neighbors if neighbors is not None else {}

    def get_label(self) -> str:
        return self.label

    def get_neighbors(self) -> dict["Node", int]:
        return self.neighbors

    def add_neighbor(self, node: "Node", distribution) -> None:
        self.neighbors[node] = distribution

    def is_neighbor(self, node: "Node") -> bool:
        return node in self.neighbors
