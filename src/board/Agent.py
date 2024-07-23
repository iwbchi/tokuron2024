from Utils import Point
from enum import Enum
from typing import Iterator


class AgentType(Enum):
    ally = 1
    enemy = 2


class Agent:
    def __init__(self, agent_id: int, point: Point) -> None:
        self.agent_id = agent_id
        self.point = point


class Agents:
    def __init__(self, agent_type: AgentType, agents: list[Agent] = list()) -> None:
        self._lst: list[Agent] = agents
        self.agent_type = agent_type

    def __len__(self) -> int:
        return len(self._lst)

    def __getitem__(self, index: int) -> Agent:
        return self._lst[index]

    def __iter__(self) -> Iterator[Agent]:
        return iter(self._lst)

    def append(self, agent: Agent) -> None:
        self._lst.append(agent)

    def check(self) -> bool:
        return True
