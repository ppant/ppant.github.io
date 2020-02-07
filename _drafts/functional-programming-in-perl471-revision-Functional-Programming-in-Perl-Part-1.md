---
id: 1113
title: 'Functional Programming in Perl: Part 1'
date: 2011-04-28T18:00:17+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2011/04/471-revision/
permalink: /2011/04/28/471-revision/
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

> <span style="color:#008000;">$cref = &func;</span>

<span style="color:#000000;">Reference to anonymous functions</span>

> <span style="color:#008000;">$cref = sub { &#8230; };</span>

<span style="color:#008000;"><br /> </span>

<span style="color:#800000;">To call a code reference:</span>

<span style="color:#800000;"><span style="color:#000000;">Using a postfix arrow notation for dereferencing a code reference.</span><br /> </span>

> <span style="color:#008000;">@returned = $cref->(@arguments);</span>

<span style="color:#000000;">A way to call the subroutine by reference prior to Perl 5.004</span>

> <span style="color:#008000;">@returned = &$cref(@arguments);</span>

<span style="color:#008000;"><br /> </span>

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