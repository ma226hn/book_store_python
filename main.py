from getpass import getpass
from methods import login, mainMenu ,memberMenu,register

from mysql.connector import connect,Error
def showSubject (userid):
  select_query= """ select distinct subject from books"""
  cursor.execute(select_query)
  rows = cursor.fetchall()
  sub= []
  for row in rows:
    sub.append(row[0])

  i=1  
  for item in sub:
    print(i,item)
    i=i+1
  choice =int( input("enter your choice : "))
  cursor.execute("select count(isbn)  from books where subject =%s", (sub[choice-1],))
  row = cursor.fetchone()
  print (row[0],"books available in this subject ")
  showbooks(int(row[0]),sub[choice-1],userid) 
def showbooks ( index,choice,userid):
   i=0
   more= True
   while i <= index and more==True:
    cursor.execute("SELECT * FROM books where subject = %s ORDER BY isbn LIMIT 2 OFFSET %s", (choice,i))
    rows = cursor.fetchall()
    colulist=["ISBN","Author","Tittel","price","subject"]
    for row in rows:
      print(row)
    print ("Enter ISBN to add to cart ")
    print ("n + enter to browse more ")
    
    alt=input("Enter to go back to menu : ")
    if not alt :
       more = False
    elif alt == 'n':
      i= i+2
    else:
      num=int(input("Enter quantity : "))
      cursor.execute("insert into cart (userid,isbn,qty) values (%s,%s,%s)",(userid,alt,num))
      connection.commit()
      more=False
       
            
try :
    with connect (
        host ="localhost",
        user= "root",
        password = "1973!@#m",
        database="book_store",
    ) as connection:
        print(connection)
        cursor = connection.cursor()
        run=True

        while (run):
         option = mainMenu()
         print(option)
         if option == '1':  
             user_login_info=login()
             select_query= """ SELECT userid from members where email = %s and password = %s"""
             cursor.execute(select_query, (user_login_info["email"],user_login_info["password"],))
             row = cursor.fetchone()
             if not row: 
               print("password or email is not correct")
             else :
                userid= row[0]
                option= memberMenu()
                userid= row[0]
                if option == '1':
                  showSubject(userid)
                elif  option == '2':
                   print ('ä')
                    #search()
                elif option == '3':
                   print('ö')
                   #checkOut()
                else: 
                   run = False            
         elif option == '2':
              print ("2")
              user_info=register()
              insert_query= """ insert into members (fname,lname,address,city,state,zip,phone,email,password) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
              cursor.execute(insert_query, (user_info["fname"],user_info["lname"],user_info["address"],user_info["city"],user_info["state"],user_info["zip"],user_info["phone"],user_info["email"],user_info["password"],))
              connection.commit()
              print("You have registered successfully!")
              input("Press Enter to go back to Menu")
         elif option == 'q': 
              run = False    
         else:
            print ("wrong option try agin")
        

        # mycursor = connection.cursor()

        # mycursor.execute("SELECT * FROM books")

        # rows = mycursor.fetchall()

        # for row in rows:
        #  print(row)
except Error as e:
    print (e)        


  