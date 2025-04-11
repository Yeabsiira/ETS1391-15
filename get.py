person = {'name': 'Yakob', 'age': 25, 'city': 'Addis Ababa'}
print(person.get('name'))          # Output: Yakob
print(person.get('age'))           # Output: 25 
print(person.get('gender'))        # Output: None
print(person.get('gender', 'N/A')) # Output: N/A
