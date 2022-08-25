---
id: 1070
title: CSS based page numbering in PDF creation
date: 2013-07-17T18:15:36+05:30
author: Pradeep Pant
layout: post
guid: /?p=1070
permalink: /2013/07/17/css-based-page-numbering-in-pdf-creation/
dsq_thread_id:
  - "1506198506"
---
I frequently use [PDF engine](/2010/02/pdf-generators/ "Open source PDF engine with CSS") for generating PDF of multiple web pages a kind of book. Though you can use engine specific switch to insert page number(s) but if you want beautiful CSS based numbering then below [code](http://pastebin.com/jzRvsdg9) can be used. Just paste the code in a .CSS file and link to your html pages.

[code lang=&#8221;css&#8221;]  
/\* Page number at the bottom of page \*/

@page {

@bottom-center {

content: "Page " counter(page) " of " counter(pages);

font-style: italic;

color: green

}

}  
[/code]