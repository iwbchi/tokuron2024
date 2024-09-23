# 盤面情報
from collections import deque

import numpy as np
from Agent import Agent, Agents, AgentType
from Utils import Point

territory = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 2, 0, 0, 1, 0, 0, 0],
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
                if territory[toy][tox] != 1:
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
    H = len(territory)
    W = len(territory[0])
    score = 0
    print(g)
    res = bfs(g, 80)
    for i in range(H):
        for j in range(W):
            if not res[i*W+j] and territory[i][j] == 2:
                score += 100
            elif not res[i*W+j] and  territory[i][j] == 1:
                score += 10
            elif not res[i*W+j] :
                score += 30
            else:
                score += 0
    print(score)
                
    # for i in range(H):
    #     for j in range(W):
    #         print(0 if res[i*W+j] else 1 ,end = " ")
    #     print()
            