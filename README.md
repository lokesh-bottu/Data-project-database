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

## 3. Write a SQL script that loads CSV data into a table.

- Create a table with the same attributes and then copy the data to that table.



#### creating matches table
- CREATE TABLE cricket_matches (
id serial PRIMARY KEY,
season integer,
city text,
date date,
team1 text,
team2 text,
toss_winner text,
toss_decision text,
result text,
dl_applied boolean,
winner text,
win_by_runs integer,
win_by_wickets integer,
player_of_match text,
venue text,
umpire1 text,
umpire2 text,
umpire3 text
);

#### copy the csv file to the created table
- .\copy matches FROM '/home/lokesh/Downloads/MB SQL/matches.csv' DELIMITER ',' CSV HEADER;

#### Create table Deliveries
- CREATE TABLE deliveries (
match_id INT,
inning INT,
batting_team text,
bowling_team text,
over DECIMAL(5,2),
ball INT,
batsman text,
non_striker text,
bowler text,
is_super_over BOOLEAN,
wide_runs INT,
bye_runs INT,
legbye_runs INT,
noball_runs INT,
penalty_runs INT,
batsman_runs INT,
extra_runs INT,
total_runs INT,
player_dismissed text,
dismissal_kind text,
fielder text
);

#### copy the csv file to the created table
- .\copy deliveries FROM '/home/lokesh/Downloads/MB SQL/deliveries.csv' DELIMITER ',' CSV HEADER;


