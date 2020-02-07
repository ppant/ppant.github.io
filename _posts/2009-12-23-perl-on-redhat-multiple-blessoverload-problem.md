---
id: 30
title: 'Perl on RedHat &#8211; multiple bless/overload problem'
date: 2009-12-23T20:27:26+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=30
permalink: /2009/12/23/perl-on-redhat-multiple-blessoverload-problem/
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1282296836";}'
dsq_thread_id:
  - "783047067"
---
I was reading over internet regarding the performance issue of Perl bundled in some Redhat versions (A combination of Rehhat and Perl version) which uses multiple bless/overload. <a href="http://blog.vipul.net/" target="_blank">Vipul&#8217;s blog</a> has given a good insight on this problem.

Well, Red hat has finally registered the bug last year on <a href="https://bugzilla.redhat.com/show_bug.cgi?id=379791" target="_blank">Bugzilla</a>.

Would recommend  everybody falling under this should  test it.  You can test your running installations by using the program given in Bugzilla.  I have done at my end and fortunately I am out of the bug.  I was running Cent Os 4.6 with Perl 5.8.6.

All the best