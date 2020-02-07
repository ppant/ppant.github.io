---
id: 1092
title: MojoMojo and Selenium test
date: 2011-03-25T09:50:24+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2011/03/429-revision/
permalink: /2011/03/25/429-revision/
---
As suggested by [Mateu](http://en.gravatar.com/mateuhunter#photo-0) I was further looking into <a href="http://mojomojo.org/" target="_blank">MojoMojo</a> <a href="http://seleniumhq.org/" target="_blank">Selenium</a> tests on [CPAN](http://search.cpan.org/~mramberg/MojoMojo-1.04/). Actually all <a href="http://cpansearch.perl.org/src/MRAMBERG/MojoMojo-1.04/t/selenium.t" target="_blank">selenium.t</a> tests require a test configuration file **mojomojo.yml** file resides in **t/app/mojomojo.yml** this file is used to add the authentication configurations. Also resides in the same directory the **sqlite** **mojomojo database: mojomojo.db**.

The complete test is as follows:

> <pre><span style="color:#008000;">#!/usr/bin/env perl
<span style="color:#993300;">use strict;
use warnings;
use Test::More;</span>

# This test requires that a Selenium server be running.  A Selenium server
# is included in Alien::SeleniumRC which is a dependency of
# Test::WWW::Selenium::Catalyst so having it installed should be
# sufficient to run this test.
#
# The selenium server is a java application that can also be started like:
#     java -jar selenium-server.jar
# See http://seleniumhq.org/ for the download of Selenium Remote Control (RC)
# which includes a selenium server.

<span style="color:#993300;">BEGIN {
    eval {require Test::WWW::Selenium::Catalyst};
    plan skip_all =&gt; 'Selenium tests need Test::WWW::Selenium::Catalyst'
        if $@;
    plan skip_all =&gt; 'Set SELENIUM_TESTS ENV variable  to enable Selenium tests'
        unless $ENV{SELENIUM_TESTS};
    plan tests =&gt; 22;
    $ENV{MOJOMOJO_CONFIG} = 't/app/mojomojo.yml';
}

Test::WWW::Selenium::Catalyst-&gt;import('MojoMojo');
my $sel = Test::WWW::Selenium::Catalyst-&gt;start;

$sel-&gt;open_ok("/");
$sel-&gt;is_text_present_ok("Log in");
$sel-&gt;open_ok("admin.profile");
$sel-&gt;is_text_present_ok("Log in");
$sel-&gt;open_ok(".recent");
$sel-&gt;is_text_present_ok("Log in");
$sel-&gt;open_ok(".list");
$sel-&gt;is_text_present_ok("Log in");
$sel-&gt;click_ok("link=Log in");
$sel-&gt;wait_for_page_to_load_ok( "15000");
$sel-&gt;type_ok( "loginField", "admin" );
$sel-&gt;type_ok( "pass",       "admin" );
$sel-&gt;click_ok("//input[@value='Login']");
$sel-&gt;wait_for_page_to_load_ok("15000");
$sel-&gt;is_text_present_ok("admin");

<span style="color:#008000;"># Check that .recent was not cached.</span>
$sel-&gt;open_ok(".recent");
$sel-&gt;is_text_present_ok("Log out");</span>

# Check that profile was no cached.
<span style="color:#993300;">$sel-&gt;open_ok("admin.profile");
$sel-&gt;is_text_present_ok("Log out");
$sel-&gt;open_ok(".list");
$sel-&gt;is_text_present_ok("Log out");
$sel-&gt;click_ok("link=Log out");</span></span>
<span style="color:#008000;">
</span></pre>

<span style="color:#000000;">Reference: <a href="http://cpansearch.perl.org/src/MRAMBERG/MojoMojo-1.04/t/selenium.t" target="_blank">MojoMojo on CPAN</a> </span>