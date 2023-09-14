import abc
from dataclasses import dataclass
from typing import Optional

from engine import Engine

from pydantic import BaseModel


@dataclass
class Car:
    seats: int = None
    engine: Engine = None
    gps: bool = False
    trip_computer: bool = False

    def __str__(self):
        return f"""
         I see physical car:
         SEATS: {self.seats}
         engine stats HP:{self.engine.hp} type: {type(self.engine)}
         gps: {self.gps}
         trip computer: {self.trip_computer}
         """

@dataclass
class Manual:
    title: str = None
    pages: list[str] = None
