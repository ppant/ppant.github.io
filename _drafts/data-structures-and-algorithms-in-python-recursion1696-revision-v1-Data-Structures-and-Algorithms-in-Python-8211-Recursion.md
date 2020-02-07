---
id: 1698
title: 'Data Structures and Algorithms in Python &#8211; Recursion'
date: 2017-09-05T15:26:12+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2017/09/1696-revision-v1/
permalink: /2017/09/05/1696-revision-v1/
---
# Computes the cumulative sum &#8211; Recursion

Aim is to write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer. For example, if n=4 , return 4+3+2+1+0, which is 10. We always should take care of the base case. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1). In this case, we have: n + (n-1) + (n-2) + &#8230;. + 0. Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c1">print</span> (recursion_cululative_sum(<span class="pl-c1">5</span>))</pre>
</div>

# <a id="user-content-sum-of-digits---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#sum-of-digits---recursion" aria-hidden="true"></a>Sum of digits &#8211; Recursion

Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1 Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c1">print</span> (recursion_sum_digits(<span class="pl-c1">12</span>))</pre>
</div>

# <a id="user-content-word-split---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#word-split---recursion" aria-hidden="true"></a>Word split &#8211; Recursion

Create a function called word\_split() which takes in a string phrase and a set list\_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable. Example:

<div class="highlight highlight-source-python">
  <pre> <span class="pl-c1">print</span> (word_split(<span class="pl-s"><span class="pl-pds">'</span>themanran<span class="pl-pds">'</span></span>,[<span class="pl-s"><span class="pl-pds">'</span>the<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>ran<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>man<span class="pl-pds">'</span></span>]))</pre>
</div>

# <a id="user-content-reverse-a-string---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#reverse-a-string---recursion" aria-hidden="true"></a>Reverse a string &#8211; Recursion

Implement a recursive reverse. Example:

<div class="highlight highlight-source-python">
  <pre> <span class="pl-c1">print</span>(reverse_str(<span class="pl-s"><span class="pl-pds">'</span>hello world<span class="pl-pds">'</span></span>))</pre>
</div>

# <a id="user-content-list-all-the-permutation-of-a-string---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#list-all-the-permutation-of-a-string---recursion" aria-hidden="true"></a>List all the permutation of a string &#8211; Recursion

Given a string, write a function that uses recursion to output a list of all the possible permutations of that string. For example, given s=&#8217;abc&#8217; the function should return [&#8216;abc&#8217;, &#8216;acb&#8217;, &#8216;bac&#8217;, &#8216;bca&#8217;, &#8216;cab&#8217;, &#8216;cba&#8217;] This way of doing permutaion is for learning in real scenerios better to use excellant Python library &#8220;ltertools&#8221; with current approach there are n! permutations, so the it looks that algorithm will take O(n*n!)time Example:

<div class="highlight highlight-source-python">
  <pre> <span class="pl-c1">print</span>(permute(<span class="pl-s"><span class="pl-pds">'</span>abc<span class="pl-pds">'</span></span>))</pre>
</div>

# <a id="user-content-implement-fibonacci-sequence-with-simple-iteration" class="anchor" href="https://github.com/ppant/DS-Algos-Python#implement-fibonacci-sequence-with-simple-iteration" aria-hidden="true"></a>Implement fibonacci sequence with simple iteration

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># We'll try to find the 9th no in the fibonacci sequence which is 34</span>
<span class="pl-c1">print</span> (fibonacci_itertaive(<span class="pl-c1">9</span>))
<span class="pl-c"># 34</span>
<span class="pl-c"># 0, 1, 1, 2, 3, 5, 8, 13, 21, 34</span>
<span class="pl-c"># The recursive solution is exponential time Big-O , with O(n).</span></pre>
</div>

# <a id="user-content-implement-fibonacci-sequence---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#implement-fibonacci-sequence---recursion" aria-hidden="true"></a>Implement fibonacci sequence &#8211; Recursion

Our function will accept a number n and return the nth number of the fibonacci sequence Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,&#8230; starts off with a base case checking to see if n = 0 or 1, then it returns 1. Else it returns fib(n-1)+fib(n+2).

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># We'll try to find the 9th no in the fibnacci sequence which is 34</span>
<span class="pl-c1">print</span> (fibonacci_recursion(<span class="pl-c1">9</span>))
<span class="pl-c"># 0, 1, 1, 2, 3, 5, 8, 13, 21, 34</span>
<span class="pl-c"># The recursive solution is exponential time Big-O , with O(2^n). However, </span>
<span class="pl-c"># its a very simple and basic implementation to consider</span></pre>
</div>

# <a id="user-content-implement-fibonacci-sequence---dynamic-programming" class="anchor" href="https://github.com/ppant/DS-Algos-Python#implement-fibonacci-sequence---dynamic-programming" aria-hidden="true"></a>Implement fibonacci sequence &#8211; Dynamic programming

Implement the function using dynamic programming by using a cache to store results (memoization). memoization + recursion = dynamic programming

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># We'll try to find the 9th no in the fibnacci sequence which is 34</span>
<span class="pl-c1">print</span> (fibonacci_dynamic(<span class="pl-c1">9</span>))
<span class="pl-c"># 0, 1, 1, 2, 3, 5, 8, 13, 21, 34</span>
<span class="pl-c"># The recursive-memoization solution is exponential time Big-O , with O(n)</span></pre>
</div>

# <a id="user-content-implement-coin-change-problem---recursion" class="anchor" href="https://github.com/ppant/DS-Algos-Python#implement-coin-change-problem---recursion" aria-hidden="true"></a>Implement coin change problem &#8211; Recursion

Given a target amount n and a list (array) of distinct coin values, what&#8217;s the fewest coins needed to make the change amount. 1+1+1+1+1+1+1+1+1+1 5 + 1+1+1+1+1 5+5 10 With 1 coin being the minimum amount.

<div class="highlight highlight-source-python">
  <pre><span class="pl-c1">print</span> (coin_change_recursion(<span class="pl-c1">8</span>,[<span class="pl-c1">1</span>,<span class="pl-c1">5</span>]))
<span class="pl-c"># 4</span>
<span class="pl-c"># Note:</span>
<span class="pl-c"># The problem with this approach is that it is very inefficient! It can take many, </span>
<span class="pl-c"># many recursive calls to finish this problem and its also inaccurate for non </span>
<span class="pl-c"># standard coin values (coin values that are not 1,5,10, etc.)</span></pre>
</div>

# <a id="user-content-implement-coin-change-problem---dynamic-programming" class="anchor" href="https://github.com/ppant/DS-Algos-Python#implement-coin-change-problem---dynamic-programming" aria-hidden="true"></a>Implement coin change problem &#8211; Dynamic programming

Given a target amount n and a list (array) of distinct coin values, what&#8217;s the fewest coins needed to make the change amount.

<div class="highlight highlight-source-python">
  <pre><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span>
<span class="pl-c1">5</span> <span class="pl-k">+</span> <span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span><span class="pl-c1">1</span>
<span class="pl-c1">5</span><span class="pl-k">+</span><span class="pl-c1">5</span>
<span class="pl-c1">10</span>
With <span class="pl-c1">1</span> coin being the minimum amount.
<span class="pl-c"># Caching</span>
target <span class="pl-k">=</span> <span class="pl-c1">74</span>
coins <span class="pl-k">=</span> [<span class="pl-c1">1</span>,<span class="pl-c1">5</span>,<span class="pl-c1">10</span>,<span class="pl-c1">25</span>]
known_results <span class="pl-k">=</span> [<span class="pl-c1"></span>]<span class="pl-k">*</span>(target<span class="pl-k">+</span><span class="pl-c1">1</span>)

<span class="pl-c1">print</span> (coin_change_dynamic(target,coins,known_results))

</pre>
</div>

Check [GitHub](https://github.com/ppant/DS-Algos-Python) for the full working code.

I will keep adding more problems/solutions.

Stay tuned!

Ref:  The inspiration of implementing DS in Python is from [this](http://interactivepython.org/runestone/static/pythonds/index.html) course