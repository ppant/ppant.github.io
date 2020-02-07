---
id: 2206
title: 'decoupled content management system: Some thoughts'
date: 2019-11-29T13:08:16+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/11/29/2205-revision-v1/
permalink: /2019/11/29/2205-revision-v1/
---
For quite some time, I am interested in building a static blog that uses markdown as the main data source and built on the top of javascript and newer technologies. My present website is a WordPress blog and being a techie I wanted to control through code. Then I stumbled to gatsby a static site generator that uses ReactJS and APIs to deliver the contents. 

Soon in my work as well a discussion started to do some revamp of UI which is currently base on traditional HTML/CSS and JavaScript.

Drupal

WordPress





New technologies to be usedReactJSDecoupled content management systems (Check how WordPress and drupal are trying to switch from coupled -> de-coupled way of working)In this case content resides separately and one can use API to fetch the data on-demand. so as a software dev mostly APIs will be developed. GraphQL type of querying the data, which is different than REST which takes the get request and fetch full object but with GraphQL can fetch an attribute of the data  
We have to explore and see if the API way of working will be beneficial for us?  
What will be the backend technologies?   
How this will affect the user interface like Tiny WYSIWYG etc  
A good JavaScript framework to be used  
I already studying now a day a framework gatsby (gas-bee) which uses API based model using reactJS and GraphQL