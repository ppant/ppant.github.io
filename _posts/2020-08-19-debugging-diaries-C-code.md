---
title: 'Debugging diaries - C/C++ code'
date: 2020-08-19
author: Pradeep Pant
layout: post
---
***Sometimes an only a single line of code change can do the magic!!***
This is one of the most difficult customer issue I have faced and was part of team who has finally solved it. 
The guy from US was not willing to transfer the code, it was huge task. It was difficult to get the info from him but as high level team was invloved in this issue. 

This was related to DocuShare (a document management system) and freeflow projects a softawre which manages the Xerox Production printers and RMS (Repository Management System)
The Repository Management Service is the service that allows FreeFlow applications to connect to supported document repositories.
Freeflow application like MakeReady, Precess Manager etc -> RMS adapter -> RMS Server > Docushare connector -> Docushare


Repository 
A generic term used in the FFAT user interface usually means DMS.
Repository service 
Another name for an RMS server. (In fact, the RMS server's class name is RepositoryService.) 
RMS 
"Repository Management System." The name we gave to the suite of client and server software that, when used together, enabled FreeFlow apps to save to DocuShare and other neat places. 
RMS client 
A library that FreeFlow apps link to which makes it easier for them to talk to an RMS server. There is one RMS client for each language FreeFlow applications are written in (C++, C#, and Java so far.) 
RMS client consumers 
An informal name for the FreeFlow applications that use the RMS client libraries.
DMS (Repository) Connector: Provides interfaces to access each repository for RMS Server. 


RMS server 
A web service (currently hosted on IIS) that accepts SOAP requests from RMS client and sends SOAP responses back to them. It uses the connector libraries directly and acts as a middle-man that allows RMS client consumers to interact with DMS systems. You can access the RMS Server as http://hostname:8090/RepositoryService.asmx.
URI 
"Uniform resource identifier", the technical name for strings like http://www.yahoo.com. 
Web service 
The simplest definition is a website that can accept incoming XML data and return an XML response. 
The RMS server is a web service; Xerox DocuShare and Microsoft SharePoint both function as one. All web services are really specially formatted web pages, and like web pages they must be referred to with a URI, not just an IP address. The FFAT and some other FreeFlow applications sometimes quietly do conversion of hostnames and IP addresses to URIs on the user's behalf. 

Uche Akotaobi
https://www.linkedin.com/in/uche-akotaobi-827b116/

 Repository Management Server: A plugin-based web service that served as an abstract layer on top of document repositories such as Documentum, Xerox DocuShare, and Microsoft SharePoint, exposing a common, WSDL-based API to interact with them. Various language-specific clients could then talk to the RMS server, allowing a wide range of programs to transparently read from and write to documents stored in those repositories.

Happy coding and debugging.

Enjoy.
