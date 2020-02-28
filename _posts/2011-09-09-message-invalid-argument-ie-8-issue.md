---
id: 634
title: 'Message: Invalid argument: IE 8 Issue'
date: 2011-09-09T21:00:57+05:30
author: Pradeep Pant
layout: post
guid: /?p=634
permalink: /2011/09/09/message-invalid-argument-ie-8-issue/
jabber_published:
  - "1315582349"
email_notification:
  - "1315582352"
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1326262078";}'
dsq_thread_id:
  - "781140610"
---
In my Perl based server application, I want to execute a script in a new pop up window. I was using a syntax like:  
[code lang=&#8221;js&#8221;]  
var my\_window = window.open(&#8216;open\_window.pl, &#8216;my window&#8217;, &#8216;width=800,height=600,resizable,scrollbars&#8217;);  
[/code]  
When I run the program in FF and Chrome it all works fine. I can open my pop-up window with above parameters and can see my desired result but the issue starts when I do the same test with IE 8. In spite of pop-up blocker off, the pop-up window was not launching, it was giving me a error message like:  
[code lang=&#8221;js&#8221;]  
Message: Invalid argument.  
Line: 100 Char: 5  
Code: 0  
[/code]  
After debugging I found a solution which is some way very ridiculous. Issue was because of the reason that Microsoft does support the name property in window.open() with spaces [<http://msdn.microsoft.com/en-us/library/ms536651%28v=vs.85%29.aspx>] this means that if I make my window.open like [See **<span style="color:#00ff00;">GREEN</span>** string  
[code lang=&#8221;js&#8221;]  
var my\_window = window.open(&#8216;open\_window.pl, <strong><span style="color:#00ff00;">&#8217;my_window&#8217;, &#8216;width=800,height=600,resizable,scrollbars&#8217;);  
[/code]  
then it should works.

After doing this change it works with me for all the browsers.

I don&#8217;t know why IE always through such type of errors,  even if you launch the in-built Developer tool from IE interface then also you will get the same error message  &#8220;Invalid arguments&#8221; no further clue/pointer to solve the issue. MS really has to improve the error handling messages to user.

So guys, be careful while developing pop-up window for all browsers specially for IE.

Thanks