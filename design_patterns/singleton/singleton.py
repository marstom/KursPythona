


class Database:
    conn = ""
    command = ""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance



if __name__ == '__main__':
    db1 = Database()
    db1.conn = "asdf"
    db1.command = "SELEC * FROM users;"
    print(db1.conn, db1.command)

    db2 = Database()
    print(db2.conn, db2.command)
    db2.conn = 'a'

    print(db1.conn, db1.command)


