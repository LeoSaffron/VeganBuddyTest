#!/usr/bin/python
import MySQLdb


class db_connection(object):
    dbname = ""
    hostname = ""
    username = ""
    password = ""
    db = ""
    cur = ""

    # def __init__(self):
    #     return self

    def set_database_parameters(self, dbname, hostname, username, password):
        self.dbname = dbname
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect(self):
        self.db = MySQLdb.connect(host = self.hostname, user = self.username, passwd = self.password, db = self.dbname)
        self.cur = self.db.cursor()

    def query(self, query_text):
        self.cur.execute(query_text)
        self.db.commit()
        return self.cur



#
# def main():
#     print "Hello World"
#     db = DB_connection()
#     cursor = db.query("SELECT * FROM amino_acids")
#     rowcount = int(cursor.rowcount)
#     for i in range(0,rowcount):
#         row = cursor.fetch
#         print row[0], "-->", row[1]
#
# if __name__ == "__main__":
#         main()
