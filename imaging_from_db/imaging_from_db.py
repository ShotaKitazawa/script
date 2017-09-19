#!/usr/bin/python3

import MySQLdb
import re

conn = MySQLdb.connect(
        user='root',
        passwd='',
        host='localhost',
        db='isuconp',
        )
c = conn.cursor()

path = "/home/isucon/private_isu/webapp/public/image/"

sql = 'SELECT COUNT(id) FROM posts'
c.execute(sql)

for i in range(1, c.fetchone()[0]+1):
    sql = 'SELECT id, imgdata FROM posts WHERE id = ' + str(i)
    c.execute(sql)
    extension = ""
    row = c.fetchone()
    if re.compile(b'\xff\xd8').match(row[1]): # jpg
        extension = "jpg"
    elif re.compile(b'\x89\x50\x4e\x47').match(row[1]): # png
        extension = "png"
    elif re.compile(b'\x47\x49\x46\x38').match(row[1]): # gif
        extension = "gif"
    with open(path + str(row[0]) + "." + extension,  "w") as file:
        file.write(row[1])
