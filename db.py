import sqlite3

import excel_reader as er

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_lltrs (
                                id INTEGER PRIMARY KEY,
                                Fcode TEXT NOT NULL,
                                Code TEXT NOT NULL,
                                Name TEXT NOT NULL,
                                Price INTEGER NOT NULL,
                                Pice_ad INTEGER NOT NULL,
                                Par TEXT NOT NULL,
                                PN TEXT NOT NULL
                                );'''
    cursor = sqlite_connection.cursor()

    df_from_exel = er.ReadEx.lltrsDf
    df_columns_list = df_from_exel.columns
    # print(df_columns_list)
    df_from_exel.to_sql(“sqlitedb_lltrs”, con = sqlite_connection, if_exists =”append”, index = False)

    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
