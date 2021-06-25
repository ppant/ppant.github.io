---
title: 'When to use Google Cloud BigTable and BigQuery? A Use case..'
date: 2021-06-08T1:46:03+05:30
author: Pradeep Pant
layout: post
---

Many times cloud folks get confused with [Google Cloud's](https://cloud.google.com/) **BigTable** and **BigQuery** services, which one to use when? 

I am putting a small use case to describe when to use either of them. 

**Use Case:** 

Say for example we have a huge incoming data stream (real-time) from multiple sensor devices and we need to store that data and analyze it in real-time, so the first part is to store that data, there comes [**BigTable**](https://cloud.google.com/bigtable) in the picture, so BigTable is a NoSQL database, it has huge storage capacity (in Peta Bytes) means that it can handle real-time data. It's a kind of OLAP. One of the thing which BigQuery is not suitable for is to provide some insight into data. Actually, we can't directly query BigTable. You can compare BigQuery with similar popular NoSQL DB's like Hbase, Casandra, and other column databases. Google Cloud offers it as Managed service.
So we have real-time data stored in BigTable, now we want to analyze this data so here comes [**BigQuery**](https://cloud.google.com/bigquery), BigQuery is a data warehouse, a kind of OLTP. One can write SQL queries to fetch the data also predictive modeling can be done. One can also analyze the results using popular using visualization tools like Data Studio, Tableau.

So in nutshell, **BigTable** is a NoSQL DB and **BigQuery** is a DataWarehouse OLTP engine for querying and analyzing. 


Happy Learning!
 
