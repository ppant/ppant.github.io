---
id: 1352
title: hadoop data loading with sqoop using pgsql
date: 2014-11-01T20:30:11+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2014/11/1351-revision-v1/
permalink: /2014/11/01/1351-revision-v1/
---
<div>
  <p>
    <span style="color: #333333;">sqoop using pgsql:</span>
  </p>
  
  <p>
    <span style="color: #333333;">1. Download JDBC driver </span>
  </p>
  
  <p>
    <span style="color: #333333;"><a style="color: #333333;" href="http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar">http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar</a></span>
  </p>
  
  <p>
    <span style="color: #333333;"> </span>
  </p>
  
  <p>
    <span style="color: #333333;">2. Copy cp /home/cloudera/Desktop/postgresql-9.3-1102.jdbc4.jar /usr/lib/sqoop/lib/</span>
  </p>
  
  <p>
    <span style="color: #333333;">3. Configure /var/lib/pgsql/data/pg_hba.conf file for allowing machine running hadoop</span>
  </p>
  
  <p>
    <span style="color: #333333;">Restart PG using pg_ctl retstart</span>
  </p>
  
  <p>
    <span style="color: #333333;">3. Run sqoop</span>
  </p>
  
  <p>
    <span style="color: #333333;">cloudera@cloudera-vm:/usr/lib/sqoop$ bin/sqoop import &#8211;connect jdbc:postgresql:                                  //192.168.0.34:5432/edureka &#8211;table employee &#8211;username postgres -P &#8211;target-dir   /sqoopOut1 -m 1</span>
  </p>
  
  <p>
    <span style="color: #333333;">Enter password:</span>
  </p>
  
  <p>
    &nbsp;
  </p>
  
  <p>
    All set!
  </p>
  
  <p>
    Enjoy hadoop.
  </p>
</div>