---
id: 1091
title: MojoMojo and Selenium test
date: 2013-07-18T11:52:20+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/429-autosave/
permalink: /2013/07/18/429-autosave/
---
As suggested by [Mateu](http://en.gravatar.com/mateuhunter#photo-0) I was further looking into <a href="http://mojomojo.org/" target="_blank">MojoMojo</a> <a href="http://seleniumhq.org/" target="_blank">Selenium</a> tests on [CPAN](http://search.cpan.org/~mramberg/MojoMojo-1.04/). Actually all <a href="http://cpansearch.perl.org/src/MRAMBERG/MojoMojo-1.04/t/selenium.t" target="_blank">selenium.t</a> tests require a test configuration file **mojomojo.yml** file resides in **t/app/mojomojo.yml** this file is used to add the authentication configurations. Also resides in the same directory the **sqlite** **mojomojo database: mojomojo.db**.

The complete test is as follows:

[code lang=&#8221;perl&#8221;]

#!/usr/bin/env perl  
use strict;  
use warnings;  
use Test::More;

\# This test requires that a Selenium server be running.  
\# A Selenium server # is included in Alien::SeleniumRC which is a dependency of  
\# Test::WWW::Selenium::Catalyst so having it installed should be sufficient to run this test.  
\# # The selenium server is a java application that can also be started like:  
\# java -jar selenium-server.jar  
\# See http://seleniumhq.org/ for the download of Selenium Remote Control (RC) # which includes a selenium server.

BEGIN { eval {require Test::WWW::Selenium::Catalyst};  
plan skip_all => &#8216;Selenium tests need Test::WWW::Selenium::Catalyst&#8217; if $@;  
plan skip\_all => &#8216;Set SELENIUM\_TESTS ENV variable to enable Selenium tests&#8217; unless $ENV{SELENIUM_TESTS};  
plan tests => 22;  
$ENV{MOJOMOJO_CONFIG} = &#8216;t/app/mojomojo.yml&#8217;; }  
Test::WWW::Selenium::Catalyst->import(&#8216;MojoMojo&#8217;);  
my $sel = Test::WWW::Selenium::Catalyst->start;  
$sel->open_ok("/");  
$sel->is\_text\_present_ok("Log in");  
$sel->open_ok("admin.profile");  
$sel->is\_text\_present_ok("Log in");  
$sel->open_ok(".recent");  
$sel->is\_text\_present_ok("Log in");  
$sel->open_ok(".list");  
$sel->is\_text\_present_ok("Log in");  
$sel->click_ok("link=Log in");  
$sel->wait\_for\_page\_to\_load_ok( "15000");  
$sel->type_ok( "loginField", "admin" );  
$sel->type_ok( "pass", "admin" );  
$sel->click_ok("//input[@value=&#8217;Login&#8217;]");  
$sel->wait\_for\_page\_to\_load_ok("15000");  
$sel->is\_text\_present_ok("admin");  
\# Check that .recent was not cached.  
$sel->open_ok(".recent");  
$sel->is\_text\_present_ok("Log out");  
\# Check that profile was no cached.  
$sel->open_ok("admin.profile");  
$sel->is\_text\_present_ok("Log out");  
$sel->open_ok(".list");  
$sel->is\_text\_present_ok("Log out");  
$sel->click_ok("link=Log out");  
[/code]

<span style="color: #000000;">Reference: <a href="http://cpansearch.perl.org/src/MRAMBERG/MojoMojo-1.04/t/selenium.t" target="_blank">MojoMojo on CPAN</a> </span>