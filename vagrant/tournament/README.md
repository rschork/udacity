Creates a database to track the end-to-end results and schedule matches for a Swiss Tournament
for the following criteria:
-Even number of entrants
-No byes
-One tournament at a time


The tournament file contains three scripts:
1) tournament.py
	Contains the functions necessary to track the tournament results.
2) tournament.sql
	Creates the database and imports the schema / table structure.
3) tournament_test.py
	Performs unit testing of each function necessary to track results in order to ensure
	everything is working properly. Important to check this file if any changes are made to tournament.py


To Use:
1) Navigate to tournament directory containing three scripts and launch psql
2) Run tournament.sql using \i tournament.sql to create database and table structure
3) Import tournament.py into whatever script you are using to manage the tournament
	and use those functions to track progress. Functions should be self-explanatory
	if you open tournament.py


To do:
1) Allow multiple tournaments at once
2) Allow odd number of participants by scheduling byes

