---
id: 1532
title: oauth authentication github
date: 2016-03-26T20:44:33+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2016/03/1523-revision-v1/
permalink: /2016/03/26/1523-revision-v1/
---
This is a technique to authenticate using github and fetch any information related to that repository. In this code I have used my [github account.](https://api.github.com/users/ppant/repos)Code is written R programming languages.

<?prettify linenums=true?>

<pre class="prettyprint">## Load required modules
library(httr)
library(httpuv)
require(jsonlite)&lt;/code>

# 1. Find OAuth settings for github:
# http://developer.github.com/v3/oauth/
oauth_endpoints("github")

# 2. To make your own application, register at at
# https://github.com/settings/applications.
## https://github.com/settings/applications/321837
## Use any URL for the homepage URL
# (http://github.com is fine) and http://localhost:1410 as the callback url. You will need httpuv

##
## Replace your key and secret below.
## Secret keys can be get from developer github
myapp &lt;- oauth_app("github",
key = "7cd28c82639b7cf76fcc",
secret = "d1c90e32e12baa81dabec79cd1ea7d8edfd6bf53")

# 3. Get OAuth credentials
github_token &lt;- oauth2.0_token(oauth_endpoints("github"), myapp)
## Authentication will be done automatically

# 4. Use API
gtoken &lt;- config(token = github_token)
req &lt;- GET("https://api.github.com/users/ppant/repos", gtoken)
stop_for_status(req)
##content(req)
output &lt;- content(req)
## Either of the two can be used to fetch the required info, name and date created of repo ProgrammingAssignment3
out&lt;-list(output[[30]]$name, output[[30]]$created_at)

BROWSE("https://api.github.com/users/ppant/repos",authenticate("Access Token","x-oauth-basic","basic"))
# OR:
req &lt;- with_config(gtoken, GET("https://api.github.com/users/ppant/repos"))
stop_for_status(req)
content(req)
</pre>

For complete code please check [github](https://github.com/ppant/)