from functools import reduce
from typing import Tuple
from random import sample

from santamatcher.models import Person, MatchResult


class NotEnoughPeople(Exception):
    pass


def match(people: Tuple[Person]) -> Tuple[MatchResult]:
    if len(people) < 2:
        raise NotEnoughPeople("The number of people to be matched should be higher than 2.")

    gift_givers = people
    gift_takers = sample(gift_givers, len(people))

    while not _are_same_values_on_the_same_positions(gift_givers, gift_takers):
        gift_takers = sample(gift_givers, len(people))

    return tuple(MatchResult(giver=giver, taker=taker) for giver, taker in zip(gift_givers, gift_takers))


def _are_same_values_on_the_same_positions(gift_givers, gift_takers):
    return reduce(
        lambda x, y: x and y,
        (giver != taker for giver, taker in zip(gift_givers, gift_takers)),
        True,
    )
