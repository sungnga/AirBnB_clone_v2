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
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| hbnb_dev_db        |
| hbtn_0e_6_usa      |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> use hbnb_dev_db;
Database changed
mysql> SHOW TABLES;
+-----------------------+
| Tables_in_hbnb_dev_db |
+-----------------------+
| amenities             |
| cities                |
| place_amenity         |
| places                |
| reviews               |
| states                |
| users                 |
+-----------------------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM amenities;
+--------------------------------------+---------------------+---------------------+-------+
| id                                   | created_at          | updated_at          | name  |
+--------------------------------------+---------------------+---------------------+-------+
| 0f008f20-0109-49f8-9d03-cc7148b8ee93 | 2019-08-15 00:11:57 | 2019-08-15 00:11:57 | Oven  |
| 44835307-d7e3-4282-8d5d-5a9afbdfecb1 | 2019-08-15 00:33:21 | 2019-08-15 00:33:21 | Cable |
| 58de07bf-9863-4918-bc75-793775cc714b | 2019-08-15 00:33:21 | 2019-08-15 00:33:21 | Wifi  |
| 8036b63e-f36f-441e-a860-0b95bdb35963 | 2019-08-15 00:11:57 | 2019-08-15 00:11:57 | Cable |
| 805df3e5-60a9-474f-92ab-5b3cdbe1c282 | 2019-08-15 00:11:57 | 2019-08-15 00:11:57 | Wifi  |
| 90f0a803-bee2-4bb7-9e00-77a8a24de52e | 2019-08-15 21:19:33 | 2019-08-15 21:19:33 | Oven  |
| a4fd5fac-d870-43f0-8fa5-c563913bb3bf | 2019-08-15 21:19:33 | 2019-08-15 21:19:33 | Cable |
| b05bf0a8-d13d-48a3-963c-fb96df24a9ca | 2019-08-15 21:19:33 | 2019-08-15 21:19:33 | Wifi  |
| b5cc98e7-3a52-4e45-bab8-1ca12f6676c8 | 2019-08-15 00:33:21 | 2019-08-15 00:33:21 | Oven  |
+--------------------------------------+---------------------+---------------------+-------+
9 rows in set (0.00 sec)

mysql>
```

### Environment variables used in this project:
* HBNB_ENV: running environment
* HBNB_MYSQL_USER: the username of MySQL
* HBNB_MYSQL_PWD: the password of MySQL
* HBNB_MYSQL_HOST: the hostname of MySQL
* HBNB_MYSQL_DB: the database name of MySQL
* HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
