from peewee import *

db = SqliteDatabase('chainsawrecords.sqlite')

"""
A menu - you need to add the database and fill in the functions. 
"""

class Chainsaw(Model):
    name = CharField()
    country = CharField()
    number_catches = IntegerField()

    class Meta: 
        database = db
    
    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.number_catches}'

db.connect()
db.create_tables([Chainsaw])

Chainsaw.delete().execute() # to clear table during testing only

# Enter some sample data
mustonen = Chainsaw(name='Janne Mustonen', country='Finland', number_catches=98)
mustonen.save()
stewart = Chainsaw(name='Ian Stewart', country='Canada', number_catches=94)
stewart.save()
gregg = Chainsaw(name='Aaron Gregg', country='Canada', number_catches=88)
gregg.save()
taylor = Chainsaw(name='Chad Taylor', country='USA', number_catches=78)
taylor.save()


def main():
    menu = {}
    menu['1']='Display all records'
    menu['2']='Search by name'
    menu['3']='Add new record'
    menu['4']='Edit existing record'
    menu['5']='Delete record'
    menu['6']='Quit'

    options=menu.keys()
    for option in options:
        print(option, menu[option])

    choice = input('Enter your choice: ')
    if choice == '1':
        display_all_records()
    elif choice == '2':
        search_by_name()
    elif choice == '3':
        add_new_record()
    elif choice == '4':
        edit_existing_record()
    elif choice == '5':
        delete_record()
    elif choice == '6':
        print('Quitting program.')
    else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')
    all_chainsaw_records = Chainsaw.select()

    for chainsaw in all_chainsaw_records:
        print(chainsaw)


def search_by_name():
    user_name_input = input('Enter a name to search for: ')
    user_search = Chainsaw.get_or_none(name=user_name_input)
    print(user_search)


def add_new_record():
    new_name = input('Enter a name for the new record: ')
    rows_containing_name = Chainsaw.select().where(Chainsaw.name == new_name).count()

    if rows_containing_name == 0:
        new_country = input('Enter a country for the new record: ')
        new_number_catches = input('Enter the number of catches for the new record: ')

        new_entry = Chainsaw(name=new_name, country=new_country, number_catches=new_number_catches)
        new_entry.save()
    else:
        print('Sorry, this name already has an entry.')

    print_upated_records()


def edit_existing_record():
    name_input = input('Enter the name of the record to change: ')

    rows_containing_name = Chainsaw.select().where(Chainsaw.name == name_input).count()

    if rows_containing_name == 0:
        print('Sorry, the record you are attempting to edit does not exist.')
    else:
        new_number_catches = input('Enter the updated number of catches: ')
        Chainsaw.update(number_catches = new_number_catches).where(Chainsaw.name == name_input).execute()

    print_upated_records()


def delete_record():
    name_input = input('Enter the name of the record to change: ')

    rows_containing_name = Chainsaw.select().where(Chainsaw.name == name_input).count()

    if rows_containing_name == 0:
        print('Sorry, the record you are attempting to delete does not exist.')
    else:
        Chainsaw.delete().where(Chainsaw.name == name_input).execute()

    print_upated_records()


def print_upated_records():
    print('Here are the updated records: ')
    all_chainsaw_records = Chainsaw.select()
    for chainsaw in all_chainsaw_records:
        print(chainsaw)


if __name__ == '__main__':
    main()