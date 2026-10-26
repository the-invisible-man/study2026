from node import Node
from chain import stream_chain
from collections import deque

def target_window(target: str, start: Node) -> list[str]:
    node: Node
    window = deque(maxlen=len(target))
    history: list[str] = []
    target_labels = list(target)

    for node in stream_chain(start):
        window.append(node.get_label())
        history.append(node.get_label())

        if list(window) == target_labels:
            break

    return history
