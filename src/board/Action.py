from enum import Enum
from dataclasses import dataclass
from typing import List, Iterator


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


class ActionType(Enum):
    """行動の種類を管理する"""

    MOVE = 1
    REMOVE = 2
    BUILD = 3


@dataclass
class Point:
    """座標を管理する"""

    x: int
    y: int


class Action:
    """エージェントの行動を管理する"""

    def __init__(
        self,
        agent_id: int,
        direction: Direction,
        action_type: ActionType,
        point: Point,
    ) -> None:
        assert 0 <= agent_id <= 3
        self.agent_id = agent_id
        self.direction = direction
        self.action_type = action_type
        self.point = point


class Actions:
    def __init__(self, actions: List[Action] = list()) -> None:
        self._lst: List[Action] = actions

    def __len__(self) -> int:
        return len(self._lst)

    def __getitem__(self, index: int) -> Action:
        return self._lst[index]

    def __iter__(self) -> Iterator[Action]:
        return iter(self._lst)

    def append(self, action: Action) -> None:
        self._lst.append(action)

    def check(self) -> bool:
        """すべてのエージェントが過不足なくそろっているか確認"""
        result = False
        for i in range(4):
            if (
                len([action for action in self._lst if action.agent_id == i])
                == 1
            ):
                result = True
            else:
                result = False
                break
        return result
