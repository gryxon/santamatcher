from random import sample


def add_secret_identities(data: dict):
    secret_identities = sample([*range(len(data['people']))], len(data['people']))
    for i, identity in enumerate(secret_identities):
        data['people'][i]['secret_identity'] = identity
