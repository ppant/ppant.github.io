---
id: 2053
title: Date print formats Perl Date::Manip
date: 2019-08-07T21:07:33+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2053
permalink: /2019/08/07/date-print-formats-perl-datemanip/
twitter_share:
  - 'a:1:{s:8:"hashtags";a:1:{i:0;s:17:"Perl #Programming";}}'
---
Perl Date::Manip is one of the modules which I use a lot. It&#8217;s a wonderful lib and has very clean API with great documentation. Below is a quick look at Date::Manip print format options which sometimes is very handy. For detailed interpretation and other options encourage to go through Date::Manip on [CPAN](https://metacpan.org/pod/Date::Manip) <figure class="wp-block-image">

<img src="http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1.png" alt="" class="wp-image-2056" srcset="http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1.png 600w, http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1-234x300.png 234w" sizes="(max-width: 600px) 100vw, 600px" /> </figure> 

Example: 

<pre class="wp-block-code"><code>my $present_date_hash = Date::Manip::Date->new("today");
my $present_date = $present_date_hash->printf("%Y-%m-%d %H:%M:%S");</code></pre>

Happy Coding!

also, can check my [previous article](http://pradeeppant.com/2016/03/creating-recurring-date-patterns-using-perl/) on generating date patterns using [Date::Manip](https://metacpan.org/pod/Date::Manip)