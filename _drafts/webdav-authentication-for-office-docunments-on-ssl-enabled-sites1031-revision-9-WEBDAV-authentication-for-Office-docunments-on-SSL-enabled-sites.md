---
id: 1103
title: WEBDAV authentication for Office docunments on SSL enabled sites
date: 2013-07-19T13:13:05+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/07/1031-revision-9/
permalink: /2013/07/19/1031-revision-9/
---
As explained in my[ post related to the Webdav authentication issue using IE for Office documents on Windows 7](http://pradeeppant.com/2012/05/solving-authentication-problem-while-opening-office-documents-hosted-on-apache-in-ie8ie9-on-windows-7/ "Solving authentication problem while opening Office documents hosted on Apache in IE8/IE9 on Windows 7"), I found that the fix will not work for SSL enabled sites. To support HTTPS you will have to add the following lines in **/etc/httpd/conf.d/ssl.conf** file.

[code lang=&#8221;html&#8221;]  
<VirtualHost>  
RewriteEngine On  
RewriteCond %{REQUEST_METHOD} ^(OPTIONS|PROPFIND)$ [NC]  
RewriteRule ^.*$ – [F,L]  
</VirtualHost>  
[/code]  
<span style="color: #993300;">Restart httpd</span>

To generate an SSL certificate you can use [OpenSSL library](http://www.openssl.org/)