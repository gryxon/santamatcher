from unittest.mock import patch

from santamatcher.identity_providers import add_secret_identities


@patch('santamatcher.identity_providers.sample')
def test_add_secret_identities(mock_shuffle):
    data = {'people': [
        {'name': f'person_{i}', 'communication_address': f'address_{i}'} for i in range(5)
    ]}
    sample_result = [2, 3, 4, 1, 0]
    mock_shuffle.return_value = sample_result

    add_secret_identities(data)

    assert [person['secret_identity'] for person in data['people']] == sample_result
