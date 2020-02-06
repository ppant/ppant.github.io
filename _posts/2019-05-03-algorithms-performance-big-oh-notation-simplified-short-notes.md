---
id: 2022
title: 'Algorithms performance: big O notation: simplified short notes'
date: 2019-05-03T21:58:49+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2022
permalink: /2019/05/03/algorithms-performance-big-oh-notation-simplified-short-notes/
---
 The big O notation is used to analyze runtime time complexity. big O notation provides an abstract measurement by which we can judge the performance of algorithms without using mathematical proofs. Some of the most common big O notations are:

  * **O(1)** : **constant**: the operation doesn&#8217;t depend on the size of its input, e.g. adding a node to the tail of a linked list where we always maintain a pointer to the tail node.
  * **O(n)**: **linear**: the run time complexity is proportionate to the size of n.
  * **O(log n)**: **logarithmic**: normally associated with&nbsp;algorithms&nbsp;that break the problem into similar chunks per each invocation, e.g. searching a binary search tree.
  * **O(n log n)**: **just n log n**: usually&nbsp;associated&nbsp;with an&nbsp;algorithm&nbsp;that breaks the problem into smaller chunks per each invocation, and then takes the results of these smaller&nbsp;chunks&nbsp;and&nbsp;stitches&nbsp;them back together, e.g, quicksort.
  * **O(n2): quadratic**: e.g. bubble sort.
  * **O(n3):** **cubic**: very rare
  * **O(2n):** **exponential**: incredibly rare.

**Brief explanation:**&nbsp; &nbsp; &nbsp;  
Cubic and exponential algorithms should only ever be used for very small problems (if ever!); avoid them if feasibly possible. If you encounter them then this is really a signal for you to review the design of your algorithm always look for algorithm optimization&nbsp;particularly&nbsp;loops and recursive calls.&nbsp;

The biggest asset that big O notation gives us is that it allows us to essentially discard things like hardware means if you have two sorting algorithms, one with a quadric run time and the other with a logarithmic run time then logarithmic algorithm will always be faster than the quadratic one when the data set becomes suitably large. This applies even if the former is ran on a machine that is far faster than the latter, Why? 

Because big O notation isolates a key factor in algorithm analysis: growth. An algorithm with quadratic run time grows faster than one with logarithmic run time. 

**Note:** The above notes are for quick reference. Understanding algorithmic performance is a complex but interesting field. I would recommend picking a good book to understand the nitty-gritty of big O and other notations.