---
id: 114
title: Installing Perl modules with cpanminus
date: 2010-07-23T09:22:09+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=114
permalink: /2010/07/23/installing-perl-modules-with-cpanminus/
jabber_published:
  - "1279857129"
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1282878460";}'
dsq_thread_id:
  - "780542348"
---
While browsing CPAN I found an intersting module by [Tatsuhiko Miyagawa](http://search.cpan.org/~miyagawa/) [cpanminus](http://search.cpan.org/~miyagawa/App-cpanminus-1.0006/lib/App/cpanminus.pm).  Basically, this is a script to get, unpack, build and install modules from CPAN. The best part of  is it&#8217;s dependency free, requires zero configuration, and stands alone. When running, it requires only 10MB of RAM. [Source: [CPAN](http://search.cpan.org/~miyagawa/App-cpanminus-1.0006/lib/App/cpanminus.pm)]

There are Debian packages, RPMs, FreeBSD ports, and packages for other operation systems available. If you want to use the package management system, search for cpanminus and use the appropriate command to install.

You can also build from latest [source](//github.com/miyagawa/cpanminus.git) itself.

I have tried it on my CentOs 4.6 and Windows XP machine. Some of the advantages which I can see at first place are:

  * It seems to consume lesser memory than traditional like CPAN and CPANPLUS which sometime goes out of the memory for heavy installation.
  * It&#8217;s provides really quiet installation in comparison to CPAN. Not many questions.
  * I think it&#8217;s good for beginners
  * Automates installation and install dependencies without CPAN installed so no need to download TAR unpack, makefile, make, make test stuff.

Will try to get some  more findings.

Cheers,