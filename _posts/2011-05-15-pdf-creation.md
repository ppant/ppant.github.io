---
id: 555
title: PDF creation in Perl
date: 2011-05-15T14:15:15+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=555
permalink: /2011/05/15/pdf-creation/
jabber_published:
  - "1305449134"
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:7:"1995146";s:7:"blog_id";s:7:"1919664";s:9:"mod_stamp";s:19:"2011-05-17 04:11:14";}'
email_notification:
  - "1305449134"
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1338741933";}'
dsq_thread_id:
  - "782210068"
---
<div id="_mcePaste">
  <p>
    We in our project use HTMLDOC for PDF generation in Cent OS 5. We pass html files with some template info and run the HTMLDOC command line from perl program. This after multiple run gives me the correct PDF book with proper table of content, Index etc. The basic issue now I face with this engine is that it doesn&#8217;t support the new pdf features like PDF/A, CSS etc. and I don&#8217;t think HTMLDOC is very much in developmental mode. I want to introduce new engine to my application and tried some of the available options:
  </p>
  
  <p>
    <a href="http://www.princexml.com/" target="_blank">Prince:</a>
  </p>
  
  <p>
    This looks excellent and supports almost all modern PDF features. The input files can be xml, html etc and can be run as a batch process. But it has a licence fee.
  </p>
  
  <p>
    <a href="http://www.realobjects.com/" target="_blank">PDF Reactor:</a>
  </p>
  
  <p>
    Looks fine also have the Perl wrapper for manipulating PDF but can&#8217;t run as a batch process for making single PDF from many HTML files. This can be done through Perl program by making a loop to documents which in result can produce combine PDF. Like prince it also has a licence fee.
  </p>
  
  <p>
    <a href="http://code.google.com/p/wkhtmltopdf/" target="_blank">WKHTMLTOPDF:</a>
  </p>
  
  <p>
    First thing I like about this engine is that this is a open source engine, beside being free it still supports CSS. It can be run as a batch process through Perl like HTMLDOC, prince. At first look it looks promising to me so I have decided to invest some time on it. The engine is QT and webkit based and in development phase.
  </p>
  
  <p>
    I was wondering if I am missing something. Is there other engines someone has tried which go well with Perl?
  </p>
  
  <p>
    Best regards,
  </p>
</div>