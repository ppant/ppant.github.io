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

<pre class="wp-block-preformatted"><em>$ git commit --amend</em></pre>

This will open an editor with the commit message. If you are using vi editor edit the commit message and save using _<g class="gr_ gr\_8 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Style replaceWithoutSep" id="8" data-gr-id="8">!<g class="gr_ gr\_5 gr-alert gr\_spell gr\_inline\_cards gr\_disable\_anim_appear ContextualSpelling" id="5" data-gr-id="5">wq</g></g>:_ Check with _$git log_ if the message has been amended correctly.

**Scenerio 2-> Already pushed + most recent commit**

It might be the case that if a user has already pushed the changes to git central repository, in this type of scenario we need to first amend the most recent local commit and afterward apply _&#8211;force push_ which will forcefully push the changes to the server. In this process, one thing to keep in mind is that if in between any other user who has already synced local copy with the central repository needs to re-pull.

<pre class="wp-block-preformatted"><em>$ git commit --amend</em><br /> Edit the message in vi and save and exit<br /><em> $ git push origin &lt;branch_name&gt; --force</em></pre>

  
**Scenerio 3-> Not pushed + old commit** 

<pre class="wp-block-preformatted">$ git rebase -&lt;g class="gr_ gr_5 gr-alert gr_tiny gr_spell gr_inline_cards gr_run_anim ContextualSpelling multiReplace" id="5" data-gr-id="5">i&lt;/g> HEAD~X</pre>

where X is the number of commits to <g class="gr_ gr\_3 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Grammar multiReplace" id="3" data-gr-id="3">go</g> back then move to the line of your commit, change pick and edit then change your commit message

<pre class="wp-block-preformatted"><em>$ git commit --amend </em></pre>

Finish the rebase with:

<pre class="wp-block-preformatted"><em>$ git rebase --continue</em></pre>

Rebase opened your history and let you pick what to change. With edit, you tell that you <g class="gr_ gr\_9 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Grammar only-ins replaceWithoutSep" id="9" data-gr-id="9">want</g> to change the message. Git moves you to a new branch to let you &#8211;amend the message. _git rebase &#8212;_ continue puts you back in your previous branch with the message changes. 

alternatively, you can <g class="gr_ gr\_4 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Grammar only-ins replaceWithoutSep" id="4" data-gr-id="4">choose</g> r_eword_ instead of edit when rebasing to change the commit directly. Then you can skip the amend and rebase continue. You may check [this](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) link from git book for more on this.

**<g class="gr_ gr\_6 gr-alert gr\_spell gr\_inline\_cards gr\_run\_anim ContextualSpelling ins-del multiReplace" id="6" data-gr-id="6">Scenerio</g> 4-> Already pushed <g class="gr_ gr\_12 gr-alert gr\_tiny gr\_gramm gr\_inline\_cards gr\_run_anim Grammar only-ins doubleReplace replaceWithoutSep" id="12" data-gr-id="12">+</g> old commit**  
Edit your message with the same 3 steps process as <g class="gr_ gr\_25 gr-alert gr\_spell gr\_inline\_cards gr\_run\_anim ContextualSpelling ins-del multiReplace" id="25" data-gr-id="25">menined</g> in scenerios 2 ( r_ebase &#8211;_<g class="gr_ gr\_7 gr-alert gr\_tiny gr\_spell gr\_inline\_cards gr\_run_anim ContextualSpelling multiReplace" id="7" data-gr-id="7">_i_</g>_, commit &#8211;amend, rebase &#8211;continue)_. Then force push the commit

<pre class="wp-block-preformatted">$<em>git push </em>&lt;branch_name&gt;<em> </em>m<em>aster --force</em></pre>

But! please remember re-pushing your commit after changing it will very likely to prevent others to sync with the <g class="gr_ gr\_7 gr-alert gr\_gramm gr\_inline\_cards gr\_run\_anim Punctuation only-del replaceWithoutSep" id="7" data-gr-id="7">repo,</g> if they already pulled a copy. You should first check with them.

<p style="text-align:left" class="has-text-color has-small-font-size has-vivid-cyan-blue-color">
  <br /><strong>References: <br /></strong><a href="https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4">https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4</a>
</p>

<p class="has-text-color has-small-font-size has-vivid-cyan-blue-color">
  <a href="https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History">https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History</a>
</p>



<p class="has-text-color has-small-font-size has-pale-cyan-blue-color">
  <br />
</p>