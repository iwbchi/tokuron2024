# 盤面情報
from collections import deque
from Board import Board
import numpy as np


# territory = [
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 2, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#     [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
# ]


def make_grid_graph(territory):
    W = len(territory[0])
    H = len(territory)
    graph = [[] for _ in range(H * W + 1)]
    dl = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for h in range(H):
        for w in range(W):
            if territory[h][w] == 1:
                continue
            for dx, dy in dl:
                if not (0 <= w + dx < W and 0 <= h + dy < H):
                    continue
                tox, toy = w + dx, h + dy
                if territory[toy][tox] != 1:
                    graph[h * W + w].append(toy * W + tox)

            # ノードH*Wについて端に行けるようにする
            if h == 0 or h == H - 1 or w == 0 or w == W - 1:
                graph[H * W].append(h * W + w)

    return graph


def bfs(territory, graph, start):
    W = len(territory[0])
    H = len(territory)
    queue = deque([start])
    visited = [False] * (H * W + 1)
    visited[start] = True

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return visited


def get_score(board: Board, is_ally: bool):
    territory = None
    # 0 : 中立,  2 : 城壁
    if is_ally:
        territory = board.board_territory_ally
    else:
        territory = board.board_territory_enemy
    territory = np.where(territory == 2, 1, 0)
    # 0: 空白, 1: 堀, 2: 城

    for i in range(len(territory)):
        for j in range(len(territory[0])):
            if board.board_obj[i][j] == 0:
                continue
            territory[i][j] = board.board_obj[i][j]

    g = make_grid_graph(territory)
    H = len(territory)
    W = len(territory[0])
    score = 0
    res = bfs(territory, g, H * W)
    # for i in range(H):
    #     for j in range(W):
    #         print(0 if res[i*W+j] else 1 ,end = " ")
    #     print()
    for i in range(H):
        for j in range(W):
            # 堀ならスキップ
            if board.board_obj[i][j] == 1:
                continue
            # 領域外ならスキップ
            if res[i * W + j]:
                continue

            if territory[i][j] == 2:
                score += 100
            elif territory[i][j] == 1:
                score += 10
            else:
                score += 30
    return score


if __name__ == "__main__":
    board = Board()
    score = get_score(board, True)
    print(score)
