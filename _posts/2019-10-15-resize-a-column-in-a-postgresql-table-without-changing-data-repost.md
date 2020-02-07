---
id: 2111
title: 'Resize a column in a PostgreSQL table without changing data: Repost'
date: 2019-10-15T19:59:24+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2111
permalink: /2019/10/15/resize-a-column-in-a-postgresql-table-without-changing-data-repost/
---
This morning I realized that one of the columns in the table I have recently created is running out of space. It is varchar(10) and I want to make it varchar(20) and of course wanted to do without losing any data which got filled in the last couple of days. Though there is a standard way to changing the size and type of the col using ALTER commands which can become tricky sometimes with the data. So I was looking for an alternate way and I found an awesome [post](http:// https://sniptools.com/databases/resize-a-column-in-a-postgresql-table-without-changing-data/) on how to do this in an easy way without disturbing data, this is an almost 10 yrs old [post](https://sniptools.com/databases/resize-a-column-in-a-postgresql-table-without-changing-data/) so reposting the commands in case they get lost. For detailed reading please visit the blog link given in references.

Command to check the current size of a given column:

<p class="has-text-color has-background has-luminous-vivid-orange-color has-very-light-gray-background-color">
  <code>SELECT atttypmod FROM pg_attribute WHERE attrelid = 'TABLE1'::regclass AND attname = 'COL1';</code>
</p>

In my case, the present size is 10 and I want to increase it to 25, so the command to update column will be as below:

<p style="font-size:0" class="has-text-color has-background has-luminous-vivid-orange-color has-very-light-gray-background-color">
  <code>UPDATE pg_attribute SET atttypmod = 25 WHERE attrelid = 'TABLE1'::regclass AND attname = 'COL1';</code>
</p>



I hope this info and re-post helps.

 **Original blog link:**  
<https://sniptools.com/databases/resize-a-column-in-a-postgresql-table-without-changing-data/>