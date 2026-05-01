---
id: 1468
title: Implementing mapper attachment in elasticsearch
date: 2015-09-16T17:19:21+05:30
layout: post
categories: [tech]
guid: /?p=1468
permalink: /2015/09/16/implementing-mapper-attachment-in-elasticsearch/
dsq_thread_id:
  - "4134780724"
---
**Create a new index**  
[code lang="bash"]curl -X PUT "192.168.0.37:9200/test" -d '{  
"settings" : { "index" : { "number\_of\_shards" : 1, "number\_of\_replicas" : 0 }}  
}'[/code]

**Mapping attachement type**  
[code lang="bash"]curl -X PUT "192.168.0.37:9200/test/attachment/_mapping" -d '{  
"attachment" : {  
"properties" : {  
"file" : {  
"type" : "attachment",  
"fields" : {  
"title" : { "store" : "yes" },  
"file" : { "term\_vector":"with\_positions_offsets", "store":"yes" }  
} } } } }'[/code]

**Shell script to convert content to base64 encoding and index**  
[code lang="bash"]#!/bin/sh</code>

coded=\`cat TestPDF.pdf | perl -MMIME::Base64 -ne 'print encode\_base64($\_)'\`  
json="{\"file\":\"${coded}\"}"  
echo "$json" > json.file  
curl -X POST "192.168.0.37:9200/test/attachment/" -d @json.file  
[/code]  
**Query  (Search esults will be highlighted)**  
[code lang="bash"]curl "192.168.0.37:9200/_search?pretty=true" -d '{  
"fields" : ["title"],  
"query" : {  
"query_string" : {  
"query" : "Cycling tips"  
}  
},  
"highlight" : {  
"fields" : {  
"file" : {}  
} } }'[/code]

\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\*****

If you want to explore more check [Full Code on GitHub](https://github.com/ppant/elasticsearch-mapper-attachement-example)