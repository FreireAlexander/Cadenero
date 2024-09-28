"""
Lines:

start: Coordinate
end: Coordinate

"""
from typing import TypeAlias

Coordinate: TypeAlias = None

class Line():

    __slots__ = ("start", "end")

    def __init__(self, start: Coordinate, end: Coordinate) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"[{self.start}, {self.end}]"