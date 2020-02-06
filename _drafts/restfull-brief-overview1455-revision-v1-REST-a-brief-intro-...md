---
id: 1457
title: REST a brief intro ..
date: 2015-08-28T17:15:03+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2015/08/1455-revision-v1/
permalink: /2015/08/28/1455-revision-v1/
---
<div>
  Putting some thoughts for newbies who are trying to understand REST and wants to make web application more RESTful. I am writing this because sometimes I feel that despite of a lot of resources its not easy to get the actual gist ..sometimes is too technical or sometime abstract. I am putting some broad points which in my view REST is ..of course I made these points based on my reading and experience working with REST but this doesn&#8217;t replace any of REST documentation. Advised to go through references given at the end for detailed study.
</div>

<div>
</div>

<div>
  <ul>
    <li>
      REST  <strong>REpresentational State Transfer</strong> is a design pattern/design concept (architecture) used in web applications for managing state information: Means REST is not a tool/technology/specification/protocol, REST isn&#8217;t a tangible thing like a piece of software or even a specification, it&#8217;s a selection of ideals, of best practices distilled from the HTTP specs. (http://www.w3.org/Protocols/Specs.html)
    </li>
    <li>
       Well, if you are using HTTP (any web page accessed is presented by http only) then you are being RESTful to some degree since HTTP is a REST protocol, but to take full advantage of the platform, APIs should use RESTful practices as much as possible.
    </li>
    <li>
      We can make our application more RESTful by using the correct HTTP methods and utilzing more HTTP methods.
    </li>
    <li>
      RESTful Web service is required to be <code>stateless</code> in it&#8217;s communication between server and client  so you should be able to request almost any format while non-REST mainly SOAP uses XML. So this is flexibility and non dependent on format.
    </li>
    <li>
      URL is the important part of REST. REST is more than just GET/POST actually browsers pretty much just GET stuff. They don&#8217;t do a lot of other types of interaction with resources. This is a problem because it has led many people to assume that HTTP is just for GETing. But HTTP is actually general purpose protocol for applying <a href="http://www.wikiwand.com/en/HTTP_verbs">HTTP verbs</a> (GET, POST, PUT, DELETE, etc.) to nouns (object/web page which has a URL).
    </li>
  </ul>
</div>

**Recommended reading:**

[Must read paper on REST by Roy Fielding ](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)

[How I Explained REST to My Wife](http://www.looah.com/source/view/2284)