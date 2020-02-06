---
id: 2190
title: 'CNN: More edge detection and horizontal edge detection with example'
date: 2019-11-27T20:08:11+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/11/27/2189-revision-v1/
permalink: /2019/11/27/2189-revision-v1/
---
In my previous [post](http://pradeeppant.com/2019/11/21/cnn-understanding-edge-detection-with-an-example/), we learned the basics of vertical edge detection with an example. In this post, we&#8217;ll dig a bit deeper into edge detection and in the latter part of the post, we&#8217;ll explore horizontal edge detection. Let&#8217;s get started:

The first thing we&#8217;ll learn is the difference between positive and negative edges, that is, the  
difference between _light to dark_ versus _dark to light_ edge transitions and we&#8217;ll also see other types of edge detectors, as well as how to have an algorithm learn, rather than have us hand-code an edge detector as we&#8217;ve been doing so far.