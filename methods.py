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
    return {
        "fname": fname,
        "lname": lname,
        "address": sAddress,
        "city": city ,
        "state" : state ,
        "zip" : zip ,
        "phone": phone ,
        "email" : email ,
        "password" : password

    }
def login ():
    email= input ("enter email: ")
    password = input (" enter password: ")
    return {
        "email": email ,
        "password" : password
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
