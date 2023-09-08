---
title: 'Understanding decision tree for Process Mining'
date: 2023-08-23
author: Pradeep Pant
layout: post
categories: Tech
---

A decision tree is a data mining technique that works best with labeled data. They play a crucial role in process discovery. In this article I will try to give you some ideas of how a decision tree can be learned, what are the most important parameters in a decision tree and its use in process mining.

If you are new to Process mining I will suggest you to go through my [introductory articles](/2022/07/02/business_process_and_process_mining.html) on Process mining. In nutshell,, Process mining is a area of where we use data science/data mining techniques to improve the existing business processes. 

Back to deseion tree, 

<figcaption align = "center"><b>Calculate entropy formula</b></figcaption>
![](/data/images/tech/calculate_entropy_formula.png){:height="200px"}

<span style="color:blue"><small>IMG Source: [Process mining, Data Science in action](https://link.springer.com/book/10.1007/978-3-662-49851-4)</small></span>



Before Process mining this is introduction to data mining techniques like decision tree which works on labelled data
Response variable and predictor variable.
Classification based on decision tree -- how to read decision tree 
Decision tree is used to understand the data, predicting the data
Decision tree can be learned from data

How to learn a decision tree?
Reduce the nodes to reduce the variability, in other words split nodes where we are uncertain about to smaller sets/classes that are more homogenous.  

High entropy - very uncertain
Target is to go from a bigger class - high entropy/high degree on uncertainty  to smaller class where we are more certain, in this way incrementally we can build the decision tree. 

To understand decision one should have good understanding of uncertainty or entropy, which is the degree of uncertainty this is opposite of compressibility where there is very less variation within the group so we can compress. Goal is to reduce entropy to improve predictability. 
Algorithm is to split the group and maximize the information gain till it is not further possible.
Finally in decsion tree algorithm cvan be stated as:
Start with root node corresponding to all instances
Iterately travese all nodes to see wherther "information gain" is poosible
For each node and for every attribute check what is the effect of spillintng the node in terms of information gain
Select the attribute with the buggest information gain above a given threshol;d
Continue until no significant improvement is possible
Return the decision tree

Many parameters are possible before learning decsion tree, one can set them
Minimal size of node to avoid overfitting
threshold setting minimal gain (no split if gain is too small)
Maximum deoth
allowing same label to appear multiple times or not 

alternate to entrpy is Gini index of diversity 
Splitting domain of a numerical variable
post pruning: remove leaf nodes that do not singnificantly increse the discrimintaive power.

Many application in process mining
what are driving these decisions, whay certains instances are going left and certain right, 
what is most liekyl path of a running case with given attribues
so we can apply decsion tree on the top of process mining. So make surre thatw e use process discovery to get the model from event log and then apply desesion tree learing.
Clustering and Association Rule Learning 


To understand Process Mining (see [this]( /tech/2022/2022/06/25/exploring_new_field_process_mining_intro.html) better, in this atricle I will try to dig into decisison trees which are the crucial element in process mining process discovery.

In next post, we'll do further digging in decision trees.

 
Thanks for reading!




