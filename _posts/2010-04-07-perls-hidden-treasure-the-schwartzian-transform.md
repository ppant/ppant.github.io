---
id: 74
title: 'Perl&#8217;s hidden treasure (The Schwartzian Transform)'
date: 2010-04-07T16:59:27+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=74
permalink: /2010/04/07/perls-hidden-treasure-the-schwartzian-transform/
dsq_thread_id:
  - "828518866"
---
<span style="color:#333333;">Hello,</span>

<span style="color:#333333;">If you ask me about the best features of Perl then there will be many answers CPAN, Hashes, RegX etc etc but the one of the hidden feature of perl is The </span>[<span style="color:#800000;"><strong><span style="color:#333333;">Schwartzian Transform</span></strong></span>](http://en.wikipedia.org/wiki/Schwartzian_transform)<span style="color:#333333;">. This is a technique that allows you to efficiently sort by a computed, secondary index.  Let&#8217;s say that you wanted to sort a list of strings by their md5 sum.  Pl. see the code below (the comments below are best read from bottom).</span>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>my @strings = (&#8216;C&#8217;, &#8216;CPlusPlus&#8217;, &#8216;Java&#8217;, &#8216;Perl&#8217;);</em></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>my $sorted_strings_on_MD5 =</em></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>map { $_->[0] } </em><span style="color:#0000ff;"><em> # map back to the original value</em></span></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>sort { $a->[1] cmp $b->[1] } </em><span style="color:#0000ff;"><em># sort by the correct element of the list</em></span></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>map { [$_, MD5Calu_func($_)] } </em><span style="color:#0000ff;"><em>#  create a list of anonymous lists</em></span></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><em>@strings </em><span style="color:#0000ff;"><em>#  take strings</em></span></span>
</p>

<span style="color:#333333;">Where MD5Calu_func($_) represents an expression that takes $_ (each item of the list in turn) and produces the corresponding value that is to be compared. This way,  you only have to do the expensive md5 computation N times, rather than N log N times. That&#8217;s the beauty of algorithm.</span>

<span style="color:#333333;">The algorithm has been given by one of the greatest guy is Perl community </span><span style="color:#800000;"><strong><a href="http://www.stonehenge.com/merlyn/"><span style="color:#333333;">Randal L. Schwartz</span></a></strong></span><span style="color:#800000;"><a href="http://www.stonehenge.com/merlyn/"><span style="color:#333333;">.</span></a></span>

<span style="color:#800000;"><strong><span style="color:#333333;">Happy reading!</span></strong></span>