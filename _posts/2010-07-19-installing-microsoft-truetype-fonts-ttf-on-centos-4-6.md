---
id: 99
title: Installing Microsoft TrueType fonts (TTF) on CentOS 4.6 and RHEL 4
date: 2010-07-19T11:53:27+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=99
permalink: /2010/07/19/installing-microsoft-truetype-fonts-ttf-on-centos-4-6/
jabber_published:
  - "1279520609"
email_notification:
  - "1325670203"
dsq_thread_id:
  - "780523850"
---
<div id="_mcePaste" style="padding-left:30px;">
  Default Linux installation (Cent OS in this case) doesn&#8217;t contain true type fonts. The application like open office, PDF generators requires proper fonts to embed into if not it will use the free system fonts which can create a lot of issues like  pdf, not showing content properly etc. It&#8217;s always good idea to install ms core fonts Well you can buy more fonts as per your requirement if you want.
</div>

<div style="padding-left:30px;">
  To install the ms core fonts follow the below steps <span style="color:#33cccc;">(Login as a ROOT):</span>
</div>

<div style="padding-left:30px;">
  <ul>
    <li>
      <span style="color:#993300;">Download cab extractor:</span><a href="http://prdownloads.sourceforge.net/corefonts/cabextract-0.6-1.i386.rpm?download" target="_blank">cabextract-0.6-1.i386.rpm</a>
    </li>
  </ul>
</div>

<div id="_mcePaste" style="padding-left:30px;">
  <span style="color:#993300;">Install RPM: </span>Change the directory to download folder and run the follwing command:
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;">#rpm -ivh cabextract-0.6-1.i386.rpm</span>
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;"><br /> </span>
</div>

<div style="padding-left:30px;">
  <ul>
    <li>
      <span style="color:#993300;">Download ms core fonts:</span><a href="http://prdownloads.sourceforge.net/corefonts/msttcorefonts-1.3-4.spec?download" target="_blank">msttcorefonts-1.3-4.spec</a>
    </li>
  </ul>
</div>

<div id="_mcePaste" style="padding-left:30px;">
  <span style="color:#993300;">Create RPM:</span> Change the directory to download folder and run the follwing command
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;">#rpmbuild -bb msttcorefonts-1.3-4.spec</span>
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;"><br /> </span>
</div>

<div id="_mcePaste" style="padding-left:30px;">
  (This step will download Microsoft CAB files and extracts the fonts and builds an RPM.  This will use system utilities <span style="color:#33cccc;">[wget, rpm-build, chkfontpath, fc-cache, ttmkfdir]</span> and also check that http port 80 opened or not. This process will download the executable for all the font files.
</div>

<div id="_mcePaste" style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
  This step will create RPM in <span style="color:#33cccc;">/usr/src/redhat/RPMS/noarch/msttcorefonts-1.3-4.noarch.rpm</span>
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
  <ul>
    <li>
      <span style="color:#993300;">Installing RPM: </span>Change the directory to <span style="color:#33cccc;">/usr/src/redhat/RPMS/noarch/ <span style="color:#000000;">and </span></span>run the follwing command
    </li>
  </ul>
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;">#</span> <span style="color:#ff6600;">rpm -ivh msttcorefonts-1.3-4.noarch.rpm</span>
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;"><br /> </span>
</div>

<div style="padding-left:30px;">
  <ul>
    <li>
      <span style="color:#993300;">Restart X server:</span>
    </li>
  </ul>
</div>

<div style="padding-left:30px;">
</div>

<div id="_mcePaste" style="padding-left:30px;">
  <span style="color:#ff6600;">/sbin/service xfs restart</span>
</div>

<div style="padding-left:30px;">
  <span style="color:#ff6600;"><br /> </span>
</div>

<div style="padding-left:30px;">
  Now you can check the newly installed fonts on <span style="color:#33cccc;">/usr/X11R6/lib/X11/fonts/TTF</span>
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
  <span style="color:#33cccc;"><strong><span style="color:#993300;">Important Note: </span></strong><span style="color:#993300;"><span style="color:#008080;"> Sometimes you might need to modify the </span></span></span><span style="color:#ff6600;">msttcorefonts-1.3-4.spec <span style="color:#008080;">file  </span><span style="color:#008080;">for adding<a href="http://sourceforge.net/projects/mscorefonts/files/MS%20Core%20Fonts/win/"> new address of mscorefonts location in sourceforge.net</a>. </span></span><span style="color:#33cccc;"><span style="color:#993300;"><span style="color:#008080;"> If you still face problems downloading font file then you can use <a href="http://www.box.com/s/ghhbz7frx89lcgq75o5o">my own font RPM <span style="color:#ff6600;">[</span></a></span></span></span><span style="color:#008080;"><span style="color:#ff6600;"><a href="http://www.box.com/s/ghhbz7frx89lcgq75o5o">msttcorefonts-1.3-4.noarch.rpm]</a>.  <span style="color:#008080;">Y</span></span>ou can download and install directly using<span style="color:#ff6600;"> # rpm -ivh msttcorefonts-1.3-4.noarch.rpm</span>.</span>
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
</div>

<div style="padding-left:30px;">
  <span style="color:#008080;">Good Luck!</span>
</div>

Enjoy new fonts in your Linux machine.