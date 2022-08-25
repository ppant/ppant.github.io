---
id: 247
title: Backtracking example1
date: 2011-01-21T10:06:29+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=247
permalink: /2011/01/21/perl-backtracking-example/
jabber_published:
  - "1295584590"
dsq_thread_id:
  - "786026045"
---
<p style="padding-left:30px;">
  <span style="color:#0000ff;">Let&#8217;s say you want to find the word following &#8220;foo&#8221; in the string &#8220;Food is on the foo table.&#8221;:</span>
</p>

<p style="padding-left:60px;">
  <p>
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
  </p>
  
  <p>
    <code> </code>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;">When the match runs, the first part of the regular expression (b(foo) ) finds a possible match right at the beginning of the string, and loads up $1 with &#8220;Foo&#8221;. However, as soon as the matching engine sees that there&#8217;s no whitespace following the  &#8220;Foo&#8221; that it had saved in $1, it realizes its mistake and starts over again one character after where it had the tentative match. This time it goes all the way until the next occurrence of &#8220;foo&#8221;. The complete regular expression matches this time and you get the expected output of &#8220;table follows foo.&#8221;</span>
  </p>
  
  <p style="padding-left:30px;">
    <p style="padding-left:30px;">
      <span style="color:#3366ff;">Still more examples to come &#8230;keep watching</span>
    </p>
    
    <p style="padding-left:30px;">
      <p style="padding-left:30px;">
        <span style="color:#3366ff;">Thanks</span>
      </p>