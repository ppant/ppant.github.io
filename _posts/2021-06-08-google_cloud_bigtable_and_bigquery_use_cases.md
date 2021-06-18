---
title: 'Google Cloud BigTable and BigQuery differences and use cases'

date: 2021-06-18T1:46:03+05:30
author: Pradeep Pant
layout: post
---

Many times ppl get confuse with [Google Cloud's](https://cloud.google.com/) **BigTable** and **BigQuery** services, which one to use when? 

I am putting a small use case to describe when to use either of them. 

**Use Case:** 
Say for example we have lots of data straming in real-time coming from many sensor devices and we need to store that data and anaylyse in real time, so first part is to store that data, there comes **BigTable** in picture, so BigTable is a NoSQL database, it has huge storage capacity (in Peta Bytes) means that it can handle real-time data. It's a kind of OLAP. One of the thing which BigQuery is not suitable for is to provide some insight of data. Actually, we can't directly query BigTable. You can compare BigQuery with similar popular NoSQL db's like Hbase, Casandra and other colum databases. Google Cloud offers it as Managed service.
So we have real-time data stored in BigTable, now we now we want analyse this data here comes **BigQuery**. BigQuery is a data warehouse, a kind of OLTP. One can write SQL queries to fetch the data also predictive modeliing can be done. One can also analyse the results using popular using visulation tools like Data studio, Tabulea.

So in nutshell, **BigTable** is a NoSQL DB and **BigQuery** is a DataWarehouse OLTP engine for querying and analysing. 


Happy Learning!
 
