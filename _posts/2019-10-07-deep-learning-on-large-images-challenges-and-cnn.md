---
id: 2096
title: 'Deep learning on large images: challenges and CNN'
date: 2019-10-07T20:13:25+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2096
permalink: /2019/10/07/deep-learning-on-large-images-challenges-and-cnn/
---
Applying deep learning on large images is always a challenge but there a solution using convolutional but first, let&#8217;s understand in brief where is the challenge? So one of the challenges in computer vision is that inputs become very big as we increase image size. 

Ok. Consider the example of a basic image classification problem e.g.; cat detection.

Let&#8217;s take an input 64&#215;64 image of a cat and try to figure out if that is a cat or not? to do that we&#8217;ll need 64x64x3, (where 3 is the no of RGB channel) parameters, so the x input feature will have 12288 dimensions though this is not a very large number considering just the 64&#215;64 image size which is very small there are lots of input features to deal with..

Say now if we take 1000&#215;1000 image (1MB) which is decent in size but there will be 1000x1000x3 (where 3 are the RGB channels) ~ 3M input features

so if you put in a deep network then x will be 3M, and suppose if first hidden layer has 1000 hidden units then the total no of weights for a fully connected network will be (Weight matrix, X) ~ (1000, 3M) dimension means that the matrix will have 3 Billion parameters which are very very large, so with that much of data it is difficult to avoid overfitting in Neural Network and also the computational requirement to train the 3 Billion params is not feasible. 

This is just for a 1MB image but in computer vision problem you don&#8217;t want to stick with using just tiny images using bigger images results in overfitting and huge input feature vector so here comes convolution operation which is the basic building block of Convolutional Neural Network (CNN).<figure class="wp-block-image">

<img src="http://pradeeppant.com/wp-content/uploads/2019/10/deep_learning_on_large_images-1024x580.png" alt="" class="wp-image-2106" srcset="http://pradeeppant.com/wp-content/uploads/2019/10/deep_learning_on_large_images-1024x580.png 1024w, http://pradeeppant.com/wp-content/uploads/2019/10/deep_learning_on_large_images-300x170.png 300w, http://pradeeppant.com/wp-content/uploads/2019/10/deep_learning_on_large_images-768x435.png 768w, http://pradeeppant.com/wp-content/uploads/2019/10/deep_learning_on_large_images.png 1145w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Image Source: Andrew Ng Deep Learning Course</figcaption></figure> 

  
  
More on CNN in the next post.

Cheers!

_Inspiration & source of understanding: Andrew Ng, Deep Learning Specialization  
_