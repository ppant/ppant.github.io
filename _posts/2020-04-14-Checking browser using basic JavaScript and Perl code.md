---
title: 'Browser detection using basic JavaScript and Perl code'
date: 2020-04-14T5:34:03+05:30
author: Pradeep Pant
layout: post
---
Here is a quick post on how to check the browser name based on ````userAgent ```` 
property which returns the value of the user-agent header sent by the browser to the server based on the value program can do some actions. This is mainly needed for IE and Edge browsers again Microsoft issue 😭

JavaScript:

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

Perl code:

````perl
	sub detect_browser {
		my $user_string = $ENV{'HTTP_USER_AGENT'};
		# NOTE: This is a quick check 
		# For more eloborated checks better to use a module e.g.; HTTP::BrowserDetect	
		if ($user_string =~ /Edge\/\d.|MSIE 10|MSIE 9|rv:11.0/i) { # IE, Edge	
		return 1;
		}
		else { # Chrome, Safari, Firefox	
		return 0;
		}	
	} # end of detect_browser
````

I will write a elaborated post on IE/Edge issues which I have faced recently.

Cheers!


