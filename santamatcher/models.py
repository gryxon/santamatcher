from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    communication_address: str


@dataclass(frozen=True)
class MatchResult:
    giver: Person
    taker: Person
