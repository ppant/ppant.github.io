---
title: 'Microsoft Edge and IE issue again and workaround'
date: 2020-04-18T5:34:03+05:30
author: Pradeep Pant
layout: post
---
*So here again a post on Microsoft issues though in past I have already written several posts on different issues from Microsoft. Here are few of them:*

 *[Year 2011- Message: Invalid argument: IE 8 Issue](/2011/09/09/message-invalid-argument-ie-8-issue)*

*[Year 2012 - Authentication in Office documents  and Apache in IE8/IE9 on Win 7](/2012/05/18/solving-authentication-problem-while-opening-office-documents-hosted-on-apache-in-ie8ie9-on-windows-7)*

*[Year 2019 -IE11 issue with arrow and includes JavaScript method](/2019/04/15/ie11-issue-with-arrow-operator-and-include-an-alternate-solution)*

*[Year 2019 - Microsoft Visio and infamous Windings font](/2019/04/16/microsoft-visio-and-infamous-windings-font)*

So you see I am reporting and writing about MS issues for almost 10 years 😭 But they don't change!

Anyways, lets talk about current issue:

So, I have a web based application where I open a pop-up window using ````window.open()```` method while clicking on a object/url. If I click on another URL then the same pop-up should get updated with new info and should bring in front. Quite simple operation! This works fine in Chrome, Firefox but when I tested the same in IE11 I saw that content of the pop-up window got updated on clicking on another object/url but the window remained in background. This is very annoying.. So I thought IE is always full of bugs and guys from redmond have made a new browser which they project as in lines with Chrome and FF so I thought that it must have been solved.. but to my surpirse in Edge also this doesn't work means that your pop-up window is updated in background but loose focus. This means that you always have to go and check your pop-up manually. And, this is not specific to my application check window.open [example at W3C School](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open3) 

So what is the solution -- After playing with some configration params of IE 11, I figured it out that if you do the below setting then it gets resolved.

*Internet options => Tabs -> Always open pop-ups in new window*

![Internet options IE 11 pop-up handling.png](\data\images\ie11-internet-options-pop-up-setting.png)


It's almost 5 years our beloved Microsoft has not solved this issue in Edge not even answered [this question](https://answers.microsoft.com/en-us/edge/forum/all/microsoft-edge-how-to-direct-popup-windows-into-a/07f2c5bc-371f-44e6-bd73-6a10d412482c?page=2) .. they took out a feature for handling pop-ups from IE11 with no new solution in edge.. so inconsistent as always! 

As Microsoft has not given any solution for Edge so I have used a workaround which is using  
````JavaScript
window_name.focus()
```` 
method. 

Example code:
````css
	var win_name = 
	window.open('url', 'TestPage', 'width=700,height=750,resizable,scrollbars,top=200,left=200');
	// have to call .focus for IE 11 and Edge to bring refreshed window in front
	win_name.focus();
````

btw I don't use and recommend IE, edge but we have to use for testing our product because some of the IT managers still advice IE to their organization and as a product we have to fix silly Microsoft bugs and sometimes customer thinks our software is buggy 😭

Cheers!

Stay Safe.
