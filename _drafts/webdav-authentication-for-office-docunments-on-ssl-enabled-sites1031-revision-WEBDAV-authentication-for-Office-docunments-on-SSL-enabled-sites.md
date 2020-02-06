---
id: 1033
title: WEBDAV authentication for Office docunments on SSL enabled sites
date: 2013-03-01T16:54:16+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2013/03/1031-revision/
permalink: /2013/03/01/1031-revision/
---
For SSL enabled sites you will have to add the following lines in /etc/httpd/conf.d/ssl.conf file.  fix will no work if the site is SSL enabled. To make it work for HTTPS we will have to add the setting for denying request in

RewriteEngine On

RewriteCond %{REQUEST_METHOD} ^(OPTIONS|PROPFIND)$ [NC]

RewriteRule ^.*$ – [F,L]

For more info you can go through my old [post](http://pradeeppant.com/2012/05/solving-authentication-problem-while-opening-office-documents-hosted-on-apache-in-ie8ie9-on-windows-7/ "Solving authentication problem while opening Office documents hosted on Apache in IE8/IE9 on Windows 7")