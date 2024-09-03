from Utils import Point
from enum import Enum
from typing import Iterator

from Utils import Point


class AgentType(Enum):
    ally = 1
    enemy = 2


class Agent:
    """一人のエージェントを管理する"""
    def __init__(self, agent_id: int, point: Point) -> None:
        self.agent_id = agent_id
        self.point = point

    def __str__(self) -> str:
        return f"Agent {self.agent_id} : {self.point}"


class Agents:
    """１つのチームのすべてのエージェントを管理する"""
    def __init__(self, agent_type: AgentType, points: list[Point]) -> None:
        self.agent_type = agent_type

    def __len__(self) -> int:
        return len(self._lst)

    def __getitem__(self, index: int) -> Agent:
        return self._lst[index]

    def __iter__(self) -> Iterator[Agent]:
        return iter(self._lst)

    def __str__(self) -> str:
        tmp = "\n".join(map(str, self._lst))
        return f"{self.agent_type}:\n{tmp}"

    def append(self, agent: Agent) -> None:
        self._lst.append(agent)

    def check(self) -> bool:
        return True
