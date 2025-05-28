---
title: 'Process mining explained'
date: 2022-08-27
author: Pradeep Pant
layout: post
category: Tech
---

In this post we'll dig deep into process mining. You can read my [last](/tech/2022/07/02/business_process_and_process_mining.html) post on data mining and process mining.

Process mining versus Data mining:

* Both starts from data
* Data mining techniques are typically not process-centric
* End-to-end process models and concurrency are essentials for process mining
* Process mining assumes event logs where events have timestamps and refer to prcess instances

Process mining gives you an amazing ability to look under the hood of your business processes and really see
how they work. How they do it? Here comes main types of process mining: 

**1. Discovery:**
process discovery involves using the event logs to create an end-to-end visualization of the process. It follows
every step that every case took as it moved through the cycle, from beginning to end.

**2. Conformance:**
Conformance checking is the part of process mining where you can
really start to see the difference between the way you think your
process ought to be and the way it really is in practice. You gain
the ability to define the preferred path, then see how processes
are deviating from the path

**3. Enhancement:**
The third type of process mining is enhancement. Here, the idea is to extend
or improve an existing process model using information about the actual process
recorded in some event log. Whereas conformance checking measures the alignment
between model and reality, this third type of process mining aims at changing or
extending the a-priori model. One type of enhancement is repair, i.e., modifying the
model to better reflect reality.

Diagram below shows the three main types of process mining: discovery, conformance, and enhancement.
![](/data/images/process_mining_basic_workflow.png){:height="700px"}


Just to conclude in this brief write-up we tried to understand different types of process mining. As we see, event logs plays a crucial role in using these methods and with the advancements in ICT event logs are widely avaliable.

In next post, we'll try to take a use cases to explain these concepts further.

 
Thanks for reading!


*IMG Source: “Process mining” by TU Eindhoven, © by Springer*
