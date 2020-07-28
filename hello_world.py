import collections


person_type = collections.namedtuple('person', ['first_name', 'last_name', 'age'])
print(person_type.first_name)