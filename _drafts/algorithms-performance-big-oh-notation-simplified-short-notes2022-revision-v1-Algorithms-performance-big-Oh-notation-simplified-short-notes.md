---
id: 2024
title: 'Algorithms performance: big-Oh notation: simplified short notes'
date: 2019-05-03T13:55:53+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/05/2022-revision-v1/
permalink: /2019/05/03/2022-revision-v1/
---
 The big-Oh notation is used to analyze runtime time complexity. big-Oh notation provides an abstract measurement by which we can judge the performance of algorithms without using mathematical proofs. Some of the most common big-Oh notations are:

  * **O(1)** : **constant**: the operation doesn&#8217;t depend on the size of its input, e.g. adding a node to the tail of a linked list where we always maintain a pointer to the tail node.
  * **O(n)**: **linear**: the run time complexity is proportionate to the size of n.
  * **O(log n)**: **logarithmic**: normally associated with algorithms that break the problem into similar chunks per each invocation, e.g. searching a binary search tree.
  * **O(n log n)**: **just n log n**: usually associated with an algorithm that breaks the problem into smaller chunks per each invocation, and then takes the results of these smaller chunks and stitches them back together, e.g, quicksort.
  * **O(n2): quadratic**: e.g. bubble sort.
  * **O(n3):** **cubic**: very rare
  * **O(2n):** **exponential**: incredibly rare.

**Brief explanation:**       
Cubic and exponential algorithms should only ever be used for very small problems (if ever!); avoid them if feasibly possible. If you encounter them then this is really a signal for you to review the design of your algorithm always look for algorithm optimization particularly loops and recursive calls. 

The biggest asset that big Oh notation gives us is that it allows us to essentially discard things like hardware means if you have two sorting algorithms, one with a quadric run time and the other with a logarithmic run time then logarithmic algorithm will always be faster than the quadratic one when the data set becomes suitably large. This applies even if the former is ran on a machine that is far faster than the latter, Why? 

Because big-Oh notation isolates a key factor in algorithm analysis: growth. An algorithm with quadratic run time grows faster than one with logarithmic run time. 

I would recommend to pick a good book to understand the nitty-gritty of big-Oh and other notations.