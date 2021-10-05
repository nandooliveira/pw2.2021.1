import psycopg2


class Database():
    Connection = psycopg2.connect(
        host='localhost',
        database='pweb',
        user='postgres',
        password='postgres'
    )

    @classmethod
    def execute(cls, sql, *args, commit=False):
        cursor = Database.Connection.cursor()
        cursor.execute(sql, args)
        if commit:
            Database.Connection.commit()

        return cursor

