from typing import Tuple, Iterable, FrozenSet
from random import sample

from santamatcher.matchers.checkers import check_match_result
from santamatcher.models import Person, MatchResult


class NotEnoughPeople(Exception):
    pass


def match(
    people: Tuple[Person], required_matches: FrozenSet[MatchResult], forbidden_matches: FrozenSet[MatchResult],
) -> Tuple[MatchResult]:
    if len(people) < 2:
        raise NotEnoughPeople("The number of people to be matched should be higher than 2.")

    gift_givers = people
    gift_takers = sample(gift_givers, len(people))
    match_result = _create_match_result(gift_givers, gift_takers)

    while check_match_result(match_result, required_matches, forbidden_matches):
        gift_takers = sample(gift_givers, len(people))
        match_result = _create_match_result(gift_givers, gift_takers)

    return match_result


def _create_match_result(givers: Iterable[Person], takers: Iterable[Person]):
    return tuple(MatchResult(giver=giver, taker=taker) for giver, taker in zip(givers, takers))
