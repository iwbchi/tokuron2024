from enum import Enum
from typing import List, Iterator

from Utils import Direction


class ActionType(Enum):
    """行動の種類を管理する"""

    MOVE = 1
    BUILD = 2
    REMOVE = 3


class Action:
    """1つのエージェントの1つ行動を管理する"""

    def __init__(
        self,
        agent_id: int,
        direction: Direction,
        action_type: ActionType,
    ) -> None:
        assert 0 <= agent_id <= 3
        self.agent_id = agent_id
        self.direction = direction
        self.action_type = action_type

    def __str__(self) -> str:
        return f"id: {self.agent_id} dir: {self.direction} Type: {self.action_type}"


class Actions:
    """1チームのすべてのエージェントの行動を管理する"""

    def __init__(self, actions: List[Action] = list()) -> None:
        self._lst: List[Action] = actions

    def __len__(self) -> int:
        return len(self._lst)

    def __getitem__(self, index: int) -> Action:
        return self._lst[index]

    def __iter__(self) -> Iterator[Action]:
        return iter(self._lst)

    def __str__(self) -> str:
        res = [f"({ac})" for ac in self._lst]
        return " ".join(res)

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
