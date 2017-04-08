# Projects

Part of Computing tools project

0.1.1 Restriction enzyme program
The program involved use of Python-SQL to contruct database named 'DNA Sites'
in which table 'Restriction enzyme' was created . The table has information
about the restriction enzyme and their corresponding site of action. Python
script was used to create the database . Another Python script was written to
implement the program which connects database,user interface and real process.
This Python script contained three functions
1. main()
2. DNA(enzyme,site)
3. Restriction db(enzyme)
main():
It is the rst function to be called. It contains code which is used by user to
mention the input le and restriction enzyme. It also redirects to
Restriction db(enzyme):
This function is vital as it connects the database with rest of the program.
This function takes an enzyme searches for it in database and extracts the cor-
responding restriction site which is later used to search the sequence.
DNA(enzyme,site): This function contains the main program which takes
enzyme and site as input. It also reads the input le, converts it to string and
searches the site in the strings. It displays the position where the sites are
present and also
Schema of database table used
For Database, Table Restriction enzyme was created in database DNA Sites.
The following is the schema of the table:-
Restriction enzyme(Enzyme,Site)
The gure below is of user interface of Restriction enzyme program , where
one can input the le and select a restriction site and get the result.
