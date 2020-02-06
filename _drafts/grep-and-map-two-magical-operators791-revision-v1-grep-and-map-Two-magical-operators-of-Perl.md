---
id: 1776
title: 'grep and map: Two magical operators of Perl'
date: 2018-08-05T17:30:09+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2018/08/791-revision-v1/
permalink: /2018/08/05/791-revision-v1/
---
<pre><span style="color: #000000;">I am writing some of my experiences with map and grep in Perl over the years..</span>

<strong><span style="color: #000000;">map - transforms the values of a list</span></strong>
The "map" function applies a transformation to each element of a list and returns the result, leaving the original list unchanged. <span style="color: #000000;">A map can also be seen as the form of </span>foreach <span style="color: #000000;"> loop but with the map, 
the implementation is much cleaner. </span>

<span style="color: #000000;">Ex: map { $_ =&gt; undef} is better than map{$_=&gt;1}, the former one will save memory</span>
<span style="color: #000000;">It's a better idea to use </span>undef <span style="color: #000000;"> instead of 1.</span>

<span style="color: #000000;">Instead of one scalar of the value '1' for every key, you get to share the same </span>undef <span style="color: #000000;"> value for all the keys and thus don't have to allocate tons of memory you aren't going to use anyway. </span>

<span style="color: #000000;">The above idiom is a simple way of creating a list of unique values from another list, as the output of the code aptly demonstrates. 
However, with all those curly braces it may not be immediately obvious what's going on, so let's break it down.</span>

<span style="color: #000000;"><tt>map { $_ =&gt; 1 } @list </tt></span>

<span style="color: #000000;">This is pretty straight-forward - create a list of key-value pairs where the keys are the values from <tt>@list</tt>.</span>

<span style="color: #000000;"><tt>{ map { $_ =&gt; 1 } @list } </tt></span>

<span style="color: #000000;">The surrounding pair of curly braces creates an anonymous hash which is populated with </span>they <span style="color: #000000;"> 
key-value pairs from the map<tt></tt> statement. So we now have a hash reference to an anonymous hash </span>who's <span style="color: #000000;"> keys are the elements from <tt>@list</tt>, and because hash keys are unique, the keys of the anonymous 
hash represent a unique set of values.</span>

<span style="color: #000000;"><tt>keys %{ { map { $_ =&gt; 1 } @list } } </tt></span>

<span style="color: #000000;">Finally, with the last pair of curly braces, the hash reference to the anonymous hash is dereferenced and we get its list of keys.</span>


<span style="color: #000000;"><strong>grep - filters a list</strong>

The "grep" function returns only the elements of a list that meet a certain condition:

   @positive_numbers = grep($_ &gt; 0, @numbers);

As you can see, each element is refered to as "$_". This (plus the fact that parentheses are optional) allows you write commands that look
similar to invocations of the Unix "grep" program:

   @non_blank_lines = grep /S/, @lines;

In addition, you can specify a code block rather than a single condition:

   @non_blank_lines = grep { /S/ } @lines;     # Equivalent to the above.

Obviously it doesn't matter in this case, but code blocks are helpful when you want a complex filter with multiple lines of code. The result
of the code block is the result of the last statement executed:

   # All positive numbers can be used as exponents,
   # but negative exponents must be integers.
   @can_be_used_as_exponent = grep {
     if ( $_ &lt; 0 ) {
       ! /./;          # No decimal point -&gt; integer.
     }
     else {
       1;               # Always true.
     }
   } @array;</span></pre>

<div>
  <pre><span style="color: #000000;"><strong>
What "grep" and "map" have in common?</strong>

"grep" and "map" have a lot in common. They both "magically" take a piece of code (either an expression or a code block) as a parameter. You
need to put a comma after an expression but shouldn't put a comma after a code block.

Changing "$_" in "grep" or "map" will change the original list. This isn't generally a good idea because it makes the code hard to read.
Remember that "map" builds a list of results by evaluating an expression, NOT by setting "$_".

A side effect of this fact is that you should not use "s///" with "map". The "s///" operator changes "$_" rather than returning a result, so you
won't get what you would expect if you use it with "map" (and you CERTAINLY shouldn't use it with "grep").</span>

Happy programming!

<span style="color: #000000;"><strong>References:</strong> </span>
<span style="color: #000000;"><a style="color: #000000;" href="https://www.perlmonks.org/?node_id=280658">Discussion on PerlMonks</a></span>
<span style="color: #000000;"><a style="color: #000000;" href="https://perldoc.perl.org/functions/map.html">perldoc</a></span></pre>
</div>