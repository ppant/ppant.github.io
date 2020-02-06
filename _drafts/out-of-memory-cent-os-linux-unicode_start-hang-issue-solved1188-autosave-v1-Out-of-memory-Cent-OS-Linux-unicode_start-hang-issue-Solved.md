---
id: 1204
title: 'Out of memory Cent OS Linux: unicode_start hang issue: Solved'
date: 2013-10-19T16:32:46+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/10/1188-autosave-v1/
permalink: /2013/10/19/1188-autosave-v1/
---
<div>
  My Cent OS 5.6 RHEL based virtual machine has suddenly became very slow ..almost died 🙁 after few min I saw a message on console related to &#8220;<strong>Out of memory</strong>&#8220;, after doing a bit analysis and search I found that this is a known issue and also reported in<a href=" https://bugzilla.redhat.com/show_bug.cgi?id=622981"> redhat bug tracker</a> (obviously got resolved in upstream versions).
</div>

<div>
</div>

<div>
  <strong>Reason:</strong> Problem is that setting <span style="color: #993300;"><em>BASH_ENV=~/.bashrc</em></span> runs<em><span style="color: #993300;"> /etc/profile</span></em>, which sources<em><span style="color: #993300;"> /etc/profile.d/lang.sh</span></em>. If <span style="color: #993300;"><em>TERM=linux</em></span>,<em><span style="color: #993300;"> lang.sh</span></em> runs <span style="color: #993300;">/bin/unicode_start</span> sending the whole process into an infinite loop.
</div>

<div>
</div>

<div>
  <p>
    I found two solutions (as of now)
  </p>
  
  <p>
    1. Open<span style="color: #993300;"><em> vi /etc/sysconfig/i18n</em></span> this file contains a reference to unicode (UTF-8). We have take out all the references to UTF-8)
  </p>
  
  <p>
    Code before:
  </p>
  
  <p>
    [code lang=&#8221;js&#8221;]<br /> LANG="en_US.UTF-8"<br /> SUPPORTED="en_US.UTF-8:en_US:en"<br /> SYSFONT="latarcyrheb-sun16"<br /> [/code]
  </p>
  
  <p>
    Code after:
  </p>
  
  <p>
    [code lang=&#8221;js&#8221;]<br /> LANG="en_US"<br /> SUPPORTED="en_US:en"<br /> SYSFONT="latarcyrheb-sun16"<br /> [/code]
  </p>
  
  <p>
    2. Another solution is to change the shell from &#8220;bash&#8221; to &#8220;sh&#8221; in <em><span style="color: #993300;">unicode_start</span></em> script<br /> We need to open the <em><span style="color: #993300;">vi /bin/unicode_start</span> </em>and<em> </em>from first line change <em><span style="color: #993300;">&#8220;#!/bin/bash</span></em>&#8221; to <em><span style="color: #993300;">&#8220;#!/bin/sh</span></em>&#8220;.
  </p>
  
  <p>
    References: <a title="Redhat Bugzilla " href="https://bugzilla.redhat.com/show_bug.cgi?id=622981">https://bugzilla.redhat.com/show_bug.cgi?id=622981</a>
  </p>
</div>