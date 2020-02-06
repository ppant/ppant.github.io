---
id: 384
title: PDL A way to deal with larger arrays
date: 2011-02-23T11:29:50+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=384
permalink: /2011/02/23/pdl-a-way-to-deal-with-larger-arrays/
jabber_published:
  - "1298440791"
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1321055699";}'
dsq_thread_id:
  - "785980839"
---
If you are working in scientific domain or using <a href="http://www.bioperl.org/wiki/Main_Page" target="_blank">bioperl</a> where you require to deal with bulk data processing then you should seriously consider learning <a href="http://pdl.perl.org/" target="_blank">PDL</a> (&#8220;Perl Data Language&#8221;). PDL is actually a way to deal with larger arrays in Perl.  It allows large N-dimensional data sets such as large images, spectrogram, etc to be stored efficiently and manipulated quickly.

To say it with the words of [Karl Glazebrook](http://en.wikipedia.org/wiki/Karl_Glazebrook), initiator of the PDL project:

<pre><span style="color:#993300;"><em>    “The PDL concept is to give standard perl5 the ability</em>
<em>    to COMPACTLY store and SPEEDILY manipulate the large</em>
<em>    N-dimensional data sets which are the bread and butter</em>
<em>    of scientific computing. e.g. $a=$b+$c can add two</em>
<em>    2048x2048 images in only a fraction of a second.”</em></span>

<em> </em></pre>

PDL is well suited for matrix computations, general handling of multidimensional data, image processing, general scientific computation, and numerical applications. It supports I/O for many popular image and data formats including 1D (line plots), 2D (images) and 3D (volume visualization, surface plots via OpenGL) etc.

Latest stable release of PDL is PDL-2.4.7 and can be found at <a href="http://search.cpan.org/~chm/PDL-2.4.7/" target="_blank">CPAN</a> or <a href="http://sourceforge.net/projects/pdl/files/" target="_blank">Sourceforge</a>.

Happy learning.