import random
from node import Node


def to_range(nodes: dict[Node, int]) -> dict[int, Node]:
    ranges: dict[int, Node] = {}
    band = 0

    for node, tendency in nodes.items():
        band += tendency
        ranges[band] = node

    return ranges


def stream_chain(current: Node):
    ranges: dict[str, dict[int, Node]] = {}

    yield current

    while True:
        n = random.random() * 100

        neighbors = current.get_neighbors()

        if current.label not in ranges:
            ranges[current.label] = to_range(neighbors)

        current_range = ranges[current.label]

        for threshold, node in current_range.items():
            if n < threshold:
                current = node
                yield current
                break
