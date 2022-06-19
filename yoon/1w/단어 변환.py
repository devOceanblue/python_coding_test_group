def solution(begin, target, words):
    min_path = float("inf")

    def find_next_nodes(node, visited):
        next_nodes = []
        for word in words:
            count = 0
            for i in range(len(node)):
                if node[i] != word[i]:
                    count += 1
            if count == 1 and word not in visited:
                next_nodes.append(word)
        return next_nodes

    def dfs(node, depth, visited):
        nonlocal min_path
        visited.add(node)
        next_nodes = find_next_nodes(node, visited)

        for next_node in next_nodes:
            if next_node == target:
                min_path = min(min_path, depth)

            dfs(next_node, depth + 1, visited)

    visited = set()
    dfs(begin, 1, visited)
    if min_path == float("inf"):
        min_path = 0
    return min_path


if __name__ == "__main__":
    print(
        solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log"])
    )
