from experiments import *
from statistics import median

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')

# Connection
node_a.add_neighbor(node_b, 100)
node_b.add_neighbor(node_a, 20)

# Connection
node_b.add_neighbor(node_c, 40)
node_c.add_neighbor(node_b, 30)

# Connection
node_b.add_neighbor(node_d, 40)
node_d.add_neighbor(node_b, 15)

# Connection
node_c.add_neighbor(node_d, 70)
node_d.add_neighbor(node_c, 85)

target = "ababc"

run_counts = [10, 100, 1000, 5000, 10000, 50000]
results = {}

for R in run_counts:
    move_counts = []

    for _ in range(R):
        move_counts.append(len(target_window(target, node_a)) - 1)

    results[R] = {
        "mean": sum(move_counts) / R,
        "move_counts": move_counts,
    }

for R, result in results.items():
    moves = result["move_counts"]
    print(
        f"Runs: {R}, "
        f"Mean: {result['mean']:.2f}, "
        f"Median: {median(moves)}, "
        f"Longest: {max(moves)}"
    )
