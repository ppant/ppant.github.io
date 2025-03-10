---
id: 2007
title: 'Python learning: scrapbook'
date: 2019-04-26T21:17:57+05:30
author: Pradeep Pant
layout: post
guid: /?p=2007
permalink: /2019/04/26/python-learning-scrapbook/
---
While browsing my Evernote I found a scrapbook which I have made while learning Python some years back. Thought to share if this helps someone. I am pasting directly (<g class="gr_ gr\_351 gr-alert gr\_spell gr\_inline\_cards gr\_run\_anim ContextualSpelling ins-del multiReplace" id="351" data-gr-id="351">no</g> editing so there might be some <g class="gr_ gr\_346 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Grammar only-ins replaceWithoutSep" id="346" data-gr-id="346">spell</g> and grammar mistake). 

  * Python 2 division, just use integer part (3/2=1) whereas Python 3 uses real division 3/2 = 1.5
  * Strings in Python are immutable means you can&#8217;t change the in-place value of a char. Once string is created you can&#8217;t change/replace its elements
  *  s= &#8220;Hello World&#8221; s[::-1] this will reverse string s &#8220;dlroW olleH&#8221; double colon is used to tell the range and also how many elements can be skipped
  * if you want to use Python 3 functions in Python 2 then use &#8216;**from \_\_future\_\_ import print_function**&#8216; and similarly other functions 
  * List are mutable but tuples are not mutable (does not support item assignment) aka immutable, fewer methods in tuples then why to use instead of a list? The key is immutability. in a program if you want sequence/Val does not to get changed then tuple is a solution e.g.; storing calendar dates which know will not change during your programs. 
  * Set is a collection of un-ordered unique items it looks like a dictionary (in notation) but only keys which are unique. It can help in removing repeated items means you can use set to cast list.
  * List comprehensive are an excellent way to write clean and efficient code &#8211; they are actually de-constructed for loop flatted out in a list
  * Lambda expressions can be used to shorten function this is really useful when used with map(), reduce() and filter() functions
  * First class functions: Treat functions like any other object, we can pass functions, we can return functions, we can assign functions to a variable
  * Closure: Closure takes advantage of first-class functions and returns inner functions and variables local to them.
  * Decorators: It is a function which takes another function as an argument and returns as a function without changing the source code of the original function. Decorator allows easily to add functionality inside our wrapper without modifying original function.  

**Note:** These are notes for quick reference. If you are serious in learning Python I encourage you to take a book or a tutorial. 

Enjoy learning! More to come &#8230;