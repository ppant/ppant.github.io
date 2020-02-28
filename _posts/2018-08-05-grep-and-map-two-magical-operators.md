---
id: 791
title: grep and map-Two magical operators
date: 2018-08-05T18:07:37+05:30
author: Pradeep Pant
layout: post
guid: /?p=791
permalink: /2018/08/05/grep-and-map-two-magical-operators/
---
Over the years I have extensively used `map` and `grep` in Perl, JavaScript, Python, Linux. I am sure most of the programmers love using these two operators. Read below some of my personal notes gathered from several resources and own understanding. 

**map &#8211; transforms the values of a list**

The &#8220;map&#8221; function applies a transformation to each element of a list and returns the result, leaving the original list unchanged. A map can also be seen as the form of `foreach` loop but with the `map`, the implementation is much cleaner.

**Ex:** `map { $_ => undef}` is better than, `map{$_=>1}` the former one will save memory. It&#8217;s a better idea to use `undef` instead of 1.

Instead of one scalar of the value &#8216;1&#8217; for every key, you get to share the same undef value for all the keys and thus don&#8217;t have to allocate tons of memory you aren&#8217;t going to use anyway.

The above idiom is a simple way of creating a list of unique values from another list, as the output of the code aptly demonstrates. However, with all those curly braces it may not be immediately obvious what&#8217;s going on, so let&#8217;s break it down.

`map { $_ => 1 } @list`

This is pretty straight-forward &#8211; create a list of key-value pairs where the keys are the values from `@list`

`{ map { $_ => 1 } @list }`

The surrounding pair of curly braces creates an anonymous hash which is populated with they key-value pairs from the `map` statement. So we now have a hash reference to an anonymous hash whose keys are the elements from `@list`, and because hash keys are unique, the keys of the anonymous hash represents a unique set of values. 

`keys %{ { map { $_ => 1 } @list } }`

Finally, with the last pair of curly braces, the hash reference to the anonymous hash is dereferenced and we get its list of keys.

**grep &#8211; filters a list**

The &#8220;grep&#8221; function returns only the elements of a list that meet a certain condition:

`@positive_numbers = grep($_ > 0, @numbers);`

As you can see, each element is refered to as &#8220;$_&#8221;. This (plus the fact that parentheses are optional) allows you write commands that look similar to invocations of the Unix &#8220;grep&#8221; program:

`@non_blank_lines = grep /S/, @lines;`

In addition, you can specify a code block rather than a single condition:

`@non_blank_lines = grep { /S/ } @lines; # Equivalent to the above.`

Obviously it doesn&#8217;t matter in this case, but code blocks are helpful when you want a complex filter with multiple lines of code. The result of the code block is the result of the last statement executed:  
`<br />
# All positive numbers can be used as exponents,<br />
# but negative exponents must be integers.<br />
@can_be_used_as_exponent = grep {<br />
if ( $_ < 0 ) {<br />
! /./; # No decimal point -> integer.<br />
}<br />
else {<br />
1; # Always true.<br />
}<br />
} @array;`

 **What &#8220;grep&#8221; and &#8220;map&#8221; have in common?**

`"grep"` and `"map"` have a lot in common. They both &#8220;magically&#8221; take a piece of code (either an expression or a code block) as a parameter. You need to put a comma after an expression but shouldn&#8217;t put a comma after a code block. Changing `"$_"` in `"grep"` or `"map"` will change the original list.

This isn&#8217;t generally a good idea because it makes the code hard to read. Remember that `"map"` builds a list of results by evaluating an expression, NOT by setting `"$_"`. A side effect of this fact is that you should not use `"s///"` with `"map"`. The `"s///"` operator changes `"$_"` rather than returning a result, so you won&#8217;t get what you would expect if you use it with `"map"` (and you CERTAINLY shouldn&#8217;t use it with `"grep"`).

Happy programming!

**References:**  
[Discussion on PerlMonks](https://www.perlmonks.org/?node_id=280658)  
[perldoc](https://perldoc.perl.org/functions/map.html)