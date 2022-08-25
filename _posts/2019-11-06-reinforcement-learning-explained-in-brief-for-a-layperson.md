---
id: 2161
title: Reinforcement Learning Explained in brief for a layperson
date: 2019-11-06T20:38:46+05:30
author: Pradeep Pant
layout: post
guid: /?p=2161
permalink: /2019/11/06/reinforcement-learning-explained-in-brief-for-a-layperson/
---
As we know, Machine Learning algorithms can broadly be divided into 3 main categories: 

  * Supervised Learning
  * Unsupervised Learning 
  * Reinforcement Learning (RL)

Let&#8217;s understand in layman term what is reinforcement learning. The main thing RL does is **Learning Control** &#8211; This is neither supervised or unsupervised learning but typically these are problems _where you are learning to control the behavior of a system._

**Example:** 

**How to cycle.**  
Remember the days when you are trying to ride a cycle&#8230;. It&#8217;s _trial and error_. Actually, it is some kind of feedback which is not fully unsupervised. So we can say that this is a type of learning where you are trying to control the system with trial and error and with minimum feedback. RL learns from the close interaction with the environment, close interaction means in this context is that an agent senses that state of the environment and takes the appropriate action. So the agent takes feedback from the close environment and we typically assume that the environment is _stochastic_ means every time you take action you are not getting the same response from the env. 

Apart from the feedback, there is an evaluation measure from the env which tells how well you are performing in a particular task. So each Reinforcement learning algorithm&#8217;s goal is to implement a policy that maximizes some measure of long term performance.

**Just to summarize:**

Reinforcement learning algorithm:

  * Learn from close interaction 
  * Stochastic environment
  * Noisy delayed scalar evaluation
  * Learn policy &#8211; Maximize a measure of long term performance



**Some applications:&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;**

  * Game playing&nbsp;&nbsp;&#8211; Games like backgammon (One of the oldest board game), Atari 
  * Robot navigation
  * Helicopter pilot&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
  * VLSI placement&nbsp; 

This was a brief introduction to RL for an easy understanding of the concept. For further study look for a good book or course. 

**My recommendation:**

  * List of books on RL  
    <https://datascience.stackexchange.com/questions/6694/books-on-reinforcement-learning>
  * There is an excellent course on NPTEL by Prof. Balaram Ravindran, IIT, Madras [https://swayam.gov.in/nd1\_noc19\_cs55/preview](https://swayam.gov.in/nd1_noc19_cs55/preview)

Happy learning!