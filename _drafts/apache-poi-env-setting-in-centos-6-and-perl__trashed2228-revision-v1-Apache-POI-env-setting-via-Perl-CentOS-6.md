---
id: 2230
title: Apache POI env setting via Perl CentOS 6+
date: 2019-12-04T13:40:36+05:30
author: Pradeep Pant
layout: revision
guid: https://pradeeppant.com/2019/12/04/2228-revision-v1/
permalink: /2019/12/04/2228-revision-v1/
---
Apache POI are the set of Java APIs that can be used to manipulate MS Office and other types of documents. In this post quick info on how to make a dev environment for using Java POI interface using Perl.

  1. Download .bin of [POI version 4.1.1](https://www.apache.org/dyn/closer.lua/poi/release/bin/poi-bin-4.1.1-20191023.tar.gz) and add classpath in .bashrc  
  
    `<em>CLASSPATH="$CLASSPATH:/usr/local/src/poi-4.1.1/poi-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-ooxml-schemas-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-excelant-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-ooxml-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-scratchpad-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-examples-4.1.1.jar:/usr/local/src/poi-4.1.1/ooxml-lib/xmlbeans-3.1.0.jar:/usr/local/src/poi-4.1.1/ooxml-lib/curvesapi-1.06.jar"</em><br><em>export CLASSPATH</em>`
  2. Install Inline module 0.83 (Through CPAN) &#8212;> `<em>$ cpan -i Inline</em> `
  3. Install Inline:: Java module 0.66 (Manually as we need to pass J2SK=/usr/ in Makefile.PL), e.g.;  `$ <em>perl Makefile.PL J2SDK=/usr/</em> `

I will explain in detail more on POI and how to use them in upcoming posts.  
  
**Prerequisites:**  
Java 8