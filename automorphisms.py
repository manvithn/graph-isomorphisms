import itertools

def generate_automorphisms(num_nodes, edges):
    adj_matrix = [[False]*num_nodes for _ in range(num_nodes)]
    for i, j in edges:
        adj_matrix[i][j] = adj_matrix[j][i] = True

    def check_edges(mapping):
        for i, j in edges:
            if not adj_matrix[mapping[i]][mapping[j]]:
                return False
        return True

    for mapping in itertools.permutations(range(num_nodes)):
        if check_edges(mapping):
            yield mapping

def count_automorphisms(num_nodes, edges):
    return list(generate_automorphisms(num_nodes, edges))

edges = [
    (0, 3), (3, 6), (6, 0), (3, 1),
    (1, 4), (4, 7), (7, 1), (4, 2),
    (2, 5), (5, 8), (8, 2), (5, 0),
]
print(count_automorphisms(9, edges))
