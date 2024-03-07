# Library-Management-System

The Library Management System is an efficient method to maintain a record of books and documentation without the requirement of manually maintaining records using Excel. This project implements an algorithm which uses MySQL database to store information and python to provide a user interface. The program enables the storage of infinite number of records and a catalogue for users to search the desired books. The Library Management aims to simplify the functioning of online libraries through automated data management system.

The Library Management System provides the following functionalities to its administrators and customers:

For administrators:
1.	Maintaining a catalogue:
Administrators can maintain a catalogue of all the books present in the library by using tables in MySQL

2.	Adding books to the catalogue:
New books can be added to the catalogue by selecting the first option on the dropdown menu and further entering the required information about the book through 3 prompts. The required information includes the name of the book, name of the author and the book’s ISBN number.
The update function, through a pre-established connection with the SQL server, updates the table containing a booklist, the changes in are further reflected in the catalogue.

3.	Removing books from the catalogue:
The administrator can remove the books - that are out of stock or to be moved out of the library – from the catalogue by selecting the second option on the dropdown menu.

The user has to follow similar procedures as in the case of adding books. The update function then removes the specified book from the table and the catalogue.

4.	Viewing rental records:
The administrator can view the records of the data maintained in the system directly from the database stored on the local MySQL server.

For Library Users:
1.	Library Membership:
The users are required to create a library account to borrow books. The username is used to keep a record of the purchases made by the customer.
The user data including the username, books borrowed and the date of borrowing the book is maintained in the format of a table in the SQL database.

2.	Viewing the Catalogue:
The customers can view the catalogue by selecting the third option on the dropdown menu. The program displays the table booklist in the form of tuples containing the information of the books.

3.	 Borrowing a book:
The following is the procedure for borrowing a book:
•	The user has to select the fourth option on the dropdown menu.
•	The user has to enter their username and the book they wish to borrow through two separate prompts.
The program then checks for the availability of the book and provides one of these three outputs:
•	The book is not available, indicating that the book is out of stock.
•	Invalid Choice, indicating that the book is not present in the catalogue.
•	No message is displayed if the process is successful and the user record is updated.

4.	Returning a book:
The following is the procedure for returning a book:
•	The user has to select the fifth option on the dropdown menu.
•	The user has to enter their username and the book they wish to return through two separate prompts.
The program then searches the user record of the book and provides one of these three outputs:
•	Invalid Choice, indicating that the book is not present in the record.
•	No message is displayed if the process is successful and the book is removed from the user record and the booklist table is updated with an increment in the number of copies.
5.	Searching for a book:
The customer can view the availability of a book using this method. The user has to select the sixth option from the menu to enable the search engine. The user has to then enter the name of the desired book in upper case. The program will return one of the following two options:
•	“Book Found”, if the book is available
•	“Book Not Found”, if the book is either out of stock or invalid.
The display menu runs on a recurring function – menu(). The program consists of the following four user defined functions:
•	increment()
•	decrement()
•	update()
•	menu()
The first three functions are called within the menu() function.
