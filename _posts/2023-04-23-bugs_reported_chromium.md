---
title: 'Bug reported to Chromium Development'
date: 2023-04-23
author: Pradeep Pant
layout: post
category: Tech
---
In the last month, I've filed two bugs with the Chromium development team. For readers, Chromium is the backbone engine for popular browsers like Google Chrome and Microsoft Edge.
The first bug I saw was "Disappearing arrowheads when printing an HTML page with SVG created by MS Visio from the second page," a bit specific to Microsoft Visio and Chrome/edge versions. I will not explain in detail here to avoid complexity. One can read here that in my original question asked on [StackOverFlow](https://stackoverflow.com/questions/75472125/disappearing-distorted-connector-arrowheads-when-printing-an-html-page-with-incl) one of the users suggested reporting to the Chromium dev team.

I filed a bug in [Chromium bug tracker](https://bugs.chromium.org/p/chromium/issues/detail?id=1417631) and after much discussion and testing, they acknowledged the bug.

![](/data/images/tech/disappearing_arrowheads_visio.jpg){:height="600px"}
The second bug, "PrintPreview is hanging and is taking a long time to load," I found while testing the first bug fix. I filed the same on [Chromium bug tracker](https://bugs.chromium.org/p/chromium/issues/detail?id=1424368)

![](/data/images/tech/printpreview_chrome.jpg){:height="600px"}
[GitHub](https://github.com/ppant/chromium-bugs-reported) repository contains all the code and screenshots I've used to re-create the issue for developers.

**Some thoughts:** I filed the bug in multiple official channels, like Google Chrome support, Microsoft Edge support, Microsoft Visio support, and the Chromium bug tracker. Google Chrome replied, but Microsoft Edge and Visio were not bothered to acknowledge it. Anyway, even the Chromium development team was initially not very keen on checking, but later, when they saw the severity of the bug, many developers jumped in. Their testing team completely missed that. I also learned how big open-source teams like Chromium work. I am happy because the first bug was blocking one of my customers.
