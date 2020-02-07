---
id: 2066
title: Date printf formats Perl Date::Manip
date: 2019-08-07T17:59:41+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/08/2053-revision-v1/
permalink: /2019/08/07/2053-revision-v1/
---
A quick look at wonderful Perl module Date::Manip printf options<figure class="wp-block-image">

<img src="http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1.png" alt="" class="wp-image-2056" srcset="http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1.png 600w, http://pradeeppant.com/wp-content/uploads/2019/07/date_format_printf_1-234x300.png 234w" sizes="(max-width: 600px) 100vw, 600px" /> </figure> 

Example: 

<pre class="wp-block-code"><code>my $present_date_hash = Date::Manip::Date->new("today");
my $present_date = $present_date_hash->printf(""%Y-%m-%d %H:%M:%S");</code></pre>

More more on Date::Manip please refer [CPAN](https://metacpan.org/pod/Date::Manip)