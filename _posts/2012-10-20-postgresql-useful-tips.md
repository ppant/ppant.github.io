---
id: 965
title: PostgreSQL useful tips
date: 2012-10-20T22:46:57+05:30
layout: post
categories: [tech]
guid: /?p=965
permalink: /2012/10/20/postgresql-useful-tips/
gr_overridden:
  - "0"
dsq_thread_id:
  - "892961847"
---
<span style="font-family: Verdana;">I am posting some of the PostgreSQL commands which I use frequently.</span>

Create a new database name testdb

\# createdb <dbname>  
e.g:  
[code lang="sql"]  
\# createdb testdb  
[/code]  
Remove a PostgreSQL database  
\# dropdb <dbname>  
e.g:  
[code lang="sql"]  
\# dropdb testdb  
[/code]

Backing up a PostgreSQL database  
[code lang="sql"]  
\# su – postgres  
[/code]

[code lang="sql"]  
\# pg\_dump –blob -Fc testdb -f /var/lib/pgsql/backups/testdb\_backup  
[/code]

Restoring PostgreSQL database from back up dump  
[code lang="sql"]  
\# pg\_restore –dbname=testdb /var/lib/pgsql/backups/testdb\_backup  
[/code]

Writing query output to a CSV file:  
[code lang="sql"]  
\# \o 'tmp/logs/query\_out\_dump.csv'  
[/code]

After this operation all the query results will be stored in a CSV file.  
Using console again for query output:  
[code lang="sql"]  
\# \o  
[/code]  
For more on [pg_dump](http://www.postgresql.org/docs/8.4/static/app-pgdump.html) and [pg_restore](http://www.postgresql.org/docs/8.4/static/app-pgrestore.html) pl. check the documentation