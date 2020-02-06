---
id: 2114
title: Resize a column in a PostgreSQL table without changing data
date: 2019-10-15T16:12:29+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/10/2111-revision-v1/
permalink: /2019/10/15/2111-revision-v1/
---
This morning I realized that one of the columns in the table I have recently created is running out of space. It is varchar(10) and I want to make it varchar(20). I want to do this without losing any data which got filled in the last couple of days. I found this awesome post on Resize a column in a PostgreSQL table without changing data. Like this, an almost 10 yrs old [post](https://sniptools.com/databases/resize-a-column-in-a-postgresql-table-without-changing-data/) so reposting the commands in case get lost. For detailed reading please visit the blog link given in references.

`SELECT atttypmod FROM pg_attribute WHERE attrelid = 'TABLE1'::regclass AND attname = 'COL1';`

`UPDATE pg_attribute SET atttypmod = 35+4 WHERE attrelid = 'TABLE1'::regclass AND attname = 'COL1';` 

  * 

Check below post

Original blog link: <https://sniptools.com/databases/resize-a-column-in-a-postgresql-table-without-changing-data/>