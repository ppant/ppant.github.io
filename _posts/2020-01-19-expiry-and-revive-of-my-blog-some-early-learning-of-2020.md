---
id: 2237
title: 'Expiry and revive of my blog: Some early learning of 2020'
date: 2020-01-19T19:15:09+05:30
author: Pradeep Pant
layout: post
---
Last week was full of adventure in reviving my blog [https://www.pradeeppant.com](https://www.pradeeppant.com). Ok. enough suspense! Here goes the story...  
After new year's feast and vacation, I suddenly realized that my blog is not accessible. Later realised that this was due to a mistake from my side imagine I forgot to extend the hosting which was combined with some other blogs from other folks. I mis-read some messages and resulted in suspension of my blog. I was so desperate even tweeted about that ....

Anyways, I restarted with a new hosting plan and restored a backup I had from 7th Dec 2019 as updraft somehow failed to take back at the end of the month. Then I realized that I have written 3 posts after the last backup was taken so obviously they were not there. Then the whole process of reviving the last 3 posts started. Though I had the content of these blog posts, means that rewriting was the option but that will break the chronology, etc and I wanted to do in a correct way, also the couple of drafts I have made and a draft from my friend Toshit to whom I requested to write a guest blog. So I thought to revive the content through database backup also the other data like users, comment and other metadata after 7th Dec 2019 was there. Though I was able to get the backup from hosting the but database was mixed. So there was a problem. 

Then I started googling and experimenting a bit through Cpanel phpMyadmin DB console finally able to find a way to extract the rows from the new DB wp_posts tables and insert them to the new DB wp_posts table without duplicates. Below are the steps for one such case:

* First I have created a new table which is the union of a table from old DB (wpis_posts) and the same table from new DB (wp_posts)

 ````sql
 create table merged_table_wpis_posts select * from wp_posts union select * from wpis_posts
 ```` 

* Renamed the original table

 ````sql
 rename table wpis_posts to wpis_post_bck
```` 

* Renamed the merged table to the original table name

 ````sql
 rename table merged_table_wpis_posts to wpis_posts
```` 

The same exercise should be repeated for other affected tables like wp_users, wp_comments and metadata tables. 

Check the website again. You should get all the published posts and other information in the expected chronology. Later you can remove the backup table once everything is working.
So, lesson learned, always do a manual check of your backup tool it might possible that you have changed your cloud credential, etc and the automatic backup failed and take hosting provider mails seriously there could be some critical info apart from publicity btw I am thinking seriously about moving to GitHub pages...

Will keep posted!