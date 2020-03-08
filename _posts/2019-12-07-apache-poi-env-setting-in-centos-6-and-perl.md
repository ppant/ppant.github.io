---
title: Apache POI env setting in CentOS 6+, Java 8 and Perl 5
date: 2019-12-09T16:57:13+05:30
author: Pradeep Pant
layout: post
---
Apache POI is the set of [**Java APIs**](http://poi.apache.org/apidocs/4.1/) that can be used to manipulate MS Office and other types of documents. This post will give quick info on how to make a [Perl](https://www.perl.org/) based dev environment for Java POI interface.

  1. Download .bin of [POI version 4.1.1](https://www.apache.org/dyn/closer.lua/poi/release/bin/poi-bin-4.1.1-20191023.tar.gz) and add classpath in ````.bashrc```` 
    ````
	CLASSPATH="$CLASSPATH:/usr/local/src/poi-4.1.1/poi-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-ooxml-schemas-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-excelant-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-ooxml-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-scratchpad-4.1.1.jar:/usr/local/src/poi-4.1.1/poi-examples-4.1.1.jar:/usr/local/src/poi-4.1.1/ooxml-lib/xmlbeans-3.1.0.jar:/usr/local/src/poi-4.1.1/ooxml-lib/curvesapi-1.06.jar"````
	````
	export CLASSPATH
	````

  2. Install [Inline module - 0.83](https://metacpan.org/release/Inline) (Through CPAN) ```` $ cpan -i Inline ````
  3. Install [Inline:: Java module 0.66](https://metacpan.org/release/Inline-Java) (Manually as we need to pass ```` J2SK=/usr/```` in ````Makefile.PL````),
  e.g.;  
  ````$perl Makefile.PL J2SDK=/usr/
  ````

You are set to go to use POI API through Perl programs. 

In the next post, I will explain in detail more on POI and how to use them inside a Perl module.

**Prerequisites and references:**  
Java 8  
[POI](https://poi.apache.org/)