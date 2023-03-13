
from getpass import getpass
from view import loginView, mainMenu ,memberMenu,register,searchMenu,printBooks,inputNumber
import re

def showMemberMenu():
   option= memberMenu()
   if option == '1':
    showSubject()
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
     #logout
     run = False    
def showSubject ():
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
    queryString = f"where subject ='{sub[choice-1]}'"
    getBooksNumber(queryString)
   
  except Exception as e:
                print("An error occurred: ", e) 


def getBooksNumber(query):
    cursor.execute(f"select count(isbn)  from books {query}")
    row = cursor.fetchone()
    print ("=============================")
    print (row[0],"books available ")
    print ("=============================")
    showBooks(int(row[0]),query)

def showBooks(index,query):
   i=0
   more= True
   while i <= index and more==True:
     queryString = f"select * from books {query} ORDER BY isbn LIMIT 2 OFFSET {i}"
     cursor.execute(queryString)
     rows = cursor.fetchall()
     alt =printBooks(rows)
     
     if not alt :
       more = False
     elif alt == 'n':
      i= i+2
      if i > index :
         print ("=============================")
         print ("No More Books back to the begin ")
         print ("=============================")
         i=0
     else:
      buyBook(alt)
   showMemberMenu()   
def buyBook(alt):
   while not alt == 'q':
       
       if not alt.isdigit():
         print("Invalid ISBN, it should contain only numbers")
         alt=input("try again or print q to quit  : ") 
       else: 
         cursor.execute("select * from books where isbn= %s",(alt,))
         row = cursor.fetchone()
         if not row:  
            print("Invalid book's ISBN or Entered book's ISBN does not exists in our Book Shop, please enter the correct ISBN")
            alt=input(" try again or print q to quit : ")
         else : 
            print("Enter quantity") 
            num=inputNumber()
            queryString =f"SELECT qty from cart where isbn ='{alt}'"
            cursor.execute(queryString)
            row=cursor.fetchone()
            if not num == '0':
              if not row  :
               cursor.execute("insert into cart (userid,isbn,qty) values (%s,%s,%s)",(userId,alt,num))
               connection.commit()
               print (" the book added to the cart")
               alt=input("enter a ISBN number to buy a new book or q to quit")
              else :
                cursor.execute("update cart set qty = %s where isbn =%s",(alt,num))
                connection.commit()
                print ("the number of the book updated")
                alt=input("enter a ISBN number to buy a new book or q to quit")
            
                  

def login():
    user_login_info=loginView()
    select_query= """ SELECT userid from members where email = %s and password = %s"""
    cursor.execute(select_query, (user_login_info["email"],user_login_info["password"],))
    row = cursor.fetchone()
    if not row: 
      print("password or email is not correct")
      print("enter  t  to try again or  any letter  to back to the main menu")
      alt = input()
      if alt == 't':
       login()         
    else :
      global userId
      userId= row[0]
      showMemberMenu()
      
def search(column):
  print("Enter the "+ column + " 's name or a part of the name :")
  searchWord =input()
  queryString="where "+ column + " like '%"+searchWord+"%'"
  getBooksNumber(queryString)
  
     
def runProgram(connect):    
        global connection 
        connection =connect
        global cursor
        cursor= connection.cursor()
        run=True
        while (run):
         option = mainMenu()
         print(option)
         if option == '1':  
           login()         
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
        
        