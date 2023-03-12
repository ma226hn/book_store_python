import hashlib
def hashPassword(password):
 
  password_bytes = password.encode('utf-8')
  sha256 = hashlib.sha256()
  sha256.update(password_bytes)
  hashed_password_bytes = sha256.digest()
  hashed_password = hashed_password_bytes.hex()
  return hashed_password

def register ():
    print ("Welcome to the online book store ")
    print("    New Member Registration ")
    fname= input("Enter first name : ")
    lname=input("Enter last name :  ")
    sAddress= input( "Enter street address:  ")
    city=input("Enter city : ")
    state=input("Enter state : ")
    zip=input("Enter Zip : " )
    phone= input ("Enter phone: ")
    email=input ("Enter email address: ")
    password=input("Enter password : ")
    hashedPassWord= hashPassword(password)
   
    return {
        "fname": fname,
        "lname": lname,
        "address": sAddress,
        "city": city ,
        "state" : state ,
        "zip" : zip ,
        "phone": phone ,
        "email" : email ,
        "password" : hashedPassWord

    }
def login ():
    email= input ("enter email: ")
    password = input (" enter password: ")
    hashedPassWord= hashPassword(password)
    return {
        "email": email ,
        "password" : hashedPassWord
    }
def memberMenu():
    print ("********************************************************************")
    print("****                                                            *****")
    print("***                     WELCOME TO ONLINE BOOKS STORE           *****")
    print ("***                         Member Menu                      ******")
    print ("********************************************************************")
    print ("            1. Browse by subjects")
    print("             2.search by author/tittle      ")
    print ("            3. check out          ")
    print ("            4. logout          ")
    option = input("type in your option:")
    if option == '1' or option == '2' or option=='3' or option == '4' :
     return option
    else:
     print(" invalid input ________________try again")
     print ("") 
     memberMenu()  
    
def mainMenu():
    print ("********************************************************************")
    print("****                                                            *****")
    print("***                     WELCOME TO ONLINE BOOKS STORE           *****")
    print ("********************************************************************")
    print ("            1. Member login")
    print("             2. New member registration      ")
    print ("            q. Quit          ")
    option = input("type in your option:")
    if option == '1' or option == '2' or option=='q' :
     return option
    else:
     print(" invalid input ________________try again")
     print ("") 
     mainMenu()  
   
def tuples_to_dict(list_tuples, column_names):
    list_dict=[]
    for tuple in list_tuples:
        dict= {}
        dict[column_names[0]]= tuple[0]
        dict[column_names[1]] = tuple[1]
        dict[column_names[2]]= tuple[2]
        dict[column_names[3]]= tuple[3]
        dict[column_names[4]]= tuple[4]
        list_dict.append(dict)
    return list_dict
def searchMenu():
    print ("====================================")
    print ("  serach  books")
    print ("1. Author Search")
    print ("2. Title Search")
    print ("3. Go Back to Main Menu")
    alt =input (" type your choice : ")
    print ("")
    if alt == '1' or alt == '2' or alt=='3' :
     return alt
    else:
     print(" invalid input ________________try again")
     print ("") 
     searchMenu()  
   


