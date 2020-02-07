---
id: 2237
title: 'Expiry and revive of my blog: Some early learning of 2020'
date: 2020-01-19T19:15:09+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2237
permalink: /2020/01/19/expiry-and-revive-of-my-blog-some-early-learning-of-2020/
---
Last week was full of adventure in reviving my blog [www.pradeeppant.com](http://www.pradeeppant.com). Ok. enough suspense! Here goes the story&#8230;  
After new year&#8217;s feast and vacation, I suddenly realized that my blog is not accessible. Later realised that this was due to a mistake from my side imagine I forgot to extend the hosting which was combined with some other blogs from other folks. I mis-read some messages and resulted in suspension of my blog. I was so desperate even tweeted about that &#8230;<figure class="wp-block-embed-twitter wp-block-embed is-type-rich is-provider-twitter">

<div class="wp-block-embed__wrapper">
  <blockquote class="twitter-tweet" data-width="550" data-dnt="true">
    <p lang="en" dir="ltr">
      my blog <a href="https://t.co/QL5EymVqnh">https://t.co/QL5EymVqnh</a> is down for some days now 😢This was due to hosting issues. My mistake&#8230; Hope will able to revive soon🤞. Maybe this is a good opportunity to move to <a href="https://twitter.com/hashtag/github?src=hash&ref_src=twsrc%5Etfw">#github</a> <a href="https://twitter.com/hashtag/gatsby?src=hash&ref_src=twsrc%5Etfw">#gatsby</a>/<a href="https://twitter.com/hashtag/Jekyll?src=hash&ref_src=twsrc%5Etfw">#Jekyll</a> <a href="https://twitter.com/hashtag/WordPress?src=hash&ref_src=twsrc%5Etfw">#WordPress</a> is too heavy for me .. what's say? <a href="https://twitter.com/chankeypathak?ref_src=twsrc%5Etfw">@chankeypathak</a>
    </p>&mdash; Pradeep Pant |प्रदीप पंत (@ppant) 
    
    <a href="https://twitter.com/ppant/status/1215333118002917377?ref_src=twsrc%5Etfw">January 9, 2020</a>
  </blockquote>
</div></figure> 

Anyways, I restarted with a new hosting plan and restored a backup I had from 7th Dec 2019 as updraft somehow failed to take back at the end of the month. Then I realized that I have written 3 posts after the last backup was taken so obviously they were not there. Then the whole process of reviving the last 3 posts started. Though I had the content of these blog posts, means that rewriting was the option but that will break the chronology, etc and I wanted to do in a correct way, also the couple of drafts I have made and a draft from my friend Toshit to whom I requested to write a guest blog. So I thought to revive the content through database backup also the other data like users, comment and other metadata after 7th Dec 2019 was there. Though I was able to get the backup from hosting the but database was mixed. So there was a problem. 

Then I started googling and experimenting a bit through Cpanel phpMyadmin DB console finally able to find a way to extract the rows from the new DB wp\_posts tables and insert them to the new DB wp\_posts table without duplicates. Below are the steps for one such case:

1. First I have created a new table which is the union of a table from old DB (wpis\_posts) and the same table from new DB (wp\_posts)

 `create table merged_table_wpis_posts select * from wp_posts union select * from wpis_posts` 

2. Renamed the original table

 `rename table wpis_posts to wpis_post_bck` 

3. Renamed the merged table to the original table name

 `rename table merged_table_wpis_posts to wpis_posts` 

The same exercise should be repeated for other affected tables like wp\_users, wp\_comments and metadata tables. 

Check the website again. You should get all the published posts and other information in the expected chronology. Later you can remove the backup table once everything is working.

<blockquote class="wp-block-quote">
  <p>
    <em>So, lesson learned, always do a manual check of your backup tool it might possible that you have changed your cloud credential, etc and the automatic backup failed and take hosting provider mails seriously there could be some critical info apart from publicity </em>🙂<br /><br />btw I am thinking seriously about moving to GitHub pages&#8230;
  </p>
</blockquote>