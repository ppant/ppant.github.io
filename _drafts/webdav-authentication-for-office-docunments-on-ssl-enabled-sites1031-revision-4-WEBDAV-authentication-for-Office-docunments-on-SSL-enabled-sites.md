---
id: 1036
title: WEBDAV authentication for Office docunments on SSL enabled sites
date: 2013-03-07T14:27:45+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/03/1031-revision-4/
permalink: /2013/03/07/1031-revision-4/
---
As explained in my[ post related to the Webdav authentication issue using IE for Office documents on Windows 7](http://pradeeppant.com/2012/05/solving-authentication-problem-while-opening-office-documents-hosted-on-apache-in-ie8ie9-on-windows-7/ "Solving authentication problem while opening Office documents hosted on Apache in IE8/IE9 on Windows 7"), I found that the fix will not work for SSL enabled sites. To support HTTPS you will have to add the following lines in **/etc/httpd/conf.d/ssl.conf** file.

<span style="color: #993300;"><strong><VirtualHost></strong></span>

<span style="color: #993300;">RewriteEngine On</span>

<span style="color: #993300;">RewriteCond %{REQUEST_METHOD} ^(OPTIONS|PROPFIND)$ [NC]</span>

<span style="color: #993300;">RewriteRule ^.*$ – [F,L]</span>

<span style="color: #993300;"><em><b></VirtualHost></b></em></span>

<span style="color: #993300;">Restart httpd</span>

_To generate an SSL certificate you can use_ _[OpenSSL library](http://www.openssl.org/) _