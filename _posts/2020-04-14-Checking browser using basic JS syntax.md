---
title: 'Browser detection using basic JavaScript syntax'
date: 2020-04-14T5:34:03+05:30
author: Pradeep Pant
layout: post
---
Here is a quick post on how to check the browser name based on ````userAgent ```` 
property which returns the value of the user-agent header sent by the browser to the server based on the value program can do some actions. This is mainly needed for IE and Edge browsers again Microsoft issue 😭

````js

	if ((/MSIE 10/i.test(navigator.userAgent)) ||
		(/MSIE 9/i.test(navigator.userAgent)) || 
		(/rv:11.0/i.test(navigator.userAgent)) ||
		(/Edge\/\d./i.test(navigator.userAgent))) { // Microsoft browsers     
	alert('IE 9, 10, 11, Edge');	
		// do some action 
	}	
	else { // Chrome, Safari, Firefox
		alert("Chrome, Safari, Firefox");
	}
````

I will write a elaoborated post on IE/Edge issues which I have faced recently.

Cheers!


