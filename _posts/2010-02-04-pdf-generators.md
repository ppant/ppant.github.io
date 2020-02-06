---
id: 32
title: Open source PDF engine with CSS
date: 2010-02-04T11:59:08+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=32
permalink: /2010/02/04/pdf-generators/
jabber_published:
  - "1280940638"
dsq_thread_id:
  - "782981694"
---
While looking for open source PDF generators I came across some very interesting engines available like Apache FOP and some very good PHP based engines too. My basic requirement was to run it as a batch process in Linux/Perl. The engine should supports CSS and if possible should supports PDF/A and SVG too. After doing a lot of analysis I was still not sure if all pdf issues can be solved by open source engines or not??. Then I tried my hand a bit on properitery engines like [princexml](http://www.princexml.com/) and [PDFReactor](http://www.realobjects.com). They have there own advantage and disadvantages. Princexml looks really nice but there is underlying cost and also doesn&#8217;t provide interface to access the API&#8217;s for pdf manipulation. Finally I found a open source engine [WKHTMLTOPDF](http://code.google.com/p/wkhtmltopdf/) it supports CSS and looks promising as it uses already tested rendering engine webkit .

Will share if it fits in my requirement and delivers the results.