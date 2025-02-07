from prac import dfs_recursive, dfs_stack,island_dfs_stack, island_dfs_recursive, bfs_queue, island_bfs, nqueen,binary_search

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# DFS 스택과 관련있다
assert dfs_recursive(graph, 1, []) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert dfs_stack(graph, 1) == [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]

assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


# BFS 큐와 관련 있다.

assert bfs_queue(graph, 1) == [1, 2, 5, 9, 3, 6, 8, 10, 4, 7]

assert island_bfs(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_bfs(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

# 백트래킹

assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

# 이진탐색

assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1