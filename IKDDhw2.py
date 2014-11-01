# !/usr/bin/evn python
#-*- coding: utf8 -*-
import sys
import psycopg2

from modules import json_io
from my_class.IServDB import IServDB


def split_text(text):
    if len(text) >= 10:
        line = text[:10]
        text = text[10:]
    else:
        line = text
        text = None
    return text, line

 


if __name__=="__main__":
    if len(sys.argv) != 2:
        print sys.stderr
        exit(-1)
    
    config = json_io.read_json('config.json')[u'database']
    
    mydb = IServDB( config[u'dbtype'], config[u'host'], config[u'dbname'], \
            config[u'username'], config[u'password'], config[u'encoding'], "")

    sql_query =  "SELECT * FROM \"twitter\" WHERE q = '王建民'"
    responese = mydb.select(sql_query)
    print '---------------------------------------------'
    print ("%10s | %10s | %10s" % ("text", "user_name", "user_id"))

    for row in responese:
        text = row[1].decode('utf-8').strip()
        text, line = split_text(text)
        print ("%10s | %7s | %7s\n" % (line, row[2].decode('utf-8'), row[3]))
        while text:
            text, line = split_text(text)
            print line
        print '---------------------------------------------'
    mydb.close()
    

