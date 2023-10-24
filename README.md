# Data-project-database

## 1. Write a SQL script that creates a new user, and database. Make the user the owner of the db.
- createuser --interactive
  write this above command and write the username which you want to add then hit y on the keyboard.
- To create a database write "database_name"
- then write sudo -u "username"
- to check the info write \conninfo 

## 2. Write another SQL script that cleans up the user, and database created in the previous step.
- Initially check whether the database and user are present or not, then delete.
- To delete the database   DROP DATABASE IF EXISTS "database_name";
- To delete the user  DROP USER IF EXISTS "username";

## 3. 
