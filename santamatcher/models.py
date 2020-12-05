from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True, order=True)
class Person:
    name: str
    communication_address: str


@dataclass(frozen=True, order=True)
class MatchResult:
    giver: Person
    taker: Person


@dataclass(frozen=True)
class MatchRequest:
    people: Tuple[Person]
    required_matches: Tuple[MatchResult]
    forbidden_matches: Tuple[MatchResult]
