from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    """方向を管理する"""

    N = 2
    NE = 3
    E = 4
    SE = 5
    S = 6
    SW = 7
    W = 8
    NW = 1


@dataclass
class Point:
    """座標を管理する"""

    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


def next_point(point: Point, direction: Direction) -> Point:
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
