---
id: 1557
title: Accessing Github API with OAuth example using R
date: 2016-06-11T18:42:45+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2016/06/1523-autosave-v1/
permalink: /2016/06/11/1523-autosave-v1/
---
Modern API provided by Google, Twitter, Facebook, Github etc uses [OAuth](http://oauth.net/) for authentication and authorization. In this example, I am using GitHub API. We get a JSON response which can be used to fetch specific information. In this code I have used my [Github account.](https://api.github.com/users/ppant/repos)Code is written R programming languages.

Here are the steps:  
1. Find [OAuth](http://oauth.net/) settings for Github  
2. Create a application in Github  
3. Add/Modify secret keys  
4. Get [OAuth](http://oauth.net/) credentials  
5. Finally use API and parse json data to show response

[code lang=&#8221;R&#8221;]

\## Load required modules  
library(httr)  
library(httpuv)  
require(jsonlite)

\# 1. Find OAuth settings for github:  
\# http://developer.github.com/v3/oauth/  
oauth_endpoints(&#8220;github&#8221;)

\# 2. To make your own application, register at at  
\# https://github.com/settings/applications.  
\## https://github.com/settings/applications/321837  
\## Use any URL for the homepage URL  
\# (http://github.com is fine) and http://localhost:1410 as the callback url. You will need httpuv

\## Add Secret keys  
\## Secret keys can be get from developer github  
myapp <- oauth_app(&#8220;github&#8221;,  
key = &#8220;7cd28c82639b7cf76fcc&#8221;,  
secret = &#8220;d1c90e32e12baa81dabec79cd1ea7d8edfd6bf53&#8221;)

\# 3. Get OAuth credentials  
github\_token <- oauth2.0\_token(oauth_endpoints(&#8220;github&#8221;), myapp)  
\## Authentication will be done automatically

\# 4. Use API  
gtoken <- config(token = github_token)  
req <- GET(&#8220;https://api.github.com/users/ppant/repos&#8221;, gtoken)  
stop\_for\_status(req)  
##content(req)  
output <- content(req)  
\## Either of the two can be used to fetch the required info, name and date created of repo ProgrammingAssignment3  
out<-list(output[[30]]$name, output[[30]]$created_at)

BROWSE(&#8220;https://api.github.com/users/ppant/repos&#8221;,authenticate(&#8220;Access Token&#8221;,&#8221;x-oauth-basic&#8221;,&#8221;basic&#8221;))  
\# OR:  
req <- with_config(gtoken, GET(&#8220;https://api.github.com/users/ppant/repos&#8221;))  
stop\_for\_status(req)  
content(req)  
[/code]  
For updated code please check [github](https://github.com/ppant/)