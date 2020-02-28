---
id: 2128
title: 'CNN: Understanding edge detection with an example'
date: 2019-11-21T21:23:30+05:30
author: Pradeep Pant
layout: post
guid: /?p=2128
permalink: /2019/11/21/cnn-understanding-edge-detection-with-an-example/
---
<p style="text-align:left">
  The convolution operation is one of the fundamental building blocks of a convolutional neural network and here we&#8217;ll discuss edge detection as an example to see how the convolution operation works. In my last <a href="/2019/10/deep-learning-on-large-images-challenges-and-cnn/"><strong>post</strong></a>, we saw how the early layers of the neural network might detect edges and then some later layers might detect parts of objects and then even later layers may detect parts of complete objects like people&#8217;s faces.
</p><figure class="wp-block-image">

<img src="/wp-content/uploads/2019/10/edge_detection_problems-e1571219621597-1024x278.png" alt="" class="wp-image-2129" srcset="/wp-content/uploads/2019/10/edge_detection_problems-e1571219621597-1024x278.png 1024w, /wp-content/uploads/2019/10/edge_detection_problems-e1571219621597-300x82.png 300w, /wp-content/uploads/2019/10/edge_detection_problems-e1571219621597-768x209.png 768w, /wp-content/uploads/2019/10/edge_detection_problems-e1571219621597.png 1067w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption> _Image Source: Andrew Ng Deep Learning Course_ </figcaption></figure> 

In this post, we&#8217;ll see how we can detect edges in an image. 

Given a picture below:<figure class="wp-block-image">

<img src="/wp-content/uploads/2019/10/edge_detection_problems-1-e1571219766497-1024x355.png" alt="" class="wp-image-2131" srcset="/wp-content/uploads/2019/10/edge_detection_problems-1-e1571219766497-1024x355.png 1024w, /wp-content/uploads/2019/10/edge_detection_problems-1-e1571219766497-300x104.png 300w, /wp-content/uploads/2019/10/edge_detection_problems-1-e1571219766497-768x266.png 768w, /wp-content/uploads/2019/10/edge_detection_problems-1-e1571219766497.png 1067w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption> _Image Source: Andrew Ng Deep Learning Course_ </figcaption></figure> 

that for a computer to figure out what are the objects in this picture, the first thing you might do is maybe detect vertical edges in this image. For example, the first image on left has all vertical lines (marked in red), where the buildings are and pedestrians and so those get detected in this vertical edge detector output. And we also want to detect horizontal edges so for example, there is a very strong horizontal line where the railing is also got detected. Now let&#8217;s see in detail, how we detect edges in images like above?

Let us look with an example, Here is a 6&#215;6 grayscale image and because this is a grayscale image, this is just a 6x6x1 matrix rather than 6x6x3 because they are on separate RGB channels. In order to detect edges or lets say vertical edges in this image, what you can do is construct a 3&#215;3 matrix and in the terminology of convolutional neural networks, this is going to be called a filter and we&#8217;re going to construct a 3&#215;3 filter or 3&#215;3 matrix and now what we are going to do is take the 6&#215;6 image and convolve it and the convolution operation is denoted by this asterisk(*) and convolve it with the 3 x3 filter. The output of this convolution operator will be a 4&#215;4 matrix, which we can interpret as a 4&#215;4 image. The way we compute this 4 x4 output is shown in fig below. <figure class="wp-block-image">

<img src="/wp-content/uploads/2019/10/vertical_edge_detection-1024x508.png" alt="" class="wp-image-2130" srcset="/wp-content/uploads/2019/10/vertical_edge_detection-1024x508.png 1024w, /wp-content/uploads/2019/10/vertical_edge_detection-300x149.png 300w, /wp-content/uploads/2019/10/vertical_edge_detection-768x381.png 768w, /wp-content/uploads/2019/10/vertical_edge_detection.png 1163w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption> _Image Source: Andrew Ng Deep Learning Course_ </figcaption></figure> 

**Explanation:** Looking on to the diagram to compute the first elements, the upper left element of the 4&#215;4 matrix, what we are going to do is take the 3&#215;3 filter and paste it on top of the 3&#215;3 region of our original input image (left side) and what we should do is take the element-wise product (check the calculation method at the top of diagram in red). Similarly, we can calculate elements of a 4&#215;4 image. These are really just matrices of various dimensions. But the matrix on the left is convenient to interpret as an image, and the one in the middle we interpret as a filter and the one on the right, we can interpret that as maybe another image And this turns out to be a vertical edge detector. 

Let&#8217;s look at another example and see how exactly vertical edge detection is happening?. To illustrate this, we are going to use a simplified image. Here is a simple 6&#215;6 image where the left half of the image is 10 and the right half is zero. If you plot this as a picture, it might look like this, where the left half, the 10s, give you brighter pixel intensive values and the right half gives you darker pixel intensive values. We are using a shade of gray to denote zeros, in this image, there is clearly a very strong vertical edge right down the middle of this image as it transitions from white to black or white to a darker color. When we convolve this with a 3&#215;3 filter and so this 3&#215;3 filter can be visualized as follows, where we can see that lighter, brighter pixels are on the left and zeroes in the middle and then darker on the right. What we get is the rightmost matrix.<figure class="wp-block-image">

<img src="/wp-content/uploads/2019/10/vertical_edge_detection_1-1024x584.png" alt="" class="wp-image-2132" srcset="/wp-content/uploads/2019/10/vertical_edge_detection_1-1024x584.png 1024w, /wp-content/uploads/2019/10/vertical_edge_detection_1-300x171.png 300w, /wp-content/uploads/2019/10/vertical_edge_detection_1-768x438.png 768w, /wp-content/uploads/2019/10/vertical_edge_detection_1.png 1171w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption> _Image Source: Andrew Ng Deep Learning Course_ </figcaption></figure> 

Now, if we plot rightmost matrix&#8217;s image it will look like that where there is this lighter region right in the middle and that corresponds to this having detected this vertical edge down the middle of our 6&#215;6 image. In case the dimensions here seem a little bit wrong that the detected edge seems really thick, that&#8217;s only because we are working with very small images in this example. And if we use, say a 1000&#215;1000 image rather than a 6&#215;6 image then you find that this does a pretty good job, really detecting the vertical edges in our image. In this example, the bright region in the middle is just the output images way of saying that it looks like there is a strong vertical edge right down the middle of the image. So in this way, we detect vertical edges using convolutional operator. 

In the next post, I will try to explain more edge detection examples also horizontal edge detection etc.

Happy learning!