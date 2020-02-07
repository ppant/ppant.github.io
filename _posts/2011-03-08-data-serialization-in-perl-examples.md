---
id: 389
title: Data Serialization in Perl examples
date: 2011-03-08T14:35:39+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=389
permalink: /2011/03/08/data-serialization-in-perl-examples/
jabber_published:
  - "1299576836"
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1333325511";}'
dsq_thread_id:
  - "783047348"
---
One can store data and objects into a file using Serialization. The bytes that is generated can then be re-used to generate an object that will be identical (a clone) to the stored object. We can achieve this by using [Storable module from CPAN](http://search.cpan.org/~ams/Storable-2.25/Storable.pm). The example below will show a way to store and retrieve such objects.

> <pre><span style="color:#993300;">#!/usr/bin/perl</span>

<span style="color:#993300;">use 5.006;</span>
<span style="color:#993300;">use strict;</span>
<span style="color:#993300;">use warnings;</span>
<span style="color:#993300;">use Data::Dumper;</span>
<span style="color:#993300;">use Storable;</span>

<span style="color:#993300;">my %hash1 = ('Test1' =&gt; '10',</span>
<span style="color:#993300;"><span style="white-space:pre;">	</span>     'Test2' =&gt; '20');</span>

<span style="color:#993300;">store %hash1, "serialized_file";</span>
<span style="color:#993300;">print "##### HASH1 #####n";</span>
<span style="color:#993300;">print Dumper(%hash1);</span>

<span style="color:#993300;">my %hash2 = %{retrieve "serialized_file"};</span>
<span style="color:#993300;">print "n##### HASH2 #####n";</span>
<span style="color:#993300;">print Dumper(%hash2);</span>

<span style="color:#993300;">exit 0;</span>
<span style="color:#993300;">
</span></pre>
> 
> <p style="text-align:left;">
>   <strong><span style="color:#0000ff;">Output:</span></strong>
> </p>
> 
> <pre><span style="color:#008000;">##### HASH1 #####</span>
<span style="color:#008000;">$VAR1 = {</span>
<span style="color:#008000;">          'Test2' =&gt; '20',</span>
<span style="color:#008000;">          'Test1' =&gt; '10'</span>
<span style="color:#008000;">        };</span>

<span style="color:#008000;">##### HASH2 #####</span>
<span style="color:#008000;">$VAR1 = {</span>
<span style="color:#008000;">          'Test2' =&gt; '20',</span>
<span style="color:#008000;">          'Test1' =&gt; '10'</span>
<span style="color:#008000;">        };</span>
<span style="color:#008000;">
</span>
<span style="color:#008000;"><span style="color:#000000;">For more info see </span><a href="http://perldoc.perl.org/Storable.html"><span style="color:#000000;">perldoc Storable</span></a></span></pre>

<div id="_mcePaste" class="mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">
  <span style="font-family:Verdana, sans-serif;line-height:13px;font-size:11px;border-collapse:collapse;color:#292929;"><strong>Serialization</strong></span><span style="font-family:Verdana, sans-serif;line-height:13px;font-size:11px;border-collapse:collapse;color:#292929;"> is used to store data and objects into a file for instance. The serie of bytes that is generated can then be re-used to generate an object that will be identical (a clone) to the stored object.</span>
</div>