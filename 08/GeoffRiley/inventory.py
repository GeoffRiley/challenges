import sqlite3
from enum import Enum
from typing import Union

DB_FILENAME = 'inventory.sqlite'
MAIN_CHOICES = '1234q'


class Choices(Enum):
    list_rooms = '1'
    select_rooms = '2'
    add_room = '3'
    delete_room = '4'
    quit_program = 'q'

    @classmethod
    def select(cls, val: str) -> Union[Enum, None]:
        for name, elem in cls.__members__.items():
            if elem.value == val:
                return elem
        return None


class Inventory(object):
    db: sqlite3

    def __init__(self):
        pass

    def __enter__(self):
        """ Open up or create our database """
        self.db = sqlite3.connect(DB_FILENAME)
        self.db_check()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Close the database at exit """
        self.db.close()

    def commit(self):
        self.db.commit()

    @property
    def cursor(self):
        return self.db.cursor()

    def db_check(self):
        """
        Check that the database tables are in place,
        and create them if not.
        """
        SQL = """
        SELECT count(*) 
        FROM sqlite_master 
        WHERE type='table' AND name='room'
        """
        cur = self.cursor
        cur.execute(SQL)
        # the room table doesn't exist: create it
        if cur.fetchone()[0] == 0:
            SQL1 = """
            CREATE TABLE room (
                id  integer PRIMARY KEY,
                name varchar(20)
            );
            """
            SQL2 = """
            CREATE TABLE contents (
                id integer PRIMARY KEY,
                room_id integer,
                name varchar(20),
                cost integer
            );
            """
            cur.execute(SQL1)
            cur.execute(SQL2)
            self.commit()

    def get_rooms(self):
        SQL = """SELECT id, name FROM room"""
        cur = self.cursor
        cur.execute(SQL)
        return cur.fetchall()

    def get_room_names(self):
        return [r for _, r in self.get_rooms()]

    def add_room(self, new_room_name):
        SQL = """INSERT INTO room (name) VALUES (?)"""
        cur = self.cursor
        cur.execute(SQL, [new_room_name])
        self.commit()


def menu_option():
    print('''Household Inventory: Menu
    
    1 List rooms
    2 Select room
    3 Add room
    4 Delete room
    
    q Quit and exit program
    ''')
    choice = ' '
    while choice not in MAIN_CHOICES:
        choice = input('Select an option: ')
        if choice not in MAIN_CHOICES:
            print(f'Please select from [{", ".join(MAIN_CHOICES)}]')
    return Choices.select(choice)


def list_rooms(inv: Inventory):
    ind = 0
    for room in inv.get_room_names():
        ind += 1
        print(f'{ind:>02} {room}')
    if ind == 0:
        print('\n*** No rooms defined\n')


def select_room(inv: Inventory):
    pass


def add_room(inv: Inventory):
    new_room_name = input('Enter new room name: ')
    if new_room_name in inv.get_room_names():
        print('Room name already exists.')
        return
    inv.add_room(new_room_name)


def delete_room(inv: Inventory):
    pass


def main():
    inv: Inventory
    with Inventory() as inv:
        while True:
            opt = menu_option()
            if opt == Choices.quit_program:
                break
            if opt == Choices.list_rooms:
                list_rooms(inv)
            if opt == Choices.select_rooms:
                select_room(inv)
            if opt == Choices.add_room:
                add_room(inv)
            if opt == Choices.delete_room:
                delete_room(inv)


if __name__ == "__main__":
    main()
