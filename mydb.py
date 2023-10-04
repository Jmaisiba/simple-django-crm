#import mysql connector
import mysql.connector

#create a db connection using a variable
#designate host,user & password
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'mvmcHNB10!'

	)


#prepare a cursor object
cursorObject = dataBase.cursor()


#create the db
cursorObject.execute("CREATE DATABASE crmdb")


print ("DB created")