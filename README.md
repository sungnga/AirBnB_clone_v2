# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`



# MySQL

In addition to FileStorage and JSON, SQLAlchemy and MySQL may be used for storage as well. To use the latter, run the setup_mysql_dev.sql script to prepare a MySQL server and set the HBNB_TYPE_STORAGE environmental variable equal to "db". Being able to switch between different forms of storage provides abstraction, allowing the code to run without knowing how it's stored.

After a MySQL server is setup, users are able to:
* Create a database
* Create a new user (in localhost)
* Setup a password for the new user
* Setup privileges on the database
* Add, update, and delete an object

### Database Storage Engine
* The folder [engine](./models/engine/) contains the File Storage engine and the Database Storage engine that manage and store all the data for all the classes in this project.

### Accessing database in MySQL interactive mode:
```
$ mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 76
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```