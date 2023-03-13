from controller import runProgram
from mysql.connector import connect,Error

try :
  global connection
  with connect (
        host ="localhost",
        user= "root",
        password = "1973!@#m",
        database="book_store",
    ) as connection:
        print(connection)
        runProgram(connection)
        # mycursor = connection.cursor()

        # mycursor.execute("SELECT * FROM books")

        # rows = mycursor.fetchall()

        # for row in rows:
        #  print(row)
except Error as e:
    print (e)        
