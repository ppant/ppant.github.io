---
id: 2189
title: 'CNN: More edge detection and horizontal edge detection with example'
date: 2020-01-17T13:47:16+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2189
permalink: /?p=2189
---
In my previous [post](http://pradeeppant.com/2019/11/21/cnn-understanding-edge-detection-with-an-example/), we learned the basics of vertical edge detection with an example. In this post, we&#8217;ll dig a bit deeper into edge detection and in the latter part of the post, we&#8217;ll explore horizontal edge detection. Let&#8217;s get started:

The first thing we&#8217;ll learn is the difference between positive and negative edges, that is, the difference between _light to dark_ versus _dark to light_ edge transitions and we&#8217;ll also see other types of edge detectors, as well as how to have an algorithm learn, rather than have us hand-code an edge detector as we&#8217;ve been doing so far.