from dataclasses import dataclass
from typing import Tuple, FrozenSet


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
    people: Tuple[Person, ...]
    required_matches: FrozenSet[MatchResult]
    forbidden_matches: FrozenSet[MatchResult]

    @classmethod
    def from_dict(cls, data: dict) -> 'MatchRequest':
        people = tuple(
            Person(name=person_data['name'], communication_address=person_data['communication_address'])
            for person_data in data['people']
        )
        name_to_people = {person.name: person for person in people}
        required_matches = frozenset(
            MatchResult(
                giver=name_to_people[match_data['giver_name']],
                taker=name_to_people[match_data['taker_name']],
            )
            for match_data in data['required_matches']
        )
        forbidden_matches = frozenset(
            MatchResult(
                giver=name_to_people[match_data['giver_name']],
                taker=name_to_people[match_data['taker_name']],
            )
            for match_data in data['forbidden_matches']
        )

        return cls(
            people=people,
            required_matches=required_matches,
            forbidden_matches=forbidden_matches,
        )
