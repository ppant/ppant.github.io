---
id: 1035
title: WEBDAV authentication for Office docunments on SSL enabled sites
date: 2013-03-01T17:04:30+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/03/1031-revision-3/
permalink: /2013/03/01/1031-revision-3/
---
As explained in my [post related to Webdav authentication issue using IE for Office documents on Windows 7](http://pradeeppant.com/2012/05/solving-authentication-problem-while-opening-office-documents-hosted-on-apache-in-ie8ie9-on-windows-7/ "Solving authentication problem while opening Office documents hosted on Apache in IE8/IE9 on Windows 7"), I found that the fix given there will not work for SSL enabled sites. So to support HTTPS access you will have to add the following lines in **/etc/httpd/conf.d/ssl.conf** file.

**<VirtualHost>**

**RewriteEngine On**

**RewriteCond %{REQUEST_METHOD} ^(OPTIONS|PROPFIND)$ [NC]**

**<em id="__mceDel"><em id="__mceDel">RewriteRule ^.*$ &#8211; [F,L]</em></em>**

**<em id="__mceDel"><em id="__mceDel"></VirtualHost></em></em>**

Restart httpd

&nbsp;

<em id="__mceDel"> </em>