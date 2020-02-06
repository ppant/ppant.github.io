---
id: 1465
title: RESTfull brief overview
date: 2015-08-29T09:12:31+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2015/08/1455-revision-v1/
permalink: /2015/08/29/1455-revision-v1/
---
<div style="text-align: left;">
  Putting some thoughts mainly for newbies trying to understand REST. Sometimes I observed that the actual documentation on the web is too technical or abstract and scattered which a bit difficult for newbies..  I am writing down some broad points which in my view REST is and it&#8217;s equation with HTTP &#8230; these points based on my reading and experience working with REST. It doesn&#8217;t replace any of REST documentation. Advised to go through references given at the end for detaled study.
</div>

<div style="text-align: left;">
</div>

<div>
</div>

<div>
  <ul>
    <li>
      REST  <strong>REpresentational State Transfer</strong> is a design pattern/design concept (architecture) used in web applications for managing state information-> REST is not a tool/techology/specification/protocol. In other words, REST isn&#8217;t a tangible thing like a piece of software or even a specification, it&#8217;s a selection of ideals, of best practices distilled from the HTTP specs.
    </li>
    <li>
       If you are using HTTP you are being RESTful to some degree since HTTP is a REST protocol, but to take full advantage of the platform, APIs should use RESTful practices as much as possible.
    </li>
    <li>
      We can make our application more RESTful by using the correct HTTP methods.
    </li>
    <li>
      RESTful Web service is required to be <code>stateless</code> in it&#8217;s communication between server and client  so you should be able to request almost any format while non-REST mainly SOAP uses XML.
    </li>
    <li>
      URL is the important part of REST. REST is more than GET/POST actually browsers pretty much just GET stuff. They don&#8217;t do a lot of other types of interaction with resources. This is a problem because it has led many people to assume that HTTP is just for GETing. But HTTP is actually ageneral purpose protocol for applying http verbs (<a href="http://www.wikiwand.com/en/HTTP_verbs">HTTP verbs</a> (GET, POST, PUT, DELETE, etc.) to nouns (object/web page which has a URL).
    </li>
  </ul>
</div>

**Recommended reading**:

Paper by Roy Fielding <span style="color: #0000ff;">http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm</span>

<span style="line-height: 24px;">HTTP Specs <span style="color: #0000ff;">http://www.w3.org/Protocols/Specs.html</span></span>

How I Explained REST to My Wife:  
<span style="color: #0000ff;">http://www.looah.com/source/view/2284</span>

Happy reading!