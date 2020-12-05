from dataclasses import dataclass
from typing import Tuple, FrozenSet, Optional

from santamatcher.models import MatchResult


@dataclass(frozen=True, order=True)
class ValidationError:
    message: str


IDENTITY_ERROR_MESSAGE = "Somebody gives present to his own"
NOT_SAME_PEOPLE_ERROR_MESSAGE = "Givers and Takers are not same people"
NOT_CONTAIN_REQUIRED = "There is no all required matches in the result"
CONTAIN_FORBIDDEN = "There is at least one forbidden matches in the result"


def check_match_result(
        matches: Tuple[MatchResult],
        required_matches: FrozenSet[MatchResult],
        forbidden_matches: FrozenSet[MatchResult],
) -> Tuple[ValidationError]:
    matches_set = frozenset(matches)
    givers = sorted(match.giver for match in matches)
    takers = sorted(match.taker for match in matches)
    not_identity_matches = next(
        (match for match in matches if match.giver == match.taker), None,
    ) is None

    errors = [
        _create_error_if_occured(NOT_SAME_PEOPLE_ERROR_MESSAGE, givers != takers),
        _create_error_if_occured(IDENTITY_ERROR_MESSAGE, not not_identity_matches),
        _create_error_if_occured(NOT_CONTAIN_REQUIRED, not required_matches.issubset(matches_set)),
        _create_error_if_occured(
            CONTAIN_FORBIDDEN, forbidden_matches.intersection(matches_set) != frozenset(),
        ),
    ]
    return tuple(error for error in errors if error is not None)


def _create_error_if_occured(message: str, was_occured: bool) -> Optional[ValidationError]:
    return ValidationError(message=message) if was_occured else None
