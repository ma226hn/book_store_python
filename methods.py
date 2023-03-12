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
    print(" ")
    return option
def mainMenu():
    print ("********************************************************************")
    print("****                                                            *****")
    print("***                     WELCOME TO ONLINE BOOKS STORE           *****")
    print ("********************************************************************")
    print ("            1. Member login")
    print("             2. New member registration      ")
    print ("             q. Quit          ")
    option = input("type in your option:")
    return option
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