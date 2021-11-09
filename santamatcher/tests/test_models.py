from pytest import fixture

from santamatcher.models import MatchRequest, Person, MatchResult


@fixture
def input_data():
    return {
        'people': [
            {'name': 'Kamil', 'communication_address': '1', 'secret_identity': 0},
            {'name': 'Ola', 'communication_address': '2', 'secret_identity': 1},
            {'name': 'Kasia', 'communication_address': '3', 'secret_identity': 2},
            {'name': 'Anna', 'communication_address': '4', 'secret_identity': 3},
        ],
        'forbidden_matches': [
            {'giver_name': 'Kamil', 'taker_name': 'Kasia'},
            {'giver_name': 'Kasia', 'taker_name': 'Kamil'},
        ],
        'required_matches': [
            {'giver_name': 'Kamil', 'taker_name': 'Ola'},
        ],
    }


@fixture
def expected_match_request():
    person_1 = Person(name='Kamil', communication_address='1', secret_identity=0)
    person_2 = Person(name='Ola', communication_address='2', secret_identity=1)
    person_3 = Person(name='Kasia', communication_address='3', secret_identity=2)
    person_4 = Person(name='Anna', communication_address='4', secret_identity=3)
    return MatchRequest(
        people=(person_1, person_2, person_3, person_4),
        forbidden_matches=frozenset((
            MatchResult(giver=person_1, taker=person_3),
            MatchResult(giver=person_3, taker=person_1),
        )),
        required_matches=frozenset((
            MatchResult(giver=person_1, taker=person_2),
        )),
    )


def test_creation_match_request_from_dict(input_data, expected_match_request):
    match_request = MatchRequest.from_dict(input_data)

    assert match_request == expected_match_request
