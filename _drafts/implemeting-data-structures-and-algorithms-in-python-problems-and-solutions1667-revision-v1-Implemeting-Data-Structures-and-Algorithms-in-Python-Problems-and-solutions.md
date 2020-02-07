---
id: 1684
title: 'Implemeting Data Structures and Algorithms in Python: Problems and solutions'
date: 2017-06-23T20:50:54+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2017/06/1667-revision-v1/
permalink: /2017/06/23/1667-revision-v1/
---
Recently I have started using Python in a lot of places including writing algorithms for MI/data science,  so I thought to try to implement some common programming problems using data structures in Python. As I have mostly implemented in C/C++ and Perl.

Let&#8217;s get started with a very basic problem.

### Anagram algorithm

An algorithm will take two strings and check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters, in other words, rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once

_Some examples of anagram:_  
**&#8220;dormitory&#8221;** is an anagram of **&#8220;dirty room&#8221;**  
**&#8220;a perfectionist&#8221;** is an anagram of **&#8220;I often practice.&#8221;**  
**&#8220;action man&#8221;** is an anagram of **&#8220;cannot aim&#8221;**

Our anagram check algorithm with take two strings and will give a boolean TRUE/FALSE depends on anagram found or not?  
I have used two approaches to solve the problem. First is to sorted function and compare two string after removing white spaces and changing to lower case. This is straightforward.

like

    
    def anagram(str1,str2):
    # First we'll remove white spaces and also convert string to lower case letters
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    # We'll show output in the form of boolean TRUE/FALSE for the sorted match hence return
    return sorted(str1) == sorted(str2)
    

The second approach is to do things manually, this is because to learn more about making logic to check. In this approach, I have used a counting mechanism and Python dictionary to store the count letter. Though one can use inbuilt Python collections idea is to learn a bit about the hash table.

Check [GitHub](https://github.com/ppant/DS-Algos-Python) for the full working code.

I will keep adding more problems/solutions.

Stay tuned!

Ref:  The inspiration of implementing DS in Python is from [this](https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/learn/v4/overview) course on [Udemy](https://www.udemy.com).