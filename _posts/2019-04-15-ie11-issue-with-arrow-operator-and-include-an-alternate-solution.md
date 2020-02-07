---
id: 1957
title: 'IE11 issue with &#8220;arrow&#8221;  and &#8220;includes&#8221; Javascript method and an alternate solution'
date: 2019-04-15T21:46:03+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1957
permalink: /2019/04/15/ie11-issue-with-arrow-operator-and-include-an-alternate-solution/
twitter_share:
  - 'a:2:{s:8:"hashtags";a:1:{i:0;s:9:"IE11Issue";}s:4:"text";s:118:"I have made small demo of #IE11 issue with arrow and include #JavaScript methods and a alternate solution #programming";}'
---
Again one more Microsoft problem <span style="font-size: 1.375rem;">😢 </span>😢

Yesterday, I  suddenly observed that one part of my newly developed feature was not working in IE11. This is a simple feature which contains two select boxes, user can select the one or multiple items from the first select box and copy to another select box. I have added a kind of logic there which checks before copying if the item(s) to be copied are already in list 2, if true, alert the user and skip copying duplicates. While developing I checked this feature in chrome, Edge and Firefox and all work perfectly!  I couldn&#8217;t check in IE11 and that was my mistake as IE is infamous for such issues. While debugging I saw that IE11 was crashing on the places where I have used the functions  => and .include. Actually, the arrow function is not supported in IE 11. You can refer to this compatibility table: <a href="https://kangax.github.io/compat-table/es6/" rel="nofollow">https://kangax.github.io/compat-table/es6/</a> to get an overview of what is supported where and to what extent in a detailed fashion. You may read more on arrow functions at below link: 

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions>

Check below a small demo which shows the problem and an alternate which solves the IE11 issue.

Demo:

\***\***\***\***\***\***\***\***\***\***\****

[JSFiddle (Fails in IE11)](https://jsfiddle.net/ppant/e5pufg39/6/)

[JSFiddle (Works in IE11)](https://jsfiddle.net/ppant/e5pufg39/5/)

\***\***\***\***\***\***\***\***\***\***\****

Github:

[code (Fails in IE11) ](https://github.com/ppant/jshacks/blob/master/list_copy_items.html)

[code (Works in IE11) ](https://github.com/ppant/jshacks/blob/master/list_copy_items_with_IE11.html)

 

\***\***\***\***\***\***\***\***\***\***\****

Happy coding!