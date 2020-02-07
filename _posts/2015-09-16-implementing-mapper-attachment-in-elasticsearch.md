---
id: 1468
title: Implementing mapper attachment in elasticsearch
date: 2015-09-16T17:19:21+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1468
permalink: /2015/09/16/implementing-mapper-attachment-in-elasticsearch/
dsq_thread_id:
  - "4134780724"
---
**Create a new index**  
[code lang=&#8221;bash&#8221;]curl -X PUT "192.168.0.37:9200/test" -d &#8216;{  
"settings" : { "index" : { "number\_of\_shards" : 1, "number\_of\_replicas" : 0 }}  
}'[/code]

**Mapping attachement type**  
[code lang=&#8221;bash&#8221;]curl -X PUT "192.168.0.37:9200/test/attachment/_mapping" -d &#8216;{  
"attachment" : {  
"properties" : {  
"file" : {  
"type" : "attachment",  
"fields" : {  
"title" : { "store" : "yes" },  
"file" : { "term\_vector":"with\_positions_offsets", "store":"yes" }  
} } } } }'[/code]

**Shell script to convert content to base64 encoding and index**  
[code lang=&#8221;bash&#8221;]#!/bin/sh</code>

coded=\`cat TestPDF.pdf | perl -MMIME::Base64 -ne &#8216;print encode\_base64($\_)&#8217;\`  
json="{\"file\":\"${coded}\"}"  
echo "$json" > json.file  
curl -X POST "192.168.0.37:9200/test/attachment/" -d @json.file  
[/code]  
**Query  (Search esults will be highlighted)**  
[code lang=&#8221;bash&#8221;]curl "192.168.0.37:9200/_search?pretty=true" -d &#8216;{  
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