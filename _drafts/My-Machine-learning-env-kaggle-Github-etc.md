---
id: 2250
title: My Machine learning env (kaggle, Github etc)
date: 2019-12-23T12:04:14+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=2250
permalink: /?p=2250
---
A quick post about my local working env to develop machine learning projects.

I use the following tools extensively.

Anaconda -> Jupyter notebook

Github

Kaggle kernels

My toolkit is pretty standard for Kaggle: **pandas**, **numpy**, **sklearn**, **XGBoost**, **LightGBM**, **Keras**. I work in Jupyter notebooks, and I am a big fan of J**upyter Lab**.

I think for most of the learning purposes CPU training is sufficient still if you need GPU support then I would recommend using some cloud instances (AWS, Google etc) for a short duration for that specific training.

I will walk over to a kaggle competition and will show the steps of how I use the Github and other envs.

&#8212; CREATE ENVIRONMENT/WORKSPACE FOR PYTHON 3.7 

C:\conda create &#8211;name neuralnets python=3.7

C:\activate neuralnets

&#8212; INSTALL EVERYTHING (notice the neuralnets workspace in parenthesis on each line). ACCEPT ANY DEPENDENCIES EACH OF THOSE STEPS WANTS TO INSTALL:  
(neuralnets) C:\conda install theano

(neuralnets) C:\conda install mingw libpython(neuralnets) 

C:\pip install tensorflow

(neuralnets) C:\pip install keras  
conda install -c conda-forge opencv

conda install -c menpo opencv3  
C:\activate neuralnets

Remove env

conda env remove -n ENV_NAME

  * Make a github repo for titatnic kaggle competetion including readme a
  * clone github repo to local machine
  * Add titatnic dataset and notebook
  * Open anaconda prompt and type &#8220;jupyter notebook&#8221;
  * Make the changes in notebook&nbsp;
  * commit the files to git&nbsp;
  * push the changes in github (This can be used to send the code and documentation to other data sources like blogs, code repos etc) Jekyll
  * Open a new kernel in kaggle
  * Upload the notebook which you have committed to github, change the input files path if needed&nbsp;
  * commit the kernel&nbsp;
  * you can further do submission of&nbsp; your predictions using sumit button and can make your kernel public