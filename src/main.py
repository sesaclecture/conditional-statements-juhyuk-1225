"""
Implement User Management System
"""
from enum import Enum

class Role(Enum):
    ADMIN = 0
    EDITOR = 1
    VIEWER = 2

todolist = {
    "clare" : {
        '20250828' : {
            'item1':"",
            'item2':""
        }
    },
    "david" :{
        '20250828' : {
            'item1':"",
            'item2':""
        }
    }
}

users = {
    "clare": {
        "name": "Clare",
        "birth": "19980101",
        "id": "clare",
        "password": "1234",
        "role": Role.EDITOR
    },
    "david": {
        "name": "David",
        "birth": "19951212",
        "id": "david",
        "password": "5678",
        "role": Role.VIEWER
    },
    "admin1": {
        "name": "Admin",
        "birth": "19900101",
        "id": "admin1",
        "password": "9999",
        "role": Role.ADMIN
    }
}


mode = input('SignUp:1, Login:2 > ')

if mode == '1':
    new_id = input('new id: ')
    if new_id in users:
        print('id already exists')
    else:
        new_name = input('name: ')
        new_birth = input('birth(YYYYMMDD): ')

        if new_birth.isdigit() and len(new_birth) == 8:
            if "19000101" <= new_birth <= "20250829":
                valid = True
            else:
                valid = False
        else:
            valid = False

        if not valid:
            print('invalid birth date')
        else:
            new_pass = input('new pass (>=3): ')
            if len(new_pass) < 3:
                print('password too short')
            else:
                users[new_id] = {
                    "name": new_name if new_name != "" else new_id,
                    "birth": new_birth,
                    "id": new_id,
                    "password": new_pass,
                    "role": Role.VIEWER
                }
                todolist[new_id] = {}
                print('Sign up success')


login = input('id, pass > ').split()
if len(login) == 2:
    username, password = login
else:
    print('id and pass are space')
    username, password = '', ''

if username in users:
    if users[username]['password'] == password:
        print('Login success')
        user_role = users[username]['role']
        acc = input('Account Edit:1, Delete:2, Skip:3 > ')
        if acc == '1':
            if users[username]['role'] == Role.VIEWER:
                target = username
            else:
                t = input('target id (blank=self): ')
                target = t if t != '' else username

            if target in users:
                nn = input('new name (blank=keep): ')
                nb = input('new birth(YYYYMMDD) (blank=keep): ')
                np = input('new pass (>=3, blank=keep): ')

                if nn != '':
                    users[target]['name'] = nn

                if nb != '':
                    if nb.isdigit() and len(nb) == 8 and "19000101" <= nb <= "20250829":
                        users[target]['birth'] = nb
                    else:
                        print('invalid birth date (keep old)')

                if np != '':
                    if len(np) >= 3:
                        users[target]['password'] = np
                    else:
                        print('password too short (keep old)')

                print('Account updated')
            else:
                print('no such user')

        elif acc == '2':
            if users[username]['role'] == Role.ADMIN:
                t = input('delete target id (blank=self): ')
                target = t if t != '' else username
            else:
                target = username

            if target in users:
                c = input('type YES to confirm: ')
                if c == 'YES':
                    users.pop(target, None)
                    todolist.pop(target, None)
                    print('Account deleted')
                    if target == username:
                        quit()
                else:
                    print('canceled')
            else:
                print('no such user')

        match user_role:
            case Role.ADMIN:
                while True:
                    print('Users:', list(users.keys()))
                    target = input('target user id (blank to exit): ')
                    if target == '':
                        break
                    if target not in users:
                        print('no such user')
                        continue

                    while True:
                        print(todolist)
                        status_in = input('Create:1, Update:2, Delete:3, Back:4')
                        if not status_in.isdigit():
                            print('type number')
                            continue
                        status = int(status_in)

                        if status == 1:
                            sd_in = input('Create -> Date:1, Item:2')
                            if not sd_in.isdigit():
                                print('type number')
                                continue
                            set_dit = int(sd_in)

                            if set_dit == 1:
                                cre_date = input('Create date : ')
                                if target not in todolist:
                                    todolist[target] = {}
                                if cre_date not in todolist[target]:
                                    todolist[target][cre_date] = {}
                                    print(todolist[target])
                                else:
                                    print("There is the date you write")
                            elif set_dit == 2:
                                set_date = input('Set date : ')
                                if target in todolist and set_date in todolist[target]:
                                    ch_i, ch_t = input('Item (space) Thing : ').split()
                                    todolist[target][set_date][ch_i] = ch_t
                                    print(todolist[target])
                                else:
                                    print("There isn't the date you write")
                            else:
                                print('Try agin')

                        elif status == 2:
                            set_date = input('Date : ')
                            if target in todolist and set_date in todolist[target]:
                                print(todolist[target][set_date])
                                set_item, set_thing = input('Item (space) Thing').split()
                                if set_item in todolist[target][set_date]:
                                    todolist[target][set_date][set_item] = set_thing
                                else:
                                    print("There isn't the item you write")
                            else:
                                print("There isn't the date you write")

                        elif status == 3:
                            sd_in = input('Delect -> Date:1, Item:2')
                            if not sd_in.isdigit():
                                print('type number')
                                continue
                            set_dit = int(sd_in)

                            if set_dit == 1:
                                del_date = input('Delect date : ')
                                if target in todolist and del_date in todolist[target]:
                                    todolist[target].pop(del_date)
                                    print(todolist[target])
                                else:
                                    print("There isn't the date you write")
                            elif set_dit == 2:
                                set_date = input('Set date : ')
                                if target in todolist and set_date in todolist[target]:
                                    ch_i = input('Item : ')
                                    todolist[target][set_date].pop(ch_i)
                                else:
                                    print("There isn't the date you write")
                            else:
                                print('Try agin')

                        elif status == 4:
                            break
                        else:
                            print('Try agin')

            case Role.EDITOR:
                while True:
                    print(todolist)
                    status_in = input('Create:1, Update:2, Delete:3, Break:4')
                    if not status_in.isdigit():
                        print('type number')
                        continue
                    status = int(status_in)

                    if status == 1:
                        sd_in = input('Create -> Date:1, Item:2')
                        if not sd_in.isdigit():
                            print('type number')
                            continue
                        set_dit = int(sd_in)

                        if set_dit == 1:
                            cre_date = input('Create date : ')
                            if username not in todolist:
                                todolist[username] = {}
                            if cre_date not in todolist[username]:
                                todolist[username][cre_date] = {}
                                print(todolist[username])
                            else:
                                print("There is the date you write")
                        elif set_dit == 2:
                            set_date = input('Set date : ')
                            if set_date in todolist.get(username, {}):
                                ch_i, ch_t = input('Item (space) Thing : ').split()
                                todolist[username][set_date][ch_i] = ch_t
                                print(todolist[username])
                            else:
                                print("There isn't the date you write")
                        else:
                            print('Try agin')

                    elif status == 2:
                        set_date = input('Date : ')
                        if set_date in todolist.get(username, {}):
                            print(todolist[username][set_date])
                            set_item, set_thing = input('Item (space) Thing').split()
                            if set_item in todolist[username][set_date]:
                                todolist[username][set_date][set_item] = set_thing
                            else:
                                print("There isn't the item you write")
                        else:
                            print("There isn't the date you write")

                    elif status == 3:
                        sd_in = input('Delect -> Date:1, Item:2')
                        if not sd_in.isdigit():
                            print('type number')
                            continue
                        set_dit = int(sd_in)

                        if set_dit == 1:
                            del_date = input('Delect date : ')
                            if del_date in todolist.get(username, {}):
                                todolist[username].pop(del_date)
                                print(todolist[username])
                            else:
                                print("There isn't the date you write")
                        elif set_dit == 2:
                            set_date = input('Set date : ')
                            if set_date in todolist.get(username, {}):
                                ch_i = input('Item : ')
                                todolist[username][set_date].pop(ch_i)
                            else:
                                print("There isn't the date you write")
                        else:
                            print('Try agin')

                    elif status == 4:
                        break
                    else:
                        print('Try agin')

            case Role.VIEWER:
                if username in todolist and len(todolist[username]) > 0:
                    print(todolist[username])
                else:
                    print('(empty)')

            case _:
                print('unknown role')
    else:
        print('Login not matches')
else:
    print(f'{username} is not in users')
