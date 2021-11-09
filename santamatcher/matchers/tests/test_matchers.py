from unittest.mock import patch

import pytest

from santamatcher.matchers.matchers import match, NotEnoughPeople
from santamatcher.matchers.tests.common import PERSON_1, PERSON_2, PERSON_4, PERSON_5, PERSON_3, PEOPLE
from santamatcher.models import Person, MatchResult


def people_random_sampling_result_for_2_people_same_positions():
    return PERSON_1, PERSON_2


def people_random_sampling_result_for_2_people_different_positions():
    return PERSON_2, PERSON_1


def people_random_sampling_result_for_5_people_some_same_positions_variant_1():
    return PERSON_1, PERSON_2, PERSON_4, PERSON_5, PERSON_3


def people_random_sampling_result_for_5_people_some_same_positions_variant_2():
    return PERSON_1, PERSON_3, PERSON_4, PERSON_5, PERSON_2


def people_random_sampling_result_for_5_people_some_same_positions_variant_3():
    return PERSON_5, PERSON_2, PERSON_3, PERSON_4, PERSON_1


def people_random_sampling_result_for_5_people_different_positions_variant_1():
    return PERSON_5, PERSON_4, PERSON_2, PERSON_3, PERSON_1


def people_random_sampling_result_for_5_people_different_positions_variant_2():
    return PERSON_3, PERSON_1, PERSON_2, PERSON_5, PERSON_4


@pytest.mark.parametrize('people', (
    tuple(),
    (Person(name='dummy_name', communication_address='communication_address', secret_identity=0), )
))
def test_match_should_raise_when_people_not_enough(people):
    with pytest.raises(NotEnoughPeople):
        match(people, frozenset(), frozenset())


@pytest.mark.parametrize(('number_of_people', 'results_of_random_sampling'), (
    (
        2,
        (
            people_random_sampling_result_for_2_people_different_positions(),
        )
    ),
    (
        2,
        (
            people_random_sampling_result_for_2_people_same_positions(),
            people_random_sampling_result_for_2_people_different_positions(),
        )
    ),
    (
        5,
        (
            people_random_sampling_result_for_5_people_different_positions_variant_1(),
        )
    ),
    (
        5,
        (
            people_random_sampling_result_for_5_people_different_positions_variant_2(),
        )
    ),
    (
        5,
        (
            people_random_sampling_result_for_5_people_some_same_positions_variant_1(),
            people_random_sampling_result_for_5_people_some_same_positions_variant_2(),
            people_random_sampling_result_for_5_people_some_same_positions_variant_3(),
            people_random_sampling_result_for_5_people_different_positions_variant_1(),
        )
    ),
    (
        5,
        (
            people_random_sampling_result_for_5_people_some_same_positions_variant_2(),
            people_random_sampling_result_for_5_people_some_same_positions_variant_3(),
            people_random_sampling_result_for_5_people_some_same_positions_variant_1(),
            people_random_sampling_result_for_5_people_different_positions_variant_2(),
        )
    ),
))
def test_match(number_of_people, results_of_random_sampling):
    input_people = PEOPLE[:number_of_people]
    with patch('santamatcher.matchers.matchers.sample') as mock_sampling:
        mock_sampling.side_effect = results_of_random_sampling
        expected_result = tuple(
            MatchResult(giver=giver, taker=taker)
            for giver, taker in zip(input_people, results_of_random_sampling[-1])
        )

        match_results = tuple(match(input_people, frozenset(), frozenset()))

        assert sorted(match_results) == sorted(expected_result)
