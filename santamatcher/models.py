from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Person:
    name: str
    communication_address: str


@dataclass(frozen=True, order=True)
class MatchResult:
    giver: Person
    taker: Person
