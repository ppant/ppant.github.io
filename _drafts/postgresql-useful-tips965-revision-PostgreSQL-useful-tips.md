---
id: 966
title: PostgreSQL useful tips
date: 2012-10-20T22:41:28+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2012/10/965-revision/
permalink: /2012/10/20/965-revision/
---
<span style="font-family: Verdana;">I am posting some of my day to day commands which I use in PostgreSQL:</span>

**<span style="font-family: Verdana;">Create</span><span style="font-family: Verdana;"> a new database</span>**

<div>
  <pre xml:space="preserve"><span style="font-family: Verdana;"># createdb &lt;dbname&gt;</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">eg: # create db test</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">
</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Remove a PostgreSQL database</span></strong></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># dropdb &lt;dbname&gt;</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">e.g: # dropdb test</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">
</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Backing up a PostgreSQL database</span></strong></pre>
  
  <div>
    <span style="font-family: Verdana;"># su &#8211; postgres</span>
  </div>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;"># pg_dump --blob -Fc test -f /var/lib/pgsql/backups/test_backup</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">
</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Restoring PostgreSQL database from back up dump</span></strong></pre>
  
  <pre xml:space="preserve"> # <span style="font-family: Verdana;">pg_restore --dbname=test /var/lib/pgsql/backuos/test_backup</span></pre>
  
  <pre xml:space="preserve"><span style="font-family: Verdana;">
</span></pre>
  
  <pre xml:space="preserve"><strong><span style="font-family: Verdana;">Writing query output to a file:</span></strong></pre>
  
  <pre xml:space="preserve"></pre>
  
  <div>
    <pre xml:space="preserve"><span style="font-family: Verdana;"># \o 'tmp/logs/query_out_dump.txt'</span></pre>
    
    <pre xml:space="preserve"><span style="font-family: Verdana;">Now all the output from query will be stored in this file.</span></pre>
    
    <pre xml:space="preserve"></pre>
    
    <div>
      <pre xml:space="preserve"><span style="font-family: Verdana;"><strong>
</strong></span></pre>
      
      <pre xml:space="preserve"><span style="font-family: Verdana;"><strong>Using console again for queries:</strong> </span></pre>
    </div>
    
    <pre xml:space="preserve"><span style="font-family: Verdana;"># \o</span></pre>
    
    <pre xml:space="preserve"></pre>
    
    <pre xml:space="preserve">For more on <a href="http://www.postgresql.org/docs/8.4/static/app-pgdump.html">pg_dump</a> and<a href="http://www.postgresql.org/docs/8.4/static/app-pgrestore.html"> pg_restore</a> pl. check the documentation</pre>
  </div>
</div>