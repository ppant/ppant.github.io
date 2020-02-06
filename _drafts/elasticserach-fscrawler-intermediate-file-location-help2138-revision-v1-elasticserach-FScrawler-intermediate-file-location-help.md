---
id: 2142
title: elasticserach FScrawler intermediate file location? help
date: 2019-10-18T19:55:35+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/10/2138-revision-v1/
permalink: /2019/10/18/2138-revision-v1/
---
I am looking for a method that can intercept the output of [FSCrwaler](http:// https://fscrawler.readthedocs.io/en/latest/) before this gets passed to the [elastic engine](https://www.elastic.co/products/enterprise-search) for indexing. 

Just take a case, what I have is a PDF file which I wanted to index plus I also have some attributes/metadata for the same PDF which are stored in the database. I want to index both the content (PDF file content + attributes stored in PostgreSQL) in a single index file so that I can refine my search criteria and get correct results. As far I understand for PDF indexing text needs to be extracted from the file and stored in a text format and then passed to the indexing engine. I am relatively new (an [HTDIG](http://htdig.sourceforge.net/) veteran -:D ) to the elastic ecosystem so looking for a way to intercept the text extracted from a PDF file so that I can append other text (in this scenario fetched from PostgreSQL) and then pass to the indexing mechanism, a kind of single index file for both the content.

Wondering if anyone has encountered this kind of scenario and can provide some pointers? It will be good to know that where does FSCrawler stores intermediate files created during the indexing process in elastic search? Can we intercept them and add some custom info? 

Comments will be much appreciated!

Thanks!