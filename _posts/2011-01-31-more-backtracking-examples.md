---
id: 263
title: More backtracking examples
date: 2011-01-31T05:45:30+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=263
permalink: /2011/01/31/more-backtracking-examples/
jabber_published:
  - "1296433780"
dsq_thread_id:
  - "783087539"
---
<span style="color:#888888;"><span style="color:#000000;">Backtracking might be costly so one should try to avoid useless backtracking. Perl regx have  special form of parentheses: (?>&#8230;). These are called Perl’s “don’t-ever-backtrack-into-me” markers. They will tell the regex engine that the enclosed sub-pattern can safely be skipped over during backtracking. As we know that the re-matching the contents either won’t succeed or, if it does succeed, won’t help the overall match. So these markers helps to avoid useless backtracking and saves a lot of tim</span>e.</span>

<span style="color:#008000;">Some more useful links and examples can be found at:</span>

[<span style="color:#00ffff;">http://codenode.com/2010/02/28/debugging-perl-regex-backtracking/</span>](http://codenode.com/2010/02/28/debugging-perl-regex-backtracking/)

<span style="color:#00ffff;">Perl Regx documentation page <a href="http://perldoc.perl.org/perlre.html" target="_blank">Perlre</a> on <a href="http://perldoc.perl.org" target="_blank">Perldoc</a></span>

<span style="color:#00ffff;">Perl Best Practices by <a href="http://damian.conway.org/">Damian Conway </a></span>