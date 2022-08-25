---
id: 179
title: Backtracking with Perl Regular expression
date: 2011-01-11T22:00:04+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=179
permalink: /2011/01/11/backtracking-with-perl-regular-expression/
jabber_published:
  - "1294763404"
dsq_thread_id:
  - "782948101"
---
<span style="color:#000080;">Wikipedia<strong> <span style="font-weight:normal;">says </span><a href="http://en.wikipedia.org/wiki/Backtracking">Backtracking</a></strong><a href="http://en.wikipedia.org/wiki/Backtracking"> </a><em>is a general algorithm for finding all (or some) solutions to some computational problem, that incrementally builds candidates to the solutions, and abandons each partial candidate c (&#8220;backtracks&#8221;) as soon as it determines that  cannot possibly be completed to a valid solution.</em></span>

<span style="color:#008080;"><strong><span style="color:#993300;">What it meant for Perl: </span></strong></span>

<span style="color:#000080;">In fact Backtracking mechanism is core functionality of languages like <a href="http://en.wikipedia.org/wiki/Prolog" target="_blank">PROLOG</a>. Perl implements it using regex engine.</span>

<span style="color:#000080;">Adding backtracking mechanism to our programming arsenal will bring alot of new functionality. This will help us solve problems that otherwise cost us alot of time and effort.</span>

<span style="color:#000080;">A fundamental feature of Perl regular expression matching involves the notion called <em><a href="http://en.wikipedia.org/wiki/Backtracking" target="_blank">backtracking</a></em>, which is currently used (when needed) by all regular non-possessive expression quantifiers, namely <code>*</code> , <code>*?</code> , <code>+</code> ,<code>+?</code>, <code>{n,m}</code>, and <code>{n,m}?</code>. Backtracking is often optimized internally.</span>

<span style="color:#000080;">For a regular expression to match, the <em>entire</em> regular expression must match, not just part of it. So if the beginning of a pattern containing a quantifier succeeds in a way that causes later parts in the pattern to fail, the matching engine backs up and recalculates the beginning part&#8211;that&#8217;s why it&#8217;s called backtracking.</span>

<span style="color:#993300;">I will try to explain backtracking with an example in my next post<span style="color:#993300;">.</span></span>

<span style="color:#993300;">Thanks</span>