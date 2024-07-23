from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    """方向を管理する"""

    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


@dataclass
class Point:
    """座標を管理する"""

    x: int
    y: int


def next_point(point, direction):
    """座標と動作方向から、次の座標を計算する"""

    if direction == Direction.N:
        return Point(point.x, point.y - 1)
    elif direction == Direction.NE:
        return Point(point.x + 1, point.y - 1)
    elif direction == Direction.E:
        return Point(point.x + 1, point.y)
    elif direction == Direction.SE:
        return Point(point.x + 1, point.y + 1)
    elif direction == Direction.S:
        return Point(point.x, point.y + 1)
    elif direction == Direction.SW:
        return Point(point.x - 1, point.y + 1)
    elif direction == Direction.W:
        return Point(point.x - 1, point.y)
    elif direction == Direction.NW:
        return Point(point.x - 1, point.y - 1)
    else:
        return point
