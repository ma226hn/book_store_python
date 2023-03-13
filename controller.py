
from getpass import getpass
from view import loginView, mainMenu ,memberMenu,registerView,searchMenu,printBooks,inputNumber,printCart,tuples_to_dict
import re
from datetime import datetime, timedelta
def checkOut():
   queryString= f"SELECT books.title, books.price,books.isbn, cart.qty  FROM books,cart  where books.isbn = cart.isbn and cart.userid = '{userId}'"
   cursor.execute(queryString)
   row = cursor.fetchone()
   if row :
     column_names=["Title","price","isbn","qty","total"]
     choice= printCart(row,column_names)
     if (choice == 'y' or choice == 'Y'):
       makeOrder(row)
     showMemberMenu()
   else :
     print ("no books in cart")
def makeOrder(row) :
   
   today = datetime.today()
     # get the current date and time
   next_week = today + timedelta(days=7) 
    # add 7 days to get the date for next week
   today=today.strftime('%Y-%m-%d')

   next_week_str = next_week.strftime('%Y-%m-%d')
   queryString =F"insert into orders (userid,received,shipped,shipAddress,shipCity,shipState,shipZip) values ('{userId}','{today}','{next_week_str}','{address}','{city}','{state}','{zip}')"
   cursor.execute(queryString)
   connection.commit()
   queryString=f"select ono from orders where userid='{userId}'"
   cursor.execute(queryString)
   tuple= cursor.fetchone()
   orderNum= tuple[0]
   queryString=f"insert into odetails(ono,isbn,qty,price) values('{orderNum}','{row[2]}','{row[3]}','{row[1]}');"
   cursor.execute(queryString)
   connection.commit()
   queryString= f"DELETE FROM cart WHERE userid='{userId}'"
   cursor.execute(queryString)
   connection.commit()
   printBill()

def printBill():
   quer

def showMemberMenu():
   option= memberMenu()
   if option == '1':
    showSubject()
   elif  option == '2':
      choice= searchMenu()
      if choice == '1' :
        print ("1. Author Search")
        search("author",3)
      elif choice =='2':
        print ("2. Title Search") 
        search("title",3)
      else :
        print ("3. Go Back to Main Menu")   
        showMemberMenu()
   elif option == '3':
        checkOut()
   else: 
     print(" you are now logged out")
     

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
    getBooksNumber(queryString,2)
   
  except Exception as e:
                print("An error occurred: ", e) 


def getBooksNumber(query,num):
    cursor.execute(f"select count(isbn)  from books {query}")
    row = cursor.fetchone()
    print ("=============================")
    print (row[0],"books available ")
    print ("=============================")
    showBooks(int(row[0]),query,num)

def showBooks(index,query,num):
   i=0
   more= True
   while i <= index and more==True:
     queryString = f"select * from books {query} ORDER BY isbn LIMIT {num} OFFSET {i}"
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
      more=False
   showMemberMenu()   
def buyBook(alt):
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
            if not num == '0':
              queryString =f"SELECT qty from cart where isbn ='{alt}' and userid ='{userId}'"
              cursor.execute(queryString)
              row=cursor.fetchone()
              if not row  :
               cursor.execute("insert into cart (userid,isbn,qty) values (%s,%s,%s)",(userId,alt,num))
               connection.commit()
               print (" the book added to the cart")
              else :
                cursor.execute("update cart set qty = %s where isbn =%s and userid = %s",(alt,num,userId))
                connection.commit()
                print ("the number of the book updated")
                
            
                  

def login():
    user_login_info=loginView()
    select_query= """ SELECT  userid, address,city,state,zip from members where email = %s and password = %s"""
    cursor.execute(select_query, (user_login_info["email"],user_login_info["password"],))
    row = cursor.fetchone()
    if not row: 
      print("password or email is not correct")
      print("enter  t  to try again or  any letter  to back to the main menu")
      alt = input()
      if alt == 't':
       login()         
    else :
      global userId ,address,city,state,zip
      userId= row[0]
      address= row[1]
      city = row[2]
      state = row[3]
      zip = row [4]

      showMemberMenu()
      
def search(column,num):
  print("Enter the "+ column + " 's name or a part of the name :")
  searchWord =input()
  queryString="where "+ column + " like '%"+searchWord+"%'"
  getBooksNumber(queryString,num)

def register():
     try:
                user_info=registerView()
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
            register() 
         else:
              run = False    
        
        