---
id: 471
title: 'Functional Programming in Perl: Part 1'
date: 2011-04-28T18:00:17+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=471
permalink: /2011/04/28/functional-programming-in-perl/
jabber_published:
  - "1303995874"
email_notification:
  - "1303995874"
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:7:"1995146";s:7:"blog_id";s:7:"1919664";s:9:"mod_stamp";s:19:"2011-05-02 11:28:20";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1341576729";}'
dsq_thread_id:
  - "783003988"
---
<span style="color:#000000;">As we know  functional programming involves creating and manipulating functions to build up larger programs. This requires a language that allows functions to be used as input and return data to other functions. Perl has two important features that make it possible: –</span>

<span style="color:#0000ff;">* Code references</span>

<span style="color:#0000ff;">* Closures</span>

<span style="color:#0000ff;"><br /> </span>

<span style="color:#000000;">Lets take code reference first:-</span>

<span style="color:#000000;"><br /> </span>

<span style="color:#800000;">Need of code reference: </span>

<span style="color:#000000;">Sometimes we need to manipulate a subroutine by reference so we need to take the references to functions. This might happen if you need to create a signal handler, a Tk callback, or a hash of function pointers etc.</span>

<span style="color:#000000;"><br /> </span>

<span style="color:#800000;">To get a code reference:</span>  
[code lang=&#8221;perl&#8221;]  
$cref = &func;  
[/code]  
<span style="color:#000000;">Reference to anonymous functions</span>  
[code lang=&#8221;perl&#8221;]  
$cref = sub { &#8230; };  
[/code]

<span style="color:#800000;">To call a code reference:</span>

<span style="color:#800000;"><span style="color:#000000;">Using a postfix arrow notation for dereferencing a code reference.</span><br /> </span>  
[code lang=&#8221;perl&#8221;]  
@returned = $cref->(@arguments);  
[/code]  
<span style="color:#000000;">A way to call the subroutine by reference prior to Perl 5.004</span>  
[code lang=&#8221;perl&#8221;]  
@returned = &$cref(@arguments);  
[/code]  
<span style="color:#000000;"><span style="color:#800000;">Explanation:</span> </span>

<span style="color:#000000;">If the name of a function is <code>func</code>, you can produce a reference to this code by preceding that name with <code>&</code> . You can also create anonymous functions using the <code>sub</code> <code>{}</code> notation. These code references can be stored just like any other reference. So we can say that code references are same as <a href="http://www.newty.de/fpt/index.html">function pointers</a> in C and C++ and which certainly helps to improve coding.</span>

<span style="color:#000000;"><br /> </span>

<span style="color:#000000;">In my next post I will try to cover closures.</span>

<span style="color:#000000;"><br /> </span>

<p style="text-align:left;">
  <span style="color:#000000;">Thanks for reading.</span>
</p>

<span style="color:#000000;"><br /> </span>

<p style="text-align:left;">
  <span style="color:#000000;"><strong>Ref:</strong><a href="http://oreilly.com/catalog/9781565922433"> Perl Cookbook</a> by <a href="http://98.245.82.12/tcpc/">Tom Christiansen</a> & <a href="http://nathan.torkington.com/">Nathan Torkingston</a></span>
</p>