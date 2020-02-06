---
id: 430
title: Testing Javascript in Perl applications
date: 2011-03-16T22:22:43+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=430
permalink: /2011/03/16/testing-javascript-in-perl-applications/
jabber_published:
  - "1300294367"
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1330163431";}'
dsq_thread_id:
  - "782725442"
---
There is a tool called <a href="http://seleniumhq.org/" target="_blank">Selenium</a> which is used to test the Javascript component in Perl based applications. This is used to run tests directly in the browser. Actually this tool sits between Perl application, test script and browser. The test script sends the Selenium server commands to run inside the web browser. The web browser then executes those commands, and returns the results to Selenium server and then to test script. It requires JRE and a working web server to work with.

<a href="http://search.cpan.org/~jrockway/" target="_blank">Jonathan Rockway</a> in his <a href="https://www.packtpub.com/catalyst-perl-web-application/book" target="_blank">book</a> has explained and used this in Catalyst applications.