create table members (fname varchar(20) not null,
lname varchar(20) not null,
address varchar(50) not null, city varchar(30) not null,
state varchar(20) not null,
zip int not null , phone varchar(12), email varchar(40) unique, 
userid int primary key AUTO_INCREMENT,
password varchar (200), creditcardtype varchar(10),
creditcardnumber char(16)
 );
create table orders ( userid int  not null  ,
ono int primary key not null  auto_increment,
received date  not null ,shipped date,shipAddress  varchar(50),
shipCity varchar(30),shipState varchar(20),shipZip int ,
 FOREIGN KEY (userid) REFERENCES members(userid));

create table books (isbn char(10) PRIMARY key not null,
author varchar(100) not null,tittle varchar(128) not null,
price float  not null,subject varchar(30) not null);

 create table cart (userid int  not null , 
 isbn char(10) not null,qty int  not null,
 primary key(userid,isbn),
  FOREIGN KEY (isbn) REFERENCES books(isbn),
   FOREIGN KEY (userid) REFERENCES members(userid));
   
    create table odetails (ono int not null, 
 isbn char(10)   not null  ,qty int  not null ,
 price float not null,
 primary key(ono,isbn),
  FOREIGN KEY (isbn) REFERENCES books(isbn),
   FOREIGN KEY (ono) REFERENCES orders(ono));