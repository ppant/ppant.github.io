---
title: 'Image classification of Indian cows breed using fastai lib: Train Model'

date: 2020-03-28T1:46:03+05:30
author: Pradeep Pant
layout: post
---

Inspiration of this blog post came from [fast.ai](https://course.fast.ai/videos/?lesson=2) course taught by Jeremy Howard. 
In the [Part 1](/2020/02/29/Image-classification-of-Indian-cows-breed-using-fastai-lib.html) of this post we'll learned how to build your image classification model using your own data through Google Images.

In this part we'll discuss about how to train the model and finally put the model in production.

We'll go through all these steps as I create a model that can take on the vital task of differentiating among different asian/indian cows breeds **sindhi**, **hallikar** and **bargur**. 

We'll be using Google Colab, data will reside in Google drive which we'll map to Jupyter notebook.
#### Path
Review the path in Google drive where we have stored the raw and cleaned images 

````python
path()
[PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/sindhi'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/hallikar'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/bargur'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/models'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/cleaned.csv')]
````

### Training the model
Now we have data, so we'll create our convolutional neural network. We'll use default *resnet34* architecture.

To Train the model we'll use the below commands:
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(4)
learn.save('stage-1')
learn.unfreeze()
learn.lr_find()
learn.fit_one_cycle(2, max_lr=slice(3e-06,3e-3))
learn.save('stage-2')
````
*In the example Jeremy gave error rate was about 2% but with me on cows data set it's higher ~ 5%, which need to brought down* **[todo]**

### Interpretatation
We can use the ClassificationInterpretation class to find how the prection process is going on...

For interpreatation we first have to saved model from stage 2
````python
learn.load('stage-2')
````
We can check confusion matrix to visulise how many were actual and predicted.
````python
interp = ClassificationInterpretation.from_learner(learn)
````
### Cleaning Up
It seems that some of our top losses aren't due to bad performance by our model. There are images in our data set that shouldn't be.

Using the *ImageCleaner* widget from *fastai.widgets* we can prune our top losses, removing photos that don't belong to the dataset.

````python
from fastai.widgets import *
````
First we need to get the file paths from our *top_losses*. We can do this with *.from_toplosses*. We then feed the top losses indexes and corresponding dataset to *ImageCleaner*.
In order to clean the entire set of images, we need to create a new dataset without the split

````python
db = (ImageList.from_folder(path)
                   .split_none()
                   .label_from_folder()
                   .transform(get_transforms(), size=224)
                   .databunch()
     )
````
Then we create a new CNN learner to use our new databunch with all the images and load the model's weights which was saved in pre steps before cleaning.
````python
learn_cln = cnn_learner(db, models.resnet34, metrics=error_rate)
learn_cln.load('stage-2');
````
Calculate the losses

````python
ds, idxs = DatasetFormatter().from_toplosses(learn_cln)
````
Make sure you're running this notebook in Jupyter Notebook, not in Jupyter Lab. I am running Google Colab so it does not show GUI.

### Put your model in production
Steps to export the content of our learned model and use it in production:

First export the content of our Learner object for production.
#### Step 1:
Export the model.
````python
learn.export()
````
This will create a file named ‘*export.pkl*’ in the directory where we are working. The file contains everything we need to deploy our model (the model, the weights but also some metadata like the classes or the transforms/normalization used).
#### Step 2:
Open the image which is to be tested.

![Production Model Test Image.png](\data\images\production_test_image_cows_breed_classifier.png)

#### Step-3:
Load the learner that we exported previously and predict the class of the image file.

````python
learn = load_learner(path)
pred_class, pred_idx, outputs = learn.predict(img)
pred_class
````
the pred_class is the predicted class of the image, the outputs variable contains the probability of each of the classes. path is the path where your *export.pkl* file lies.

### Things that can go wrong
Most likely are we might have to tune:  
* Learning rate
* Number of epochs

##### Learning rate (LR) too high
Let’s go back to our cow breed detector. and let’s make our learning rate really high. The default learning rate is 0.003 that works most of the time. So what if we try a learning rate of 0.5. That’s huge. What happens?
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(1, max_lr=0.5)
````

Our validation loss gets pretty damn high. Remember, this is something that’s normally something underneath 1. So if you see your validation loss do that, before we even learn what validation loss is, just know this, if it does that, your learning rate is too high. That’s all you need to know. Make it lower. Doesn’t matter how many epochs you do. If this happens, there’s no way to undo this. You have to go back and create your neural net again and fit from scratch with a lower learning rate. Excellent Explanation By PoonamV [resource](https://forums.fast.ai/t/deep-learning-lesson-2-notes/28772)

##### Learning rate (LR) too low
What if we used a learning rate, not of default *0.003* but *1e-5 (0.00001)*?

````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(5, max_lr=1e-5)
learn.recorder.plot_losses()
````
You can just see them gradually going down so slow. If you see that happening, then you have a learning rate which is too small. So bump it by 10 or bump it up by 100 and try again. The other thing you see if your learning rate is too small is that your training loss will be higher than your validation loss. You never want a model where your training loss is higher than your validation loss. That always means you haven’t fitted enough which means either your learning rate is too low or your number of epochs is too low. So if you have a model like that, train it some more or train it with a higher learning rate.

##### Too few epochs

````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate, pretrained=False)
learn.fit_one_cycle(1)
````

What if we train for just one epoch? Our error rate is certainly better than random, 5%. But look at the difference between training loss and validation loss, a training loss is much higher than the validation loss. So too few epochs and too lower learning rate look very similar. So you can just try running more epochs and if it’s taking forever, you can try a higher learning rate. If you try a higher learning rate and the loss goes off to 100,000 million, then put it back to where it was and try a few more epochs. That’s the balance. That’s all you care about 99% of the time. And this is only the 1 in 20 times that the defaults don’t work for you.

##### Too many epochs
Too many epochs create overfitting". If you train for too long as we’re going to learn about it, it will learn to recognize your particular cow breed but not cows in general. Here is the thing. Despite what you may have heard, it’s very hard to overfit with deep learning. So we were trying today to show you an example of overfitting and Jeremy turned off everything. He turned off all the data augmentation, dropout, and weight decay. He tried to make it overfit as much as he can. He trained it on a small-ish learning rate and trained it for a really long time. And maybe he started to get it to overfit. Maybe.

````python
np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.9, bs=32, 
        ds_tfms=get_transforms(do_flip=False, max_rotate=0, max_zoom=1, max_lighting=0, max_warp=0
                              ),size=224, num_workers=4).normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet50, metrics=error_rate, ps=0, wd=0)
learn.unfreeze()
learn.fit_one_cycle(40, slice(1e-6,1e-4))
````

Basically, if you are overfitting there is only one thing you can notice which is that the error rate improves for a while and then starts getting worse again. You will see a lot of people, even people that claim to understand machine learning, tell you that if your training loss is lower than your validation loss, then you are overfitting. As you will learn today in more detail and during the rest, of course, that is absolutely not true.
Any model that is trained correctly will always have train loss lower than validation loss.
That is not a sign of overfitting. That is not a sign you’ve done something wrong. That is a sign you have done something right. The sign that you’re overfitting is that your error starts getting worse because that’s what you care about. You want your model to have a low error. So as long as you’re training and your model error is improving, you’re not overfitting. How could you be?

#### References 
* [fast.ai](https://course.fast.ai/videos/?lesson=2)
* [Jupyter Notebook](https://jupyter.org/)
* Check full code at [GitHub](https://github.com/ppant/course-v3/blob/master/lesson2_ppant_cows_classifier.ipynb)

