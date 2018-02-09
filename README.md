# LogsAnalysis

 - This is a backend tool to execute postgreSQL on a provided database with some log information.
 
 - It uses ```psycopg2``` in ```Python``` to connect to ```PostgreSQL``` and execute queries such as in the output file example.

---
### Installation

 - This project is made in Python2 programming language.
 
 - This project needs ```PostgreSQL``` databse to be installed with a created username
 ```vagrant``` and a pre-existing database called ```news``` or just follow the installation
 steps of ```Vagrant``` and ```Virtualbox``` then download the virtual machine from course's
 page. 

 - This project uses ```psycopg2``` to connect and execute queries on postgreSQL.
   ```
   pip install psycopg2
   ```
- It uses ```tabulate``` to format output file in Text format.
   ```
   pip install tabulate
   ```
---
### Usage

 - Populate ```news``` database with data from ```newsdata.sql```:
   ```
   psql -d news -f newsdata.sql
   ```
 - To run it you just run:

   ```
   python log.py
   ```

---
### Contributors

 - amrgamalmohammed