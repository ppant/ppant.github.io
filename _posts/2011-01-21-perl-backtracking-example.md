---
id: 247
title: Backtracking example1
date: 2011-01-21T10:06:29+05:30
layout: post
categories: [tech]
guid: http://ppant.wordpress.com/?p=247
permalink: /2011/01/21/perl-backtracking-example/
jabber_published:
  - "1295584590"
dsq_thread_id:
  - "786026045"
---
<p style="padding-left:30px;">
  <span style="color:#0000ff;">Let's say you want to find the word following "foo" in the string "Food is on the foo table.":</span>


<p style="padding-left:60px;">
  

    <code>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#008000;">#!/usr/bin/perl&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#008000;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#008000;"># Example of backtracking algorithm&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">use 5.006;&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">use strict;&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">use warnings;&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">$_ = "Food is on the foo table.";&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">if ( /b(foo)s+(w+)/i ) {&lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:60px;">&lt;span style="color:#993300;">print "$2 follows $1.n";&lt;/span>&lt;/p>
&lt;p style="padding-left:30px;">&lt;span style="color:#993300;"> &lt;/span>&lt;/p>
&lt;p style="padding-left:30px;">&lt;span style="color:#993300;"> }&lt;/span>&lt;/p>
&lt;p></code>
  
  
  

    <code> </code>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;">When the match runs, the first part of the regular expression (b(foo) ) finds a possible match right at the beginning of the string, and loads up $1 with "Foo". However, as soon as the matching engine sees that there's no whitespace following the  "Foo" that it had saved in $1, it realizes its mistake and starts over again one character after where it had the tentative match. This time it goes all the way until the next occurrence of "foo". The complete regular expression matches this time and you get the expected output of "table follows foo."</span>
  
  
  <p style="padding-left:30px;">
    <p style="padding-left:30px;">
      <span style="color:#3366ff;">Still more examples to come ...keep watching</span>
    
    
    <p style="padding-left:30px;">
      <p style="padding-left:30px;">
        <span style="color:#3366ff;">Thanks</span>
      