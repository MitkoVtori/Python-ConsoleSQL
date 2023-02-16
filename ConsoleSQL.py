import os
import shutil
from colorama import Fore
import errors


def documentation():
    return Fore.GREEN + f'''
Current Functionalities:

- Creating DataBase
- Using/Changing DataBase
- Creating Tables and Files
- Writing in Tables and Files
- Checking the content of Tables and Files
- Deleting DataBases, Tables and Files
- Saves all the code in File.

{Fore.MAGENTA + "All commands can be in upper or lower case!"}

{Fore.GREEN + "1.How to create DataBase:"}
  - At first, you'll be asked to use or create database, 
    - if you choose to create database, it'll just ask you for the name.
  - Otherwise, if you want to create database while working,
    - Use the current command: CREATE DATABASE DataBaseName

2.How to use/change database:
 - At first, you'll be asked to use or create database, 
    - if you choose to use database, it'll just ask you for the name.
 - Otherwise, if you want to change the database you're working with,
    - Use the current command: USE DATABASE DataBaseName

3.How to create a table and save information in it:
 - To create a table, you need to use the main keywords "CREATE TABLE",
    - And then, the name of the table, containing information about the storage,
        - Example: TableName(id: int, name: str)
    - Console command: CREATE TABLE TableName(id: int, name: str, age: float, more...)
 - To write in table, you can see this Example:
        
        {Fore.CYAN + "ADD TableName VALUES ("}
        (id, name, age, more...)
        (id, name, age)
        );

{Fore.GREEN + "4.How to create file and write in it:"}
 - To create a file, use the following command: CREATE FILE FileName
 - To write in file, you need to start with the keywords "WRITE IN FileName:",
    - And then, write whatever you want on every new line.
    - To stop writing, you need to use ";;;" at the end
    "WARNING": """The ;;; get also saved in the txt file, so if you don't want them attached to your text,
            you might write them on new line!
        """
 - Write Example:
        
        
        {Fore.CYAN + "WRITE IN FileName:"}
        Something isn't right.
        Some Messages!
        content, content, content,
        content, content,
        content,
        content,
        content;;;

{Fore.GREEN + "5.How to see the content of my Tables and Files:"}
 - Use this command for Tables: GET ALL TableName
 - Use this command for Files: GET FILE FileName

6.How to delete DataBases, Tables and Files:
 - Delete DataBase/s:
    
    {Fore.MAGENTA + "One DataBase:"}
        FIRST WAY: DROP DB DataBaseName
        SECOND WAY: DROP DATABASE DataBaseName

    More Than One DataBases:
        FIRST WAY: DROP DBS FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
        SECOND WAY: DROP DATABASES FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
 
 {Fore.GREEN + "- Delete Tables:"}
    
    {Fore.MAGENTA + "One Table:"}
        DROP TABLE TableName

    More Than One Table:
        DROP TABLES FirstTableName SecondTableName ThirdTableName...
        
 {Fore.GREEN + "- Delete Files:"}
     
     {Fore.MAGENTA + "One File:"}
        DEL FILE FileName

     More Than One File:
        DEL FILES FirstFileName SecondFileName ThirdFileName...
    
    
    
{Fore.LIGHTGREEN_EX + "7.How to save the code?"}
 - The code is saving by itself in the chosen at the beginning by you file, to change the file
 you must stop the program and rerun it. The file can be found in the same directory "src/filename"
 

Submit issues and questions here: https://github.com/MitkoVtori/Python-ConsoleSQL/issues/new

'''


def create_database(database, *args):
    '''
        Console command
        CREATE DATABASE DataBaseName
    '''

    try:

        os.mkdir(f"databases/{database}"), os.mkdir(f"databases/{database}/files"), os.mkdir(f"databases/{database}/tables")

    except FileExistsError:
        return Fore.WHITE + "Database already exists"

    return Fore.WHITE + f"Database \"{database}\" was created"


def use_database(database, *args):
    '''
        Console command
        USE DATABASE DataBaseName
    '''

    if os.path.exists(f"databases/{database}/"):
        return [Fore.WHITE + f"Currently working with database \"{database}\"", database]

    raise errors.DataBaseNotFoundError(Fore.WHITE + f"Database \"{database}\" not found!")


def create_table(database, table, values, *args):
    '''
        Console command
        CREATE TABLE TableName(id: int, name: str, age: float, more...)
    '''

    if os.path.exists(f"databases/{database}/tables/{table}.txt"):
        return Fore.WHITE + f"Table already exists!"

    table = open(f"databases/{database}/tables/{table}.txt", "a+")
    table.write(f"{values}\n\n")
    table.close()

    return Fore.WHITE + f"Table \"{table}\" was created!"


def add_content_to_table(database, table, *content):
    '''
        Console command

        ADD TableName VALUES (
        (id, name, age, more...)
        (id, name, age)
        );

    '''

    try:

        with open(f"databases/{database}/tables/{table}.txt", "r") as file:

            values = [line for line in file][0]
            values_dictionary = {}

            for item in values[1:-2].split(", "):

                key, value = item.split(": ")
                values_dictionary[key] = value

            with open(f"databases/{database}/tables/{table}.txt", "a+") as write_file:

                for content_list in content:

                    content_dict = {}

                    for index, item in enumerate(values_dictionary.keys()):

                        content_dict[item] = content_list[index]

                        if type(content_dict[item]) is int and values_dictionary[item] == "'int'" or \
                                type(content_dict[item]) is str and values_dictionary[item] == "'str'" or \
                                    type(content_dict[item]) is float and values_dictionary[item] == "'float'":
                                        continue

                        raise errors.ItemValueDifferentThanTheSetValue(f"item \"{item}\" is type \'{type(content_dict[item])}\' and it must be \'{values_dictionary[item]}\'")

                    write_file.write(f"{content_dict}\n")

    except Exception as e:
        raise e

    return Fore.WHITE + "Content added to table!"


def create_file(database, file_name):
    '''
        Console command
        CREATE FILE FileName
    '''

    if os.path.exists(f"databases/{database}/files/{file_name}.txt"):
        return Fore.WHITE + "File already exists"

    file = open(f"databases/{database}/files/{file_name}.txt", 'x')
    file.close()

    return Fore.WHITE + f"File \"{file_name}\" was created!"


def write_in_file(database, file, *content):
    '''
        Console command
        WRITE IN FileName:
        Something isn't right.
        Some Messages!
        content, content, content,
        content, content,
        content,
        content,
        content;;;
    '''

    if os.path.exists(f"databases/{database}/files/{file}.txt"):
        with open(f"databases/{database}/files/{file}.txt", "a+") as f:
            for line in content:
                f.write(f"{line}\n")

        return Fore.WHITE + "Content added to file!"

    return Fore.WHITE + f"Database \"{database}\" or File \"{file}\" not found!"


def check_table_content(database, table, *args):
    '''
        Console command
        GET ALL TableName
    '''

    if os.path.exists(f"databases/{database}/tables/{table}.txt"):
        file = open(f"databases/{database}/tables/{table}.txt", "r")

        return [Fore.WHITE + line for line in file][2:]

    print(Fore.WHITE + "Table not found!")
    return []


def check_file_content(database, file_name, *border):
    '''
        Console command
        GET FILE FileName
    '''

    if os.path.exists(f"databases/{database}/files/{file_name}.txt"):
        file = open(f"databases/{database}/files/{file_name}.txt", "r")

        return [Fore.WHITE + line for line in file]

    print("File not found!")
    return []


def drop_database(*databases):
    '''
        Console command

        One DataBase:
            FIRST WAY: DROP DB DataBaseName
            SECOND WAY: DROP DATABASE DataBaseName

        More Than One DataBases:
            FIRST WAY: DROP DBS FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
            SECOND WAY: DROP DATABASES FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
    '''

    for db in databases:
        if os.path.exists(f"databases/{db}/"):
            shutil.rmtree(f"databases/{db}/")

    return Fore.WHITE + "Database/s dropped!"


def drop_table(database, *tables):
    '''
        Console command

        One Table:
            DROP TABLE TableName

        More Than One Table:
            DROP TABLES FirstTableName SecondTableName ThirdTableName...
    '''

    for table in tables:
        if os.path.exists(f"databases/{database}/tables/{table}.txt"):
            os.remove(f"databases/{database}/tables/{table}.txt")

    return Fore.WHITE + "Table/s dropped!"


def delete_file(database, *files):
    '''
            Console command

            One File:
                DEL FILE FileName

            More Than One File:
                DEL FILES FirstFileName SecondFileName ThirdFileName...
        '''

    for file in files:
        if os.path.exists(f"databases/{database}/files/{file}.txt"):
            os.remove(f"databases/{database}/files/{file}.txt")

    return Fore.WHITE + "File/s deleted!"


def code_saver(user_input, code_file, new_line):
    '''
        Saves the code in the code file.
    '''

    file = open(f"src/{code_file}", "a+")
    file.write(f"{user_input}{new_line}")
    file.close()


def run_program():
    see_documentation = input(Fore.WHITE + "Wanna see the documentation? 'yes' or 'no': ")

    if see_documentation.lower() == "yes":
        print(documentation())

    while True:
        db = input(Fore.WHITE + "create or use database: ")

        if db == 'create':
            create_db = input(Fore.WHITE + "database name: ")
            create_database(create_db)
            d = use_database(create_db)
            break

        elif db == "use":
            d = use_database(input(Fore.WHITE + "database name: "))[-1]
            break

    database = d

    while True:
        file = input(Fore.WHITE + "Create or choose file where to save the code from your console experience:\n")

        if not os.path.exists(f"src/{file}.txt"):
            f = open(f"src/{file}.txt", "x")
            f.close()

        if file:
            break

    file = f"{file}.txt"

    while True:

        operation_code = input()

        if operation_code == "END":
            break

        if operation_code == "docs":
            print(documentation())
            continue

        operation = operation_code.lower().split()

        code_saver(operation_code, file, '\n')

        if len(operation) >= 3:
            if operation[-1]:

                if operation[:-1] == ["create", "database"]:
                    print(create_database(operation[-1]))

                elif operation[:-1] == ["use", "database"]:

                    db = use_database(operation[-1])
                    print(db[0])
                    database = db[-1]

                elif operation[:2] == ["create", "table"]:

                    table_name = ' '.join(operation[2:])[:' '.join(operation[2:]).index("(")]
                    values = ' '.join(operation[2:])[' '.join(operation[2:]).index("(")+1:' '.join(operation[2:]).index(")")]
                    values_tuple = values.split(", ")
                    values_dict = {}

                    for items in values_tuple:

                        key, value = items.split(": ")
                        values_dict[key] = value

                    print(create_table(database, table_name, values_dict))

                elif operation[0] == "add" and operation[-2] == "values":

                    table = operation[1]

                    if operation[-1] == "(":

                        lst_values = []
                        item = input()

                        while item != ");":

                            code_saver(item, file, '\n')
                            items = item[1:-1].split(", ")

                            for index in range(len(items)):

                                if len(items[index].split(".")) == 2:
                                    if items[index].split(".")[0].isdigit() and items[index].split(".")[1].isdigit():
                                        items[index] = float(items[index])

                                elif items[index].isdigit():
                                    items[index] = int(items[index])

                            lst_values.append(items)
                            item = input()

                        code_saver(item, file, '\n\n\n')
                        print(add_content_to_table(database, table, *lst_values))

                elif operation[:-1] == ["create", "file"]:
                    print(create_file(database, operation[-1]))

                elif operation[:-1] == ["write", "in"]:

                    content = []
                    text = input()

                    while text[-3:] != ";;;":

                        code_saver(text, file, '\n')
                        content.append(text)
                        text = input()

                    content.append(text)

                    if operation[-1][-1] == ':':
                        print(write_in_file(database, operation[-1][:-1], *content))

                    else:
                        print(write_in_file(database, operation[-1], *content))

                    code_saver(content[-1], file, '\n\n\n')

                elif operation[0] == "get" and operation[1] == "all":

                    lines = check_table_content(database, operation[-1])
                    print()
                    [print(line) for line in lines]

                elif operation[:-1] == ["get", "file"]:

                    lines = check_file_content(database, operation[-1])
                    print()
                    [print(line) for line in lines]

                elif operation[:-1] == ["drop", "db"] or operation[:-1] == ["drop", "database"] or operation[:2] == \
                    ["drop", "dbs"] or operation[:2] == ["drop", "databases"]:

                    dbs = operation[2:]
                    print(drop_database(*dbs))

                elif operation[:2] == ["drop", "table"] or operation[:2] == ["drop", "tables"]:
                    print(drop_table(database, *operation[2:]))

                elif operation[:2] == ["del", "file"] or operation[:2] == ["del", "files"]:
                    print(delete_file(database, *operation[2:]))

    code_saver('\n// everything bellow is made on new run.', file, '\n')
