---
id: 1523
title: Accessing Github API with OAuth example using R
date: 2016-03-27T08:53:20+05:30
author: Pradeep Pant
layout: post
guid: /?p=1523
permalink: /2016/03/27/accessing-github-api-with-oauth-example-using-r/
---
Modern API provided by Google, Twitter, Facebook, Github etc uses [OAuth](http://oauth.net/) for authentication and authorization. In this example, I am using GitHub API. We get a JSON response which can be used to fetch specific information. In this code I have used my [Github account.](https://api.github.com/users/ppant/repos)Code is written R programming languages.

Here are the steps:  
1. Find [OAuth](http://oauth.net/) settings for Github  
2. Create a application in Github  
3. Add/Modify secret keys  
4. Get [OAuth](http://oauth.net/) credentials  
5. Finally use API and parse json data to show response

````R

## Load required modules  
library(httr)  
library(httpuv)  
require(jsonlite)

# 1. Find OAuth settings for github:  
# http://developer.github.com/v3/oauth/  
oauth_endpoints("github")

# 2. To make your own application, register at at  
# https://github.com/settings/applications.  
## https://github.com/settings/applications/321837  
## Use any URL for the homepage URL  
# (http://github.com is fine) and http://localhost:1410 as the callback url. You will need httpuv

## Add Secret keys  
## Secret keys can be get from developer github  
myapp <- oauth_app("github",  
key = "cd28c82639b7cf76fcc",  
secret = "d1c90e32e12baa81dabec79cd1ea7d8edfd6bf53")

# 3. Get OAuth credentials  
github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)  
## Authentication will be done automatically

# 4. Use API  
gtoken <- config(token = github_token)  
req <- GET("https://api.github.com/users/ppant/repos", gtoken)  
stop_for_status(req)  
##content(req)  
output <- content(req)  
## Either of the two can be used to fetch the required info, name and date created of repo ProgrammingAssignment3  
out<-list(output[[30]]$name, output[[30]]$created_at)

BROWSE("https://api.github.com/users/ppant/repos&",authenticate("Access Token","x-oauth-basic","basic"))  
# OR:  
req <- with_config(gtoken, GET("https://api.github.com/users/ppant/repos"))  
stop_for_status(req)  
content(req)  
````  
For updated code please check [github](https://github.com/ppant/)