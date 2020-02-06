---
id: 1107
title: PostgreSQL useful tips
date: 2013-07-19T16:21:11+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/965-revision-15/
permalink: /2013/07/19/965-revision-15/
---
<span style="font-family: Verdana;">I am posting some of the PostgreSQL commands which I use frequently.</span>

Create a new database name testdb

\# createdb <dbname>  
e.g:  
[code lang=&#8221;sql&#8221;]  
\# createdb testdb  
[/code]  
Remove a PostgreSQL database  
\# dropdb <dbname>  
e.g:  
[code lang=&#8221;sql&#8221;]  
\# dropdb testdb  
[/code]

Backing up a PostgreSQL database  
[code lang=&#8221;sql&#8221;]  
\# su &#8211; postgres  
[/code]

[code lang=&#8221;sql&#8221;]  
\# pg\_dump &#8211;blob -Fc testdb -f /var/lib/pgsql/backups/testdb\_backup  
[/code]

Restoring PostgreSQL database from back up dump  
[code lang=&#8221;sql&#8221;]  
\# pg\_restore &#8211;dbname=testdb /var/lib/pgsql/backups/testdb\_backup  
[/code]

Writing query output to a CSV file:  
[code lang=&#8221;sql&#8221;]  
\# \o &#8216;tmp/logs/query\_out\_dump.csv&#8217;  
[/code]

After this operation all the query results will be stored in a CSV file.  
Using console again for query output:  
[code lang=&#8221;sql&#8221;]]  
\# \o  
[/code]  
For more on [pg_dump](http://www.postgresql.org/docs/8.4/static/app-pgdump.html) and [pg_restore](http://www.postgresql.org/docs/8.4/static/app-pgrestore.html) pl. check the documentation