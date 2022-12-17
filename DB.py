import mysql.connector
from mysql.connector import errorcode, MySQLConnection
import config as db


def aggregateDb():
    try:
        db_connection = MySQLConnection(
            user= db.user, password= db.password, port=db.port, database=db.database)
        print("Database connection made!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)
    else:
        db_connection.connect()

    cursor = db_connection.cursor()

    sql = ("commands")
    cursor.execute(sql)
    db_connection.close()
