---
id: 971
title: PostgreSQL useful tips
date: 2012-10-20T22:49:03+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2012/10/965-revision-5/
permalink: /2012/10/20/965-revision-5/
---
<span style="font-family: Verdana;">I am posting some of the commands which I use in PostgreSQL for my day to day work:</span>

**<span style="font-family: Verdana;">Create</span><span style="font-family: Verdana;"> a new database name testdb</span>**

<div>
  <pre xml:space="preserve"><span style="font-family: Verdana;"># createdb &lt;dbname&gt;</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">e.g: </span><span style="font-family: Verdana;"># create db test</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Remove a PostgreSQL database</span></strong></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># dropdb &lt;dbname&gt;</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">e.g: </span><span style="font-family: Verdana;"># dropdb testdb</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Backing up a PostgreSQL database</span></strong></pre>
  
  <div>
    <span style="font-family: Verdana;"># su &#8211; postgres</span>
  </div>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># pg_dump --blob -Fc testdb -f /var/lib/pgsql/backups/testdb_backup</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Restoring PostgreSQL database from back up dump</span></strong></pre>
  
  <pre xml:space="preserve"># <span style="font-family: Verdana;">pg_restore --dbname=testdb /var/lib/pgsql/backuos/testdb_backup</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Writing query output to a file:</span></strong></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># \o 'tmp/logs/query_out_dump.txt'</span></pre>
  
  <div>
    <pre xml:space="preserve"><span style="font-family: Verdana;">After this operation all the query results will be stored in file.</span></pre>
    
    <pre xml:space="preserve"><strong style="font-family: Verdana;">Using console again for query output:</strong></pre>
    
    <pre xml:space="preserve"><span style="font-family: Verdana;"># \o</span></pre>
    
    <pre xml:space="preserve"></pre>
    
    <pre xml:space="preserve">For more on <a href="http://www.postgresql.org/docs/8.4/static/app-pgdump.html">pg_dump</a> and<a href="http://www.postgresql.org/docs/8.4/static/app-pgrestore.html"> pg_restore</a> pl. check the documentation</pre>
  </div>
</div>