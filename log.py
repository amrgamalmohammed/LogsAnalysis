#!/usr/bin/env python2

import psycopg2 as psql
from tabulate import tabulate as tab

DBNAME = "news"

header_1 = "The most popular three articles of all time: "

query_1 = "select a.title, count(*) as views " \
          "from articles as a, log as l " \
          "where l.path like '%' || a.slug " \
          "and l.status like '200' || '%' " \
          "group by a.title " \
          "order by views desc " \
          "limit 3"

header_2 = "The most popular article authors of all time: "

query_2 = "select au.name, count(*) as views " \
          "from articles as ar, authors as au, log as l " \
          "where l.path like '%' || ar.slug " \
          "and l.status like '200' || '%' " \
          "and au.id = ar.author " \
          "group by au.name " \
          "order by views desc "

header_3 = "Days on which more than 1% of requests lead to errors: "

query_3 = "select * from " \
          "(select one_day.date, " \
          "round((err.rate::decimal / one_day.rate::decimal)*100, 2) " \
          "as ratio " \
          "from " \
          "(select date(time) as date, count(*) as rate " \
          "from log group by date) as one_day, " \
          "(select date(time) as date, count(*) as rate " \
          "from log where status not like '200' || '%' " \
          "group by date) as err " \
          "where one_day.date = err.date) as rates " \
          "where rates.ratio > 1;"

# List all header alongside their queries
log = [(header_1, query_1), (header_2, query_2), (header_3, query_3)]


def main():
    """
    Main method to handle running queries
    """
    # Make a connection to Postgres
    conn = psql.connect(dbname=DBNAME)
    # Init a Cursor to execute date
    cur = conn.cursor()
    # Open an output stream
    output = open("output.txt", "w")
    # Iterate over desired questions
    for info in log:
        output.write("* " + info[0] + "\n")
        # Execute the associated query
        cur.execute(info[1])
        # Format results and write to output
        output.write(tab(cur.fetchall(), tablefmt='grid') + "\n\n")

# Handle main call
if __name__ == "__main__":
    main()
