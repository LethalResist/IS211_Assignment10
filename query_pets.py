import os
import sqlite3
import sys


DB_FILE = 'pets.db'
EXIT_ID = -1

PERSON_QUERY = 'SELECT first_name, last_name, age FROM person WHERE id = ?'

PETS_QUERY = '''
SELECT pet.name, pet.breed, pet.age, pet.dead
FROM pet
JOIN person_pet ON pet.id = person_pet.pet_id
WHERE person_pet.person_id = ?
ORDER BY pet.id
'''


def years_old(age):
    return f'{age} year{"" if age == 1 else "s"} old'


def article(word):
    return 'an' if word[:1].lower() in 'aeiou' else 'a'


def show_person(cursor, person_id):
    cursor.execute(PERSON_QUERY, (person_id,))
    person = cursor.fetchone()

    if person is None:
        print(f'Error: no person found with ID {person_id}')
        return

    first_name, last_name, age = person
    full_name = f'{first_name} {last_name}'
    print(f'{full_name}, {years_old(age)}')

    cursor.execute(PETS_QUERY, (person_id,))
    pets = cursor.fetchall()

    if not pets:
        print(f'{full_name} has no pets')

    for name, breed, pet_age, dead in pets:
        owns, is_ = ('owned', 'was') if dead else ('owns', 'is')
        print(f'{full_name} {owns} {name}, {article(breed)} {breed}, '
              f'that {is_} {years_old(pet_age)}')


def main():
    print('Running query_pets.py')

    if not os.path.exists(DB_FILE):
        print(f'Error: {DB_FILE} not found. Run load_pets.py first.')
        sys.exit(1)

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    try:
        while True:
            entry = input(f"\nEnter a person's ID number ({EXIT_ID} to exit): ")

            try:
                person_id = int(entry)
            except ValueError:
                print('Error: please enter a whole number')
                continue

            if person_id == EXIT_ID:
                break

            show_person(cursor, person_id)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
