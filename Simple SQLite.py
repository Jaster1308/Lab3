import sqlite3
import traceback

db_name = 'knives.db'

def main():


    #call the design
    while True:
        make_db()
        choice = display_options()
        if choice == '1':
            add_player()
        elif choice == '2':
            search_player()
        elif choice == '3':
            break
        elif choice == '4':
            del_player()
        elif choice == '5':
            show_all()
        else:
            break

def make_db():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('create table if not exists records (name text, country text, catches int)')

def add_player():
    # get player data
    name = input("What's his name? ")
    country = input("What's his country? ")
    catches = int(input('How many catches? '))
    add_to_db(name, country, catches)

def search_player():
    with sqlite3.connect(db_name) as db:
        new_data = input('What name? ')
        cur = db.cursor()
        result = cur.execute('select * from records WHERE name=?', (new_data,))
        for row in result:
            print(row)
def del_player():
    with sqlite3.connect(db_name) as db:
        deleting = input('What name? ')
        cur = db.cursor()
        result = cur.execute('delete from records where name=?', (deleting,))
        for row in result:
            print(row)
        for list in db.cursor().execute('select * from records'):
            print(list)

def add_to_db(name, country, catches):
    # get data from add_player()
    try:
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            cur.execute('insert into records values (?, ?, ?)', (name, country, catches))
    except sqlite3.Error as e:
        print('rolling back to the last edit: ', e)
        traceback.print_exc()
        db.rollback()

def show_all():
    with sqlite3.connect(db_name) as db:
        for r in db.cursor().execute('select * from records'):
            print(r)

def display_options():
    # create the options
    print("""
        1. Add a player
        2. Search a player
        3. Edit a Player
        4. Delete a Player
        5. Show All
    """)
    return input('Enter choice: ')



if __name__ == '__main__':
    main()