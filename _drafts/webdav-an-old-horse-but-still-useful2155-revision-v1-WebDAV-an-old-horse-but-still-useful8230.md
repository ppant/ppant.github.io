---
id: 2160
title: 'WebDAV: an old horse but still useful&#8230;'
date: 2019-11-06T13:59:04+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/11/2155-revision-v1/
permalink: /2019/11/06/2155-revision-v1/
---
My first encounter with WebDav protocol back in 2004-05 when I was writing the web part for SharePoint. This is an old protocol of the &#8217;90s but still very useful in certain scenarios. Let first understand how this protocol helps in online editing of a document, creating files and folders, etc 

WebDAV (Web Distributed Authoring and Versioning) is one mechanism. A web server that supports WebDAV simultaneously works like a fileserver. That’s a powerful capability. 

<p class="has-text-color has-luminous-vivid-orange-color">
  Servers which have implemented WebDav
</p>

  * Apache HTTP Server
  * Microsoft IIS
  * Box.com 
  * WordPress
  * Drupal
  * Microsoft Sharepoint
  * Subversion
  * Git
  * Microsoft Office 
  * Apple iWork
  * Adobe Photoshop etc.

WebDAV (<a rel="noreferrer noopener" href="https://tools.ietf.org/html/rfc4918" target="_blank">RFC 4918</a>) is an extension to&nbsp;<a rel="noreferrer noopener" href="https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol" target="_blank">HTTP</a>, the protocol that web-browsers and web servers use to communicate with each other. The WebDAV protocol enables a webserver to behave like a fileserver too, supporting collaborative authoring of web content. 



A range of applications have the ability to work with files accessed via WebDAV. The application’s file selection dialog supports entering not just a local filename, but a WebDAV URL, with the username and password needed for the WebDAV server. These applications include Microsoft Office (Word, Excel, etc); Apple iWork (Pages, Numbers, Keynote); Adobe Photoshop and Dreamweaver; and others. 

WebDAV is a long-standing protocol that enables a webserver to act as a fileserver and support collaborative authoring of content on the web. In many of its use cases WebDAV is being supplanted by more modern mechanisms. But it’s still a reliable workhorse when the right servers and clients are matched, so it’s still encountered in many different applications. 

References:  
WebDav RFC: <https://tools.ietf.org/html/rfc4918>

<https://www.comparitech.com/net-admin/webdav/>