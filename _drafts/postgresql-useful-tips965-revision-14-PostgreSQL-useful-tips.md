---
id: 1106
title: PostgreSQL useful tips
date: 2013-07-19T14:35:15+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/965-revision-14/
permalink: /2013/07/19/965-revision-14/
---
<span style="font-family: Verdana;">I am posting some of the PostgreSQL commands which I use frequently.</span>

**<span style="font-family: Verdana;">Create</span><span style="font-family: Verdana;"> a new database name testdb</span>**

<div>
  <pre xml:space="preserve"><span style="font-family: Verdana;"># createdb &lt;dbname&gt;</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">e.g: </span>
[code lang="sql"]# createdb testdb[/code]


<pre xml:space="preserve"><strong><span style="font-family: Verdana;">Remove a PostgreSQL database</span></strong></pre>


<pre xml:space="preserve"><span style="font-family: Verdana;"># dropdb &lt;dbname&gt;</span></pre>


<pre xml:space="preserve"><span style="font-family: Verdana;">e.g: </span>
[code lang="sql"]# dropdb testdb[/code]


<pre xml:space="preserve"><strong><span style="font-family: Verdana;">Backing up a PostgreSQL database</span></strong></pre>


<p>
  [code lang="sql"]# su - postgres[/code]<br />
  [code lang="sql"]# pg_dump --blob -Fc testdb -f /var/lib/pgsql/backups/testdb_backup[/code]
</p>


<pre xml:space="preserve"><strong><span style="font-family: Verdana;">Restoring PostgreSQL database from back up dump</span></strong></pre>


<p>
  [code lang="sql"]# pg_restore --dbname=testdb /var/lib/pgsql/backups/testdb_backup[/code]
</p>


<pre xml:space="preserve"><strong><span style="font-family: Verdana;">Writing query output to a CSV file:</span></strong></pre>


<p>
  [code lang="sql"]# \o 'tmp/logs/query_out_dump.csv'[/code]
</p>


<div>
  <pre xml:space="preserve"><span style="font-family: Verdana;">After this operation all the query results will be stored in a CSV file.</span></pre>
  
  
  <pre xml:space="preserve"><strong style="font-family: Verdana;">Using console again for query output:</strong></pre>
  
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># \o</span></pre>
  
  
  <pre xml:space="preserve"></pre>
  
  
  <pre xml:space="preserve">For more on <a href="http://www.postgresql.org/docs/8.4/static/app-pgdump.html">pg_dump</a> and<a href="http://www.postgresql.org/docs/8.4/static/app-pgrestore.html"> pg_restore</a> pl. check the documentation</pre>
  
</div>