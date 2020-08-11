---
title: 'Debugging diaries - Perl code'
date: 2020-08-11
author: Pradeep Pant
layout: post
---
***Sometimes only line of code change can do the magic!***

So it happened couple of weeks back when I was working on a new feature which involves a lot of caching of different authentic user's full names with respective unique user ids of a large scale web based distributed system. As we know caching is very useful way to optimize the code to avoid the repetive information but at the same time it can give us a very different and weird results. For me whenever I implement heavy caching ground rule is to add as many as test cases to do the better testing. So while during such a testing I found a unusual behavior though it was not a common case but still there was something which was not correct so first thing came in mind is that maybe this is because of new cache dev.  Next step is to stash the current branch code and do a git checkout of the master branch to know that what is the cause of issue. New Imple or old a bug? *as a side note I think with git we can make branches in no time so developer should make as many as experiential branches they need and always test the code on master in case of break and before trying to give solution.* 

So back to the issue, master branch also had the same issue so next step is to look for more older releases and look for a fix. In my case it didn't come up with any of the realses instead it was never implemented or can say that no one saw this case as I mentioned a rare case and mostly solved by a workaround which user generally do (a simple logout). So a bit fast forward, this particular issue took me almost 3 days to do the deep debugging of the multiple code files, env which involves multiple third party open source libs and OS layers (I use Cent OS) and behold it took me just 3 min to resolve this with just ONE line code addition. 

So what I want to communicate that this is the beauty of software dev, your code has to be 100% correct and once you analyse the problem correctly and deeply, you will amazed to see that solution was right here .. This is not the first time happened .. bottom line is that one needs to be patient enough to analyse properly to take all the surroundings in consideration and debug. In critical real time software this is much more needed. 
btw the ONE line of Perl code was 

````$user->load()````

*Reload the USER object, beauty is to find the place where this reloading to be done without breaking the other flows and by taking minimal memory and only triggered in case of this rare case encounters.*

Happy coding and debugging.

Enjoy.

