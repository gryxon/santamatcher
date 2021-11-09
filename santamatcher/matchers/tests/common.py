from santamatcher.models import Person

PEOPLE = tuple(Person(name=f'person_{i}', communication_address=f'address_{i}', secret_identity=i) for i in range(5))
PERSON_1, PERSON_2, PERSON_3, PERSON_4, PERSON_5 = PEOPLE
