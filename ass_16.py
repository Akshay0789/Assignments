#1
import MySQLdb
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()

import MySQLdb
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()


#2
import MySQLdb
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
   db.close()


import MySQLdb
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()


#3
import MySQLdb
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()