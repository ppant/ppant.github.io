---
id: 1847
title: git amend scenerios
date: 2019-03-12T21:16:50+05:30
author: Pradeep Pant
layout: post
guid: /?p=1847
permalink: /2019/03/12/git-amend-scenerio/
---
Sometimes we need to change the commit message of already committed/committed-pushed files. See below some of the scenarios might arise<g class="gr_ gr\_4 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Punctuation multiReplace" id="4" data-gr-id="4">..</g> 

**Scenerio 1-> Committed but not pushed**

````bash 
$ git commit --amend 
````

This will open an editor with the commit message. If you are using vi editor edit the commit message and save using ````!wq:```` 
You can check with ````$git log```` 
if the commit message is amended correctly.

**Scenerio 2-> Already pushed + most recent commit**

It might be the case that if a user has already pushed the changes to git central repository, in this type of scenario we need to first amend the most recent local commit and afterward apply ````-force push```` 
which will forcefully push the changes to the server. In this process, one thing to keep in mind is that if in between any other user who has already synced local copy with the central repository needs to re-pull.

````bash
$ git commit --amend
````
Edit the message in vi and save and exit

````bash 
$ git push origin <branch_name> --force 
````

  
**Scenerio 3-> Not pushed + old commit** 

````bash 
$ git rebase -i HEAD~X
````

where X is the number of commits to go back then move to the line of your commit, change pick and edit then change your commit message.
e.g.; Go back to previous 2 commits

````bash 
$ git rebase -i HEAD~2
````
**Note:** *It's always good idea to use* 
````bash 
$ git log 
````
*to check the commit history to avoid the mistake in rebase.*

Use amend 

````bash 
$ git commit --amend 
````
and finish the rebase with:

````bash 
$ git rebase --continue
````

Rebase opened your history and let you pick what to change. With edit, you can change the message. Git moves you to a new branch to let you amend the message. 
````bash 
$ git rebase --continue
```` 
puts you back in your previous branch with the changed message. 

alternatively, you can choose 
````bash 
reword
```` 
instead of edit when rebasing to change the commit directly. Then you can skip the amend and rebase continue. You may check [this](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) link from git book for more on this.

**Scenerio 4-> Already Pushed + Old Commit**  
Edit your message with the same 3 steps process as we saw in scenerios 2 
````bash 
rebase -i, commit --amend, rebase --continue
````
Then force push the commit.

````bash 
$git push <branch_name> master --force
````

Please so remember re-pushing your commit after changing, it will be very likely to prevent others to sync with the repo if they already pulled a copy. You should first check with them.


**References:** 

[https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4](https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4)

[git-scm](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)




<p class="has-text-color has-small-font-size has-pale-cyan-blue-color">
  <br />
</p>
