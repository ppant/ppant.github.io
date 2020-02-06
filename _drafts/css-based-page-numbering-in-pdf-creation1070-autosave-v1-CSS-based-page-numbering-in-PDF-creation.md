---
id: 1073
title: CSS based page numbering in PDF creation
date: 2013-07-18T11:32:56+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/1070-autosave/
permalink: /2013/07/18/1070-autosave-v1/
---
I frequently use [PDF engine](http://pradeeppant.com/2010/02/pdf-generators/ "Open source PDF engine with CSS") for generating PDF of multiple web pages a kind of book. Though you can use engine specific switch to insert page number(s) but if you want beautiful CSS based numbering then below [code](http://pastebin.com/jzRvsdg9) can be used. Just paste the code in a .CSS file and link to your html pages.

[code lang=&#8221;css&#8221;]

@page {

@bottom-center {

content: "Page " counter(page) " of " counter(pages);

font-style: italic;

color: green

}

}  
[/code]