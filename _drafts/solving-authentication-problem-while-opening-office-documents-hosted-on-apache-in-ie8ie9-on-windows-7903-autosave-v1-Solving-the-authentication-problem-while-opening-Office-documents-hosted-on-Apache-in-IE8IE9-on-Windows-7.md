---
id: 1096
title: Solving the authentication problem while opening Office documents hosted on Apache in IE8/IE9 on Windows 7
date: 2013-07-19T12:17:50+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/903-autosave/
permalink: /2013/07/19/903-autosave-v1/
---
We were facing a problem in IE 8/9 on Windows 7 while accessing  Office 2007/ Office 2010 documents hosted on apache/Cent OS 4.6. After some analysis I found the reason and finally ended in a fix. See below my findings and solution. Hope this helps:

The main issue is with the Microsoft&#8217;s way of implementing Webdav protocol for accessing web content through Microsoft Web Client. When we click on a Office document then web client  sends HTTP /1.1 OPTIONS Request header to server to check the WebDav communication (My server doesn&#8217;t have WebDav). In response Apache return 200 OK Response header to Web Client which results in prompting the authentication screen by Windows 7.  Well you have option in IE to pass the authentication login automatically but that would be security breach as you will be exposing your machine authentication to internet so I would not prefer that. Best way is to configure Apache to reject these request. This is how i have solved. These changes needs to be done in <span style="color: #993300;">httpd.conf</span> file in <span style="color: #993300;">/etc/httpd/conf</span> folder (Cent OS 4.6)

<span style="color: #0000ff;"># One way to doing it &#8211; Deny access based on request method</span>

[code lang=&#8221;html&#8221;]  
RewriteEngine On  
RewriteCond %{REQUEST_METHOD} ^(OPTIONS|PROPFIND)$ [NC]  
RewriteRule ^.*$ &#8211; [F,L]  
[/code]  
<span style="color: #0000ff;"># Another way to implementing &#8211; Deny acess based on user agent (Vista and Windows 7 used same user agent with different version so this Regx shall work for both</span>

RewriteEngine On</span>  
<span style="color: #000000;">RewriteCond %{HTTP_USER_AGENT} ^Microsoft-WebDAV-MiniRedir</span>

<span style="color: #000000;">RewriteRule ^.*$ &#8211; [F,L]</span>

<span style="color: #0000ff;">Explanation on Flags:</span>

1. [F] flag causes the server to return a 403 Forbidden status code to the client.

2. Use of the [NC] flag causes the RewriteRule to be matched in a case-insensitive manner. That is, it doesn&#8217;t care whether letters appear as upper-case or lower-case in the matched URI.

3. The [L] flag causes mod_rewrite to stop processing the rule set. In most contexts, this means that if the rule matches, no further rules will be processed. This corresponds to the last command in Perl.

<span style="color: #0000ff;"> Some References:</span>

[Microsoft knowledge article on authentication requests from office documents ](http://support.microsoft.com/kb/2019105)

[Apache mod_rewrite rule documentaion](http://httpd.apache.org/docs/current/mod/mod_rewrite.html)

[fiddler tool for debugging HTTP requests](http://www.fiddler2.com/fiddler2/)