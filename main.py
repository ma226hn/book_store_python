# Name : Manar Alibrahim
# Email : ma226hn@student.lnu.se

from controller import runProgram
from mysql.connector import connect,Error
from getpass import getpass

# Start the program 
try :
  global connection
  with connect (
        host ="localhost",
        user=input("Enter username:   "),
        password=getpass("enter  password:  "),
        database="book_store",
    ) as connection:
        print(connection)
        runProgram(connection)
except Error as e:
    print (e)        
