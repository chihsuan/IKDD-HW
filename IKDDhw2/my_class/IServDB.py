# !/usr/bin/evn python
# -*- coding: utf8 -*-
import psycopg2
import sys

class IServDB:

    # initial object
    def __init__(self, db_type, host, db_name, user, passwd, charset, port):
        self.db_type = db_type.lower()
        self.host = host
        self.db_name = db_name
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.port = port

        self.connectdb()

    # connect to database
    # will create a Cursor object which can execute all the quries you need.
    def connectdb(self):
        try:
            self.db = psycopg2.connect( host = self.host,
                    database = self.db_name,
                    user = self.user,
                    password = self.passwd,
                    port = self.port )
            self.cursor = self.db.cursor()
        except:
            print "ERROR: in connectdb"
            sys.exit(1)


    # execute sql statment
    def exe_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            self.db.rollback()
            sys.exit(1)


    def select(self, sql):
        self.exe_sql(sql)
        return self.cursor.fetchall()
    
    # disconnect database
    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()

