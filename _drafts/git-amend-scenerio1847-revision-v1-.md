---
id: 1851
date: 2019-03-12T16:37:29+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/03/1847-revision-v1/
permalink: /2019/03/12/1847-revision-v1/
---
Sometimes we need to change the commit message of already committed/pushed files. See below some of the scenarios might arise.. 

**Scenerio 1-> Committed but not pushed**

_$ git commit &#8211;amend_

This will open an editor with the commit message. If you are using vi editor edit the commit message and save using _<g class="gr_ gr\_8 gr-alert gr\_gramm gr\_inline\_cards gr\_disable\_anim_appear Style replaceWithoutSep" id="8" data-gr-id="8">!</g>__<g class="gr_ gr\_8 gr-alert gr\_gramm gr\_inline\_cards gr\_disable\_anim_appear Style replaceWithoutSep" id="8" data-gr-id="8"><g class="gr_ gr\_5 gr-alert gr\_spell gr\_inline\_cards gr\_disable\_anim_appear ContextualSpelling" id="5" data-gr-id="5">wq</g></g>__:_ Check with _$git log_ if the message has been amended corretly.

**Scenerio 2-> Already pushed + most recent commit**

It might be the case that if a user has already pushed the changes to git central repository in that case we need to first amend the most recent local commit and afterward with &#8211;force push the changes to the server. In this process, one thing to keep in mind is that if any other user has already synced with repo in between then they will have to <g class="gr_ gr\_338 gr-alert gr\_spell gr\_inline\_cards gr\_run\_anim ContextualSpelling ins-del multiReplace" id="338" data-gr-id="338">re pull</g>.

_$ git commit &#8211;amend_  
Edit the message in vi and save and exit  
 _$ git push origin <branch_name> &#8211;force_

Not pushed + old commit  
git rebase -i HEAD~X

# X is the number of commits to go back

# Move to the line of your commit, change pick and edit

# then change your commit message

$ git commit &#8211;amend

# Finish the rebase with:

$ git rebase &#8211;continue

Rebase opened your history and let you pick what to change. With edit you tell you want to change the message. Git moves you to a new branch to let you &#8211;amend the message. git rebase &#8211;continue puts you back in your previous branch with the message changes. 

Already pushed + old commit  
Edit your message with the same 3 steps process as above ( rebase -i, commit &#8211;amend, rebase &#8211;continue). Then force push the commit

# _git push origin master &#8211;force_

But! Remeber re-pushing your commit after changing it will very likely to prevent others to sync with the repo, if they already pulled a copy. You should first check with them.

Comment: You can choos reword instead of edit whenrebasing to change the commit directly. Then you can skip the amend and rebase continue.

References:  
<https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4>