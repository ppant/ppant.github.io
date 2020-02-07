---
id: 2035
title: git push up to a certain commit
date: 2019-05-06T17:52:45+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/05/2030-revision-v1/
permalink: /2019/05/06/2030-revision-v1/
---
This is a quick share on git.  
**Scenario:** I want to push my local changes to git but am having a few commits which I don&#8217;t want to push now. In other words, I just want to push changes till a certain commit.  
**Solution:**  
`$git push  <remotename><commit SHA>:<remote_branch_name>`

To elaborate  
First, fetch the SHA of the commit you want to push  
`$ git log`

Copy the SHA and use the command below (Make sure that you replace the SHA of your commit with the given in the example).

`$git push origin 7120f221660dad58d41b9ac729a22f08572b109:master`

You are good to go. Your local commit of the given SHA is now pushed to server master keeping your local commits local only.  
  
Please share in comments if you any other alternate way.  
  
Thanks