---
id: 1072
title: CSS for page numbering in PDF creation
date: 2013-07-17T16:30:52+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/1070-revision-2/
permalink: /2013/07/17/1070-revision-v1/
---
I frequently use PDF engine for generating PDF of multiple web pages a kind of book. Though you can use engine specific switch to insert page number(s) but if you want beautiful CSS based numbering then below code can be used. Just paste the code in a .CSS file and link to your html pages.

<pre><span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">/* Page number at the bottom of page */</span>
<span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">@page {</span>
<span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">    @bottom-center {</span>
<span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">        content: "Page " counter(page) " of " counter(pages);</span>
<span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">        font-style: italic;</span>
<span style="line-height: 1.714285714; font-size: 1rem; color: #993300;">        color: green</span>
<span style="font-size: 1rem; line-height: 1.714285714; color: #993300;">    }</span>
<span style="font-size: 1rem; line-height: 1.714285714; color: #993300;">}</span></pre>

Ref: <http://pastebin.com/jzRvsdg9>