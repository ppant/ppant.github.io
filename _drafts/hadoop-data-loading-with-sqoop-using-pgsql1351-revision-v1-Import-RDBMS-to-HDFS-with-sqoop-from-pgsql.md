---
id: 1375
title: Import RDBMS to HDFS with sqoop from pgsql
date: 2014-11-14T13:00:59+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2014/11/1351-revision-v1/
permalink: /2014/11/14/1351-revision-v1/
---
**Steps:**

1. Download JDBC driver

<span style="color: #333333;"><a style="color: #333333;" href="http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar">http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar</a></span>

<span style="color: #333333;"> </span>2. Copy:<span style="color: #0000ff;"> <em>cp /home/cloudera/Desktop/postgresql-9.3-1102.jdbc4.jar</em> <em>/usr/lib/sqoop/lib/</em></span>

<span style="color: #333333;">3. Configure:<em><span style="color: #0000ff;"> /var/lib/pgsql/data/pg_hba.conf</span></em> file. You need to allow the IP/host of machine running hadoop.</span>

<span style="color: #333333;">Restart PG using <em><span style="color: #0000ff;">pg_ctl restart</span></em></span>

<span style="color: #333333;">3. Run sqoop:</span>

_<span style="color: #0000ff;">cloudera@cloudera-vm:/usr/lib/sqoop$ bin/sqoop import &#8211;connect jdbc:postgresql:                                  //192.168.0.34:5432/Testdb &#8211;table employee &#8211;username postgres -P &#8211;target-dir   /sqoopOut1 -m 1</span>_

<span style="color: #333333;">Enter password:</span>

&nbsp;

**prerequisites:**

<ul style="list-style-type: circle;">
  <li>
    <a href="http://www.cloudera.com/content/cloudera/en/documentation/DemoVMs/Cloudera-QuickStart-VM/cloudera_quickstart_vm.html">Cloudera hadoop VM distribution</a>
  </li>
  <li>
    PGSQL installation
  </li>
  <li>
    Testdb and employee table on running pgsql
  </li>
</ul>

&nbsp;

All set! Your pgsql table data is now available on [HDFS](http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) of  VM hadoop cluster.

&nbsp;

Enjoy hadoop.