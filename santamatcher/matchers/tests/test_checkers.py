from typing import Tuple

import pytest

from santamatcher.matchers.checkers import (
    check_match_result, ValidationError, IDENTITY_ERROR_MESSAGE, NOT_SAME_PEOPLE_ERROR_MESSAGE, NOT_CONTAIN_REQUIRED,
    CONTAIN_FORBIDDEN,
)
from santamatcher.matchers.tests.common import PERSON_1, PERSON_2, PERSON_3, PERSON_4
from santamatcher.models import MatchResult

FORBIDDEN_MATCHES = frozenset(
    (MatchResult(giver=PERSON_3, taker=PERSON_1),)
)
REQUIRED_MATCHES = frozenset(
    (MatchResult(giver=PERSON_1, taker=PERSON_2),)
)

NOT_ALL_PEOPLE_IN_MATCHES = (
    MatchResult(giver=PERSON_1, taker=PERSON_2),
    MatchResult(giver=PERSON_2, taker=PERSON_3),
    MatchResult(giver=PERSON_3, taker=PERSON_2),
    MatchResult(giver=PERSON_4, taker=PERSON_1),
)

IDENTITY_IN_MATCHES = (
    MatchResult(giver=PERSON_1, taker=PERSON_2),
    MatchResult(giver=PERSON_2, taker=PERSON_4),
    MatchResult(giver=PERSON_3, taker=PERSON_3),
    MatchResult(giver=PERSON_4, taker=PERSON_1),
)

NOT_ALL_REQUIRED_IN_MATCHES = (
    MatchResult(giver=PERSON_1, taker=PERSON_3),
    MatchResult(giver=PERSON_2, taker=PERSON_1),
    MatchResult(giver=PERSON_3, taker=PERSON_2),
)

ONE_FORBIDDEN_IN_MATCHES = (
    MatchResult(giver=PERSON_1, taker=PERSON_2),
    MatchResult(giver=PERSON_2, taker=PERSON_4),
    MatchResult(giver=PERSON_3, taker=PERSON_1),
    MatchResult(giver=PERSON_4, taker=PERSON_3),
)

CORRECT_MATCHES = (
    MatchResult(giver=PERSON_1, taker=PERSON_2),
    MatchResult(giver=PERSON_2, taker=PERSON_1),
    MatchResult(giver=PERSON_3, taker=PERSON_4),
    MatchResult(giver=PERSON_4, taker=PERSON_3),
)


@pytest.mark.parametrize(("matches", "expected_result"), (
    (NOT_ALL_PEOPLE_IN_MATCHES, (ValidationError(message=NOT_SAME_PEOPLE_ERROR_MESSAGE),)),
    (IDENTITY_IN_MATCHES, (ValidationError(message=IDENTITY_ERROR_MESSAGE),)),
    (NOT_ALL_REQUIRED_IN_MATCHES, (ValidationError(message=NOT_CONTAIN_REQUIRED),)),
    (ONE_FORBIDDEN_IN_MATCHES, (ValidationError(message=CONTAIN_FORBIDDEN),)),
    (CORRECT_MATCHES, tuple()),
))
def test_check_matches(matches: Tuple[MatchResult], expected_result: bool):
    assert check_match_result(
        matches=matches, forbidden_matches=FORBIDDEN_MATCHES, required_matches=REQUIRED_MATCHES
    ) == expected_result
