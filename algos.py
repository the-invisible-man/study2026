import math
from collections import deque

# O(n log n) time
# O(n) space
def merge_sort(arr, left_key, right_key):
    # Keys are inclusive. We prevent creating new isntances
    # of the same array by passing the keys that mark the start
    # and the end of the subarray rather than slicing into new arrays
    # to keep space complexity at O(n)
    length = right_key - left_key + 1

    if left_key >= right_key:
        return

    mid = ((right_key - left_key) // 2) + left_key

    merge_sort(arr, left_key, mid)
    merge_sort(arr, mid+1, right_key)

    # Things get sorted here
    left_tracker = left_key
    right_tracker = mid+1
    aux = []

    # Place sorted values in auxiliary array
    for i in range(length):
        if left_tracker > mid:
            aux.append(arr[right_tracker])
            right_tracker+=1
        elif right_tracker > right_key:
            aux.append(arr[left_tracker])
            left_tracker+=1
        elif arr[left_tracker] > arr[right_tracker]:
            aux.append(arr[right_tracker])
            right_tracker+=1
        else:
            aux.append(arr[left_tracker])
            left_tracker+=1

    aux_left = left_key

    # Replace original array values with values from aux
    for i in range(len(aux)):
        arr[aux_left] = aux[i]
        aux_left+=1

def binary_search(needle, haystack):
    left_pointer = 0
    right_pointer = len(haystack) - 1

    while left_pointer <= right_pointer:
        midpoint = ((right_pointer - left_pointer) // 2) + left_pointer

        if haystack[midpoint] == needle:
            return True
        elif needle > haystack[midpoint]:
            left_pointer = midpoint+1
        else:
            right_pointer = midpoint-1

    return False

class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.previous = None

    def insert(self, value):
        self.head = self._insert(self.head, value)

    def _insert(self, node, value):
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        return self._search(self.head, value)

    def _search(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def pre_order(self, node):
        if node is None:
            return

        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return

        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)

    def level_order(self):
        self._level_order(self.head)

    def _level_order(self, node):
        queue = deque()

        if node is not None:
            queue.append(node)

        total_nodes_remaining_at_current_level = 1
        total_nodes_at_current_level = 1
        total_nodes_at_next_level = 0
        level_counter = 0

        while len(queue) != 0:
            if total_nodes_at_current_level == total_nodes_remaining_at_current_level:
                print("Level " + str(level_counter))

            current = queue.popleft()
            total_nodes_remaining_at_current_level -= 1

            print(current.value)

            if current.left is not None:
                queue.append(current.left)
                total_nodes_at_next_level += 1

            if current.right is not None:
                queue.append(current.right)
                total_nodes_at_next_level += 1

            if total_nodes_remaining_at_current_level == 0:
                total_nodes_remaining_at_current_level = total_nodes_at_next_level
                total_nodes_at_current_level = total_nodes_at_next_level
                total_nodes_at_next_level = 0
                level_counter += 1

    def is_valid_search_tree(self):
        self.previous = None
        return self._is_valid_search_tree(self.head)

    def _is_valid_search_tree(self, node):
        if node is None:
            return True

        if self._is_valid_search_tree(node.left) is False:
            return False

        if self.previous is not None and self.previous > node.value:
            return False

        self.previous = node.value

        if self._is_valid_search_tree(node.right) is False:
            return False

        return True

    def max_depth(self):
        return self._max_depth(self.head)

    def _max_depth(self, node) -> int:
        if node is None:
            return 0

        left_height = self._max_depth(node.left)
        right_height = self._max_depth(node.right)

        return max(left_height, right_height) + 1

    def invert(self, node) -> Node | None:
        if node is None:
            return node

        self.invert(node.right)
        self.invert(node.left)

        tmp = node.left
        node.left = node.right
        node.right = tmp

        return node



my_arr = [1, 2, 3, 5, 8, 13]

# print("pre sort")
#
# print(my_arr)
#
# merge_sort(my_arr, 0, len(my_arr) - 1)
#
# print("sorted")
# print(my_arr)
#
# merge_sort(my_arr, 0, len(my_arr) - 1)
#
# print(binary_search(1, my_arr))

tree = BinarySearchTree()

tree.insert(8)
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(5)
tree.insert(9)
tree.insert(14)

tree.level_order()

