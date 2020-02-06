---
id: 1109
title: 'Message: Invalid argument: IE 8 Issue'
date: 2011-09-09T21:00:57+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2011/09/634-revision/
permalink: /2011/09/09/634-revision/
---
In my Perl based server application, I want to execute a script in a new pop up window. I was using a syntax like:

<pre><span style="color:#800000;">var my_window = </span>
<span style="color:#800000;"> window.open('open_window.pl, 'my window', 'width=800,height=600,resizable,scrollbars');</span></pre>

When I run the program in FF and Chrome it all works fine. I can open my pop-up window with above parameters and can see my desired result but the issue starts when I do the same test with IE 8. In spite of pop-up blocker off, the pop-up window was not launching, it was giving me a error message like:

<span style="color:#800000;">Message: Invalid argument.</span>  
<span style="color:#800000;">Line: 100 Char: 5</span>  
<span style="color:#800000;">Code: 0</span>

After debugging I found a solution which is some way very ridiculous. Issue was because of the reason that Microsoft does support the name property in window.open() with spaces [<http://msdn.microsoft.com/en-us/library/ms536651%28v=vs.85%29.aspx>] this means that if I make my window.open like [See **<span style="color:#00ff00;">GREEN</span>** string]

<pre><span style="color:#800000;">var my_window = </span>
<span style="color:#800000;"> window.open('open_window.pl, <strong><span style="color:#00ff00;">'my_window'</span></strong>, 'width=800,height=600,resizable,scrollbars');</span></pre>

then it should works.

After doing this change it works with me for all the browsers.

I don&#8217;t know why IE always through such type of errors,  even if you launch the in-built Developer tool from IE interface then also you will get the same error message  &#8220;Invalid arguments&#8221; no further clue/pointer to solve the issue. MS really has to improve the error handling messages to user.

So guys, be careful while developing pop-up window for all browsers specially for IE.

Thanks