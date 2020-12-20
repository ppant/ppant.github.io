---
title: 'Firefox SameSite Set cookie reject issue apache solution'
date: 2020-12-20
author: Pradeep Pant
layout: post
---
A couple of days back while testing something I found the below warning in my Firefox console (Press F12 to get access to console).

![](/data/images/SameSite_cookie_warning_ff.png)

as per the warning cookie from my application will be **rejected** soon, though they have not mentioned any timeline by when the cookie with current attributes will be supported?

through there is documentation which explains a bit about options one can use for ````Set-Cookie```` to solve but that depends how you are setting your cookie..

[https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)

**Coming to solution part**, if you are using apache then you can make global change in ````httpd.conf```` file, one can also do from other places like using ````HTACESS```` file or depends on the application cookie setting mechanism.

To solve the issue from apache. Below are the steps: 

**ENV:**

````
CentOS 6.x,7.x 
Apache 2.2.x
````
* Open ````/etc/httpd/conf/httpd.conf```` file Check if ````mod_headers.so```` is loaded if not do so by below command (in default apache installation it should be there already)
  ````LoadModule headers_module modules/mod_headers.so````

* Add Header fix. I have added ````Http```` with secure settings in
  ````Set_Cookie````

    
    ````<ifmodule mod_headers.c>````
    
    ````Header always edit Set-Cookie (.*) "$1;HttpOnly;Secure;SameSite=Strict"````
    
    ````</ifmodule>````
    

* Finally, restart the webserver

    ````
    service  httpd restart
    ````


Done!  

**FF Warning should go and hopefully cookies should be allowed.**


All the best!
