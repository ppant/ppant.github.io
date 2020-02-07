---
id: 1472
title: implementing mapper attachment in elasticserach
date: 2015-09-16T17:14:40+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2015/09/1468-revision-v1/
permalink: /2015/09/16/1468-revision-v1/
---
**Create a new index**  
`curl -X DELETE "192.168.0.37:9200/test"<br />
curl -X PUT "192.168.0.37:9200/test" -d '{<br />
"settings" : { "index" : { "number_of_shards" : 1, "number_of_replicas" : 0 }}<br />
}'`

**Mapping attachement type**  
`curl -X PUT "192.168.0.37:9200/test/attachment/_mapping" -d '{<br />
"attachment" : {<br />
"properties" : {<br />
"file" : {<br />
"type" : "attachment",<br />
"fields" : {<br />
"title" : { "store" : "yes" },<br />
"file" : { "term_vector":"with_positions_offsets", "store":"yes" }<br />
} } } } }'`

**Shell script to convert content to base64 encoding and index them**  
`#!/bin/sh`

coded=\`cat TestPDF.pdf | perl -MMIME::Base64 -ne &#8216;print encode\_base64($\_)&#8217;\`  
json=&#8221;{\&#8221;file\&#8221;:\&#8221;${coded}\&#8221;}&#8221;  
echo &#8220;$json&#8221; > json.file  
curl -X POST &#8220;192.168.0.37:9200/test/attachment/&#8221; -d @json.file

**Search (Search results will be highlighted)**  
`curl "192.168.0.37:9200/_search?pretty=true" -d '{<br />
"fields" : ["title"],<br />
"query" : {<br />
"query_string" : {<br />
"query" : "Cycling tips"<br />
}<br />
},<br />
"highlight" : {<br />
"fields" : {<br />
"file" : {}<br />
} } }'`

&nbsp;

[Code on GitHub](https://github.com/ppant/elasticsearch-mapper-attachement-example)