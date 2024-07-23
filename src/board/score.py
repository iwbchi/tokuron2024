# 盤面情報
from collections import deque

import numpy as np
from Agent import Agent, Agents, AgentType
from Utils import Point

territory = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
]

def make_grid_graph(territory):
    W = len(territory[0])
    H = len(territory)
    graph = [[] for _ in range(H*W + 1)]
    dl = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for h in range(H):
        for w in range(W):
            if territory[h][w] == 1:
                continue
            for dx, dy in dl:
                if not (0 <= w+dx < W and 0 <= h+dy < H):
                    continue
                tox, toy = w+dx, h+dy
                if territory[toy][tox] == 0:
                    graph[h * W + w].append(toy * W + tox)

            # ノードH*Wについて端に行けるようにする
            if h == 0 or h == H-1 or w == 0 or w == W-1:
                graph[H * W].append(h*W + w)

    return graph


def bfs(graph, start):
    W = len(territory[0])
    H = len(territory)
    queue = deque([start])
    visited = [False] * (H*W+1)
    visited[start] = True

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return visited

if __name__ == "__main__":
    g = make_grid_graph(territory)
    print(g)
    res = bfs(g, 80)
    for i, r in enumerate(res[:-1]):
        print(1 if r else 0, end=" ")
        if i % 10 == 9:
            print()
