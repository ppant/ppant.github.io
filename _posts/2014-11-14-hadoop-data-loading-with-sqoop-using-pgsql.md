---
id: 1351
title: Import RDBMS table to HDFS with sqoop from postgreSQL
date: 2014-11-14T20:39:44+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1351
permalink: /2014/11/14/hadoop-data-loading-with-sqoop-using-pgsql/
dsq_thread_id:
  - "3223140421"
---
**Steps:**

1. Download JDBC driver

&nbsp;

[code lang=&#8221;bash&#8221;]$wget http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar[/code]

&nbsp;

<span style="color: #333333;"> </span>2. Copy:<span style="color: #800000;"> </span>

[code lang=&#8221;bash&#8221;]cp /home/cloudera/Desktop/postgresql-9.3-1102.jdbc4.jar /usr/lib/sqoop/lib/ [/code]

&nbsp;

<span style="color: #333333;">3. Configure:<em><span style="color: #0000ff;"> </span></em></span>

[code lang=&#8221;bash&#8221;]/var/lib/pgsql/data/pg_hba.conf[/code]

file. You need to allow the IP/host of machine running Hadoop.

<span style="color: #333333;">Restart postgreSQL using<span style="color: #800000;"> </span></span>

[code lang=&#8221;bash&#8221;]$pg_ctl restart[/code]

&nbsp;

<span style="color: #333333;">4. Run sqoop: Open the terminal on machine running hadoop and type the below command.</span>

&nbsp;

[code lang=&#8221;bash&#8221;] cloudera@cloudera-vm:/usr/lib/sqoop bin/sqoop import &#8211;connect jdbc:postgresql://192.168.0.34:5432/Testdb&#8211;table employee &#8211;username postgres -P &#8211;target-dir /sqoopOut1 -m 1 [/code]

&nbsp;

<span style="color: #333333;">Enter password:</span>

&nbsp;

**prerequisites:**

<ul style="list-style-type: circle;">
  <li>
    <a href="http://www.cloudera.com/content/cloudera/en/documentation/DemoVMs/Cloudera-QuickStart-VM/cloudera_quickstart_vm.html">Cloudera hadoop VM distribution</a> or any other machine running hadoop.
  </li>
  <li>
    postgreSQL installation.
  </li>
  <li>
    database<span style="color: #800000;"> Testdb</span> and employee <span style="color: #800000;">table</span> on a running instance of postgreSQL (e.g.; <span style="color: #800000;">192.168.0.34:5432</span> in point 4).
  </li>
</ul>

&nbsp;

All set! Your pgsql table data is now available on [HDFS](http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) of  VM hadoop cluster.

&nbsp;

Enjoy hadoop learning!