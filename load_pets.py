import sqlite3


DB_FILE = 'pets.db'

SCHEMA = '''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER
);
'''

PEOPLE = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
]

PETS = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1),
]

PERSON_PETS = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
]


def load_data(connection):
    cursor = connection.cursor()
    cursor.executescript(SCHEMA)

    cursor.execute('DELETE FROM person_pet')
    cursor.execute('DELETE FROM pet')
    cursor.execute('DELETE FROM person')

    cursor.executemany(
        'INSERT INTO person (id, first_name, last_name, age) '
        'VALUES (?, ?, ?, ?)', PEOPLE)
    cursor.executemany(
        'INSERT INTO pet (id, name, breed, age, dead) '
        'VALUES (?, ?, ?, ?, ?)', PETS)
    cursor.executemany(
        'INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)',
        PERSON_PETS)

    connection.commit()


def main():
    print('Running load_pets.py')
    connection = sqlite3.connect(DB_FILE)
    try:
        load_data(connection)
    finally:
        connection.close()
    print(f'Loaded {len(PEOPLE)} people, {len(PETS)} pets, and '
          f'{len(PERSON_PETS)} person_pet rows into {DB_FILE}')


if __name__ == '__main__':
    main()
