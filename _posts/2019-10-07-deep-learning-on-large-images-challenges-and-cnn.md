---
title: 'Deep learning on large images: challenges and CNN'
date: 2019-10-07T20:13:25+05:30
author: Pradeep Pant
layout: post
---
Applying deep learning on large images is always a challenge but there a solution using convolutional but first, let&#8217;s understand in brief where is the challenge? So one of the challenges in computer vision is that inputs become very big as we increase image size. 

Ok. Consider the example of a basic image classification problem e.g.; cat detection.

Let's take an input **64x64** image of a cat and try to figure out if that is a cat or not? to do that we'll need **64x64x3**, (where 3 is the no of RGB channel) parameters, so the x input feature will have 12288 dimensions though this is not a very large number considering just the **64x64** image size which is very small there are lots of input features to deal with..

Say now if we take **1000x215x1000** image (1MB) which is decent in size but there will be **1000x1000x3** (where 3 are the RGB channels) ~ 3M input features

so if you put in a deep network then x will be 3M, and suppose if first hidden layer has 1000 hidden units then the total no of weights for a fully connected network will be (Weight matrix, X) ~ (1000, 3M) dimension means that the matrix will have 3 Billion parameters which are very very large, so with that much of data it is difficult to avoid overfitting in Neural Network and also the computational requirement to train the 3 Billion params is not feasible. 

This is just for a 1MB image but in computer vision problem you don't want to stick with using just tiny images using bigger images results in overfitting and huge input feature vector so here comes convolution operation which is the basic building block of Convolutional Neural Network (CNN).

  ![](/wp-content/uploads/2019/10/deep_learning_on_large_images-1024x580.png "Deep learning on large images")

*Image Source: Andrew Ng Deep Learning Course* 

More on CNN in the next post.

Cheers!


*Inspiration & source of understanding: Andrew Ng, Deep Learning Specialization*  