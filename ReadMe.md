# Highland Golf Club Digital Scorecard
#### Video Demo: https://youtu.be/1W7_xExQ7-M
#### Description:
The following application utilizes the flask framework in relation with Python, HTML & CSS and SQlite in order to create a score tracker for front 9 and back 9 scores at Highland Country Club in Auburn New York

## app.py
This is the python framework for the application

## Databased.db
This is the SQlite database for the application, it was preconfigured using the following command (Found below or in DatabaseDefinition.sql)
```SQL
CREATE DATABASE GOLF;

CREATE TABLE USERS (

FirstName varchar(255),

LastName varchar(255)

);


CREATE TABLE ROUNDS (

Date varchar(255),

LastName varchar(255),

Hole1 int,

Hole2 int,

Hole3 int,

Hole4 int,

Hole5 int,

Hole6 int,

Hole7 int,

Hole8 int,

Hole9 int,

Hole10 int,

Hole11 int,

Hole12 int,

Hole13 int,

Hole14 int,

Hole15 int,

Hole16 int,

Hole17 int,

Hole18 int

);
```
## Static
This folder contains the stylesheet and image used on the html webpages

## Templates
This folder contains the html pages which are connected via app.py for function and style.css for design.

## How to run
```
flask run
```
