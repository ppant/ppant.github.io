---
id: 1190
title: out of memory redhat
date: 2013-10-18T16:45:38+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/10/1188-revision-v1/
permalink: /2013/10/18/1188-revision-v1/
---
<div>
  <span style="font-family: Verdana;">My redhat based virtual machine is becoming very slow (almost died) and then I found a message out of memory, after doing a bit analysis and search I found that this is known issue and reported in redhat bug tracker.</span>
</div>

<div>
</div>

<div>
  <span style="font-family: Verdana; line-height: 1.5;">There are two solutions (at this point of time)</span>
</div>

<div>
  <span style="font-family: Verdana; line-height: 1.5;">Go to </span><b style="font-family: Verdana; line-height: 1.5;">/etc/sysconfig/i18n</b><span style="font-family: Verdana;"><span style="line-height: 1.5;"> this file contains a reference to unicode (UTF-8) we have take out all the </span>references<span style="line-height: 1.5;"> to UTF-8)</span></span>
</div>

<div>
  Before:
</div>

<div>
  <div>
    <pre><span style="font-family: Verdana;">LANG="en_US.UTF-8"
SUPPORTED="en_US.UTF-8:en_US:en"
SYSFONT="latarcyrheb-sun16"
</span></pre>
  </div>
  
  <div>
    <span style="font-family: Verdana; line-height: 1.5;"> After:</span>
  </div>
  
  <div>
    <pre><span style="font-family: Verdana;">LANG="en_US" 
SUPPORTED="en_US:en" 
SYSFONT="latarcyrheb-sun16" 
</span></pre>
  </div>
  
  <div>
    <a style="line-height: 1.5;" href="http://wiki.zimbra.com/wiki/CentOS_-_UTF-8_-_unicode_start"><span style="font-family: Verdana;">http://wiki.zimbra.com/wiki/CentOS_-_UTF-8_-_unicode_start</span></a>
  </div>
  
  <div>
    <span style="font-family: Verdana;"> </span>
  </div>
  
  <div>
    <span style="font-family: Verdana;">another solution is to change the shell from &#8220;bash&#8221; to &#8220;sh&#8221;. </span>
  </div>
  
  <div>
    <span style="font-family: Verdana;"> </span>
  </div>
  
  <div>
    <pre><span style="color: #7b003d; font-family: Verdana;"> The problem is that setting BASH_ENV=~/.bashrc runs /etc/profile,
 which sources <b>/etc/profile.d/lang.sh</b>.  If TERM=linux, lang.sh runs
 <b>/bin/unicode_start</b> sending the whole process into an infinite
  loop.

 The resolution is to change the first line of /etc/unicode_start
 from "<b>#!/bin/bash</b>" to "<b>#!/bin/sh</b>".  This seems to be the way
 upstream (Fedora 12, at least) is written.</span>
<span style="color: #7b003d; font-family: Verdana;">Link: </span><a href="https://bugzilla.redhat.com/show_bug.cgi?id=622981">https://bugzilla.redhat.com/show_bug.cgi?id=622981

</a></pre>
    
    <div>
      <code>sys-unconfig</code> sources <code>/etc/init.d/functions</code> which in turn can source<code>/etc/profile.d/lang.sh</code> which eventually calls the command <code>/bin/unicode_start</code>. If your <code>TERM</code> variable happens to be set to the terminal type &#8220;linux&#8221;<code>/bin/unicode_start</code> will hang. Changing your <code>TERM</code> to &#8220;xterm&#8221; allows the command to succeed. It probably works with other terminal types as well.
    </div>
    
    <pre><a href="https://bugzilla.redhat.com/show_bug.cgi?id=622981"> </a></pre>
  </div>
</div>