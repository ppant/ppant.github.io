---
id: 1784
title: 'git quick tip &#8211; branching and merging'
date: 2018-08-07T20:13:17+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1784
permalink: /2018/08/07/git-quick-tip-branching-and-merging/
twitter_share:
  - 'a:2:{s:8:"hashtags";a:1:{i:0;s:16:"git #programming";}s:4:"text";s:37:"git quick tip - branching and merging";}'
---
Sometimes you want to do experiment work or wants to patch the [git](https://git-scm.com/) master branch with some experimental code, in that case, it&#8217;s not the good idea to change the local master branch. Below are steps to do the changes in an experimental branch made with master and merge back to master and the pushback server.

**Scenario:**

<li style="list-style-type: none;">
  <ul>
    <li>
      Create a new branch locally with the existing branch
    </li>
    <li>
      Make changes and commit these changes
    </li>
    <li>
      Merge them with the local branch from where we have made the branch
    </li>
    <li>
      push to the git server.
    </li>
  </ul>
</li>

**Example:  
** # Make a master_dev from master branch  
`$ git checkout -b master_dev master<br />
`  
\# Do changes in master_dev branch  
`$ git commit -am "Commit message"`

\# Checkout master branch  
`$ git checkout master`

\# Merge the changes of master_dev to master  
`$ git merge --no-ff master_dev`

\# Push the changes of master to origin master  
`$ git push origin master`

\# Optionally one can push the master_dev branch to remote  
\# DO ONLY IF YOU WANT MASTER_DEV BRANCH ALSO ON SERVER  
`$ git push origin master_dev`

&nbsp;

Happy programming!

 ``