---
id: 2053
title: Date print formats Perl Date::Manip
date: 2019-08-07T21:07:33+05:30
layout: post
categories: [tech]
guid: /?p=2053
permalink: /2019/08/07/date-print-formats-perl-datemanip/
twitter_share:
  - 'a:1:{s:8:"hashtags";a:1:{i:0;s:17:"Perl #Programming";}}'
---
Perl Date::Manip is one of the modules which I use a lot. It's a wonderful lib and has very clean API with great documentation. Below is a quick look at Date::Manip print format options which sometimes is very handy. For detailed interpretation and other options encourage to go through Date::Manip on [CPAN](https://metacpan.org/pod/Date::Manip) <figure>

<img src="/assets/images/date_format_printf_1.png" alt="" /> </figure> 

Example: 

```
my $present_date_hash = Date::Manip::Date->new("today");
my $present_date = $present_date_hash->printf("%Y-%m-%d %H:%M:%S");
```

Happy Coding!

also, can check my [previous article](/2016/03/creating-recurring-date-patterns-using-perl/) on generating date patterns using [Date::Manip](https://metacpan.org/pod/Date::Manip)