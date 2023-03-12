from getpass import getpass
from view import login, mainMenu ,memberMenu,register,tuples_to_dict,searchMenu
from mysql.connector import connect,Error
import re

def search(column):
  print("Enter the "+ column + " 's name or a part of the name :")
  searchWord =input()
  queryString=" select * from books where "+column + " like '%"+searchWord+"%'"
  print (queryString)
  cursor.execute( queryString)
  rows = cursor.fetchall()
  print(row[0])
  column_names=["ISBN","Author","Title","price","subject"]
  my_list= tuples_to_dict(rows ,column_names)
  for object in my_list:
    
      for key, value in object.items():
        print(key + ':', value)
    
      print('---')
     
 
def showSubject (userid):
  try:
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
    if (choice>i-1):
      raise Exception("Please enter the valid subject number, it should be less than or equal ", i-1) 
    cursor.execute("select count(isbn)  from books where subject =%s", (sub[choice-1],))
    row = cursor.fetchone()
    print (row[0],"books available in this subject ")
    queryString = "SELECT * FROM books where subject = '" +sub[choice-1]+"'"
   # showbooks(int(row[0]),sub[choice-1],userid)
    showbooks(int(row[0]),queryString,userid)
  except Exception as e:
                print("An error occurred: ", e)   


def showbooks ( index,query,userid):
   i=0
   more= True
   while i <= index and more==True:
    queryString = f"{query} ORDER BY isbn LIMIT 2 OFFSET {i}"
    print(queryString)
    #cursor.execute("SELECT * FROM books where subject = %s ORDER BY isbn LIMIT 2 OFFSET %s", (choice,i))
    cursor.execute(queryString)
    rows = cursor.fetchall()
    column_names=["ISBN","Author","Tittel","price","subject"]
    my_list= tuples_to_dict(rows ,column_names)
    for object in my_list:
    
      for key, value in object.items():
        print(key + ':', value)
    
      print('---')
     
    print ("Enter ISBN to add to cart ")
    print ("n + enter to browse more ")
    
    alt=input("Enter to go back to menu : ")
    if not alt :
       more = False
    elif alt == 'n':
      i= i+2
    else:
      newTry= True
      while(  newTry):
       if alt == 'q':
        more=False
        newTry=False
       elif not alt.isdigit():
         print("Invalid ISBN, it should contain only numbers")
         alt=input("try again or print q to quit  : ") 
       else: 
         cursor.execute("select * from books where isbn= %s",(alt,))
         row = cursor.fetchone()
         if not row: 
            print("Invalid book's ISBN or Entered book's ISBN does not exists in our Book Shop, please enter the correct ISBN")
            alt=input("try again try again or print q to quit : ")
         else :  
            num=int(input("Enter quantity : "))
            cursor.execute("insert into cart (userid,isbn,qty) values (%s,%s,%s)",(userid,alt,num))
            connection.commit()
            more=False
            newTry=False
       
            
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
                option= memberMenu()
                userid= row[0]
                if option == '1':
                  showSubject(userid)
                elif  option == '2':
                   choice= searchMenu()
                   if choice == '1' :
                      print ("1. Author Search")
                      search("author")
                   elif choice =='2':
                      print ("2. Title Search") 
                      search("title")
                   else :
                      print ("3. Go Back to Main Menu")   
                    #search()
                elif option == '3':
                   print('ö')
                   #checkOut()
                else: 
                   run = False            
         elif option == '2':
              try:
                user_info=register()
                pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
                if not re.match(pattern, user_info["email"]):
                 raise Exception("invalid email")
                insert_query= """ insert into members (fname,lname,address,city,state,zip,phone,email,password) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(insert_query, (user_info["fname"],user_info["lname"],user_info["address"],user_info["city"],user_info["state"],user_info["zip"],user_info["phone"],user_info["email"],user_info["password"],))
                connection.commit()
                print("You have registered successfully!")
                input("Press Enter to go back to Menu")
              except Exception as e:
                print("")
                print("An error occurred: ", e) 
                print ("TRY  AGAIN _______________________________________") 
                print("")
                print("")
         else:
              run = False    
        
        

        # mycursor = connection.cursor()

        # mycursor.execute("SELECT * FROM books")

        # rows = mycursor.fetchall()

        # for row in rows:
        #  print(row)
except Error as e:
    print (e)        


  