---
title: 'Image classification of Flowers in Machine Learning: Challenges and developments'

date: 2020-05-25T1:46:03+05:30
author: Pradeep Pant
layout: post
---


![](/data/images/iris_dataset_cover.jpg)


Flower classification is one of the most widely studied examples of machine learning. Some of the advantage of flower/plant classification to detect rare species which can be used in medicine, agriculture, etc. On the other hand, it is also very challenging that there is a diversity of flower species and it is very hard to classify them when they can be very similar to each other. Therefore, this subject has already become crucial.

Classification of [iris flowers](https://en.wikipedia.org/wiki/Iris_flower_data_set) is the standard dataset. One of the challenges in flower classification is the lack of labeled data which can result in performance loss. Recognizing a large number of classes within one category of flowers is also a challenge. If we have more classes then combinations of features can improve classification performance. 

In flower classification, we mainly used the feature like local shape/texture, the shape of the boundary, the overall spatial distribution of petals, and the color classifying flowers which poses an extra challenge over the categories such as bikes, cars, and cats, because of the large similarity between classes. Another challenge with flower classification is that flowers are non-rigid objects that can deform in many ways, and consequently there is also a large variation within classes. More the no of classes add more complexity but performance get an increase. 
also what distinguishes one flower from another can sometimes be just the color, sometimes the shape and sometimes patterns on the petals. The difficulty lies in finding suitable features to represent color, shape, patterns, etc.

Newer techniques like  Deep CNN and Deep CNN and Data Augmentation have demonstrated better performance. 


#### References and further reading
* Excellent Research Paper [Automated flower classification over a large number of classes](http://www.robots.ox.ac.uk/~vgg/publications/papers/nilsback08.pdf)
* [IRIS Flower Dataset](https://www.kaggle.com/arshid/iris-flower-dataset/)
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.php)
* [IEEE: Flower Classification with Deep CNN and Machine Learning Algorithms](https://ieeexplore.ieee.org/document/8932908)
