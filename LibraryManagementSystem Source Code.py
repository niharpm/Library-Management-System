# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:21:32 2024

@author: NIHAR MAHAJAN
"""

from datetime import date

import mysql.connector as sql



#Connecting to the database


mydb = sql.connect(
        host="localhost",
        user="root",
        password="BlueDolphin"
    )




#Code to use file to keep mysql table up to date


def update():

    mycursor = mydb.cursor()
    mycursor.execute("use school_project")

    mycursor.execute("delete from booklist;")
    mydb.commit()


    f = open("/Users/NIHAR/Desktop/Books.txt", "r")

    lines = f.readlines()

    set = {""}

    for line in lines:

        set.add(line[:-1])


    for element in set:


        if element != "":

            count = 0
            data = element.split(", ")


            for line in lines:


                if data[2] == line.split(", ")[2][:-1]:

                    count += 1
            query = "insert into booklist values (\"" + data[0] + "\", \"" + data[1] + "\", \"" + data[2] + "\", \"" + str(count) + "\");"



            mycursor.execute("use school_project")

            mycursor.execute(query)

            mydb.commit()


#Code to update the main Booklist table


def decrement(book):


    mycursor = mydb.cursor()

    mycursor.execute("use school_project;")

    query = "select copies from booklist where Book_Name = '" + book.upper() + "';"

    mycursor.execute(query)


    num = mycursor.fetchone()[0] - 1

    mydb.commit()


    query = "update booklist set copies = '" + str(num) + "' where Book_Name = '" + book.upper() + "';"\

    mycursor.execute(query)

    mydb.commit()

#Code to update the main Booklist table


def increment(book):


    mycursor = mydb.cursor()

    mycursor.execute("use school_project;")

    query = "select copies from booklist where Book_Name = '" + book.upper() + "';"

    mycursor.execute(query)


    num = mycursor.fetchone()[0] + 1

    mydb.commit()


    query = "update booklist set copies = '" + str(num) + "' where Book_Name = '" + book.upper() + "';"


    mycursor.execute(query)

    mydb.commit()

#Main program


def menu():


    update()

    catalogue = ""

    mycursor = mydb.cursor()


    mycursor.execute("use school_project;")

    mycursor.execute("select book_name, author_name from booklist;")


    for element in mycursor.fetchall():

        catalogue += str(element) + "\n"



    print("Enter 1 for new books to be added to the catalogue (for admin)", "\n",
          "Enter 2 for books to be removed from the catalogue (for admin)", "\n",
          "Enter 3 to view the catalogue", "\n",
          "Enter 4 to borrow books", "\n",
          "Enter 5 to return books", "\n"
          "Enter 6 to search for a book in the catalogue", "\n")



    key = int(input())


    if key == 1:

        print("Enter the name of the book you want to add : ")

        name = input()

        print("Enter the author of the book you want to add : ")

        auth = input()

        print("Enter the ISBN number of the book you want to add : ")

        isbn = input()


        row = name + ", " + auth + ", " + isbn

        f = open("/Users/gautam/Desktop/Books.txt", "a")

        f.write(row)

        update()


    elif key == 2:



        isbn = input("Enter isbn number of the book to be removed : ")

        f = open("/Users/gautam/Desktop/Books.txt", "r")

        lines = f.readlines()

        f1 = open("/Users/gautam/Desktop/Books.txt", "w")

        found = False

        for line in lines:


            if line.split(", ")[2][:-1] != str(isbn):

                f1.write(line)


            elif found == False:

                found = True

            else:

                f1.write(line)


        f1.close()

        update()



    elif key == 3:

        print(catalogue)


    elif key == 4:

        mycursor = mydb.cursor()


        mycursor.execute("use school_project2")

        name = input("Enter user name : ")

        mycursor.execute("SHOW TABLES LIKE '" + name + "'")


        output = mycursor.fetchone()


        if name not in str(output):


            query = "create table " + name + " (Books_borrowed varchar(50), Date_borrowed varchar(50));"

            mycursor.execute(query)

            mydb.commit()

        book = input("Enter name of book you want to borrow : ")


        if book.upper() in catalogue.upper():


            decrement(book)

            query = "insert into " + name + " values ('" + book + "', '" + str(date.today()) + "');"

            mycursor.execute("use school_project2")

            mycursor.execute(query)

            mydb.commit()

        else:
            print("Book not available")



    elif key == 5:

        mycursor = mydb.cursor()

        mycursor.execute("use school_project2;")


        name = input("Enter user name : ")

        book = input("Enter name of book you want to return : ")


        increment(book)


        mycursor.execute("use school_project2")
        query = "delete from " + name + " where Books_borrowed = '" + book + "';"
        mycursor.execute(query)

        mydb.commit()



    elif key == 6:


        name = input("Enter name of book you want to search for : ")


        fullcatalogue = ""




        mycursor = mydb.cursor()

        mycursor.execute("use school_project;")

        mycursor.execute("select * from booklist;")


        for element in mycursor.fetchall():


            fullcatalogue += str(element) + "\n"



        if name.upper() in str(fullcatalogue).upper():

            print("Book found")



        else:

            print("Book not found")




    else:


        print("Invalid choice")

        menu()

menu()
