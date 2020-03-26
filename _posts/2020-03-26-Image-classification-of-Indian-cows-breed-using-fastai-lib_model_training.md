---
title: 'Image classification of Indian cows breed using fastai lib: Train Model'

date: 2020-03-26T6:46:03+05:30
author: Pradeep Pant
layout: post
---

Inspiration of this blog post came from [fast.ai](https://course.fast.ai/videos/?lesson=2) course taught by Jeremy Howard. 
In the [Part 1](/2020/02/29/Image-classification-of-Indian-cows-breed-using-fastai-lib.html) of this post we'll learned how to build your image classification model using your own data through Google Images.

In this part we'll discuss about how to train the model and finally put the model in production.

We'll go through all these steps as I create a model that can take on the vital task of differentiating among different asian/indian cows breeds **sindhi**, **hallikar** and **bargur**. 

We'll be using Google Colab, data will reside in Google drive which we'll map to Jupyter notebook.

### Train model
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

### Interpretatation

For interpreatation we first have to saved model from stage 2
learn.load('stage-2')
We can check confusion matrix to visulise how many were actual and predicted.
interp = ClassificationInterpretation.from_learner(learn)
````python
path()
[PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/sindhi'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/hallikar'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/bargur'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/models'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/cleaned.csv')]
````
### Cleaning Up
Some of our top losses aren't due to bad performance by our model. There are images in our data set that shouldn't be.

Using the ImageCleaner widget from fastai.widgets we can prune our top losses, removing photos that don't belong.
````python
from fastai.widgets import *
````
First we need to get the file paths from our top_losses. We can do this with .from_toplosses. We then feed the top losses indexes and corresponding dataset to ImageCleaner.
In order to clean the entire set of images, we need to create a new dataset without the split
````python
db = (ImageList.from_folder(path)
                   .split_none()
                   .label_from_folder()
                   .transform(get_transforms(), size=224)
                   .databunch()
     )
````
Then we create a new learner to use our new databunch with all the images.
````python
learn_cln = cnn_learner(db, models.resnet34, metrics=error_rate)
learn_cln.load('stage-2');
ds, idxs = DatasetFormatter().from_toplosses(learn_cln)
````
Make sure you're running this notebook in Jupyter Notebook, not Jupyter Lab. I am running Google Colab so it does not show GUI 
#### Step 3:
Create a new CNN learner with the above new created databunch and load the model’s weights that you previously saved before these cleaning steps.
````python
learn_clean = create_cnn(data, models.resnet34, metrics=error_rate)
learn_clean.load('Lesson 2 stage-2')
````
#### Step 4:
Calculate the losses
````python
losses, idxs = DatasetFormatter().from_toplosses(learn_clean)
````
### Put your model in production
Steps to export the content of our learned model and use it in production:

#### Step 1:
Export the model.
````python
learn.export()
````
This will create a file named ‘export.pkl’ in the directory where we are working. The file contains everything we need to deploy our model (the model, the weights but also some metadata like the classes or the transforms/normalization used).
![Production Model Test Image.png](\data\images\production_test_image_cows_breed_classifier.png)
#### Step 2:
Open the image which is to be tested.
````python
img = open_image(path/'filename.jpg')
````

#### Step-3:
Load the learner that we exported previously and predict the class of the img image file.

````python
learn = load_learner(path)
pred_class, pred_idx, outputs = learn.predict(img)
pred_class
````
the pred_class is the predicted class of the image, the outputs variable contains the probability of each of the classes. path is the path where your export.pkl file lies.

### Things that can go wrong

#### Learning rate (LR) too high
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(1, max_lr=0.5)
````
#### Learning rate (LR) too low
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(5, max_lr=1e-5)
learn.recorder.plot_losses()
````
#### Too few epochs
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate, pretrained=False)
learn.fit_one_cycle(1)
````
#### Too many epochs
````python
np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.9, bs=32, 
        ds_tfms=get_transforms(do_flip=False, max_rotate=0, max_zoom=1, max_lighting=0, max_warp=0
                              ),size=224, num_workers=4).normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet50, metrics=error_rate, ps=0, wd=0)
learn.unfreeze()
learn.fit_one_cycle(40, slice(1e-6,1e-4))
````
#### References: 
* [fast.ai](https://course.fast.ai/videos/?lesson=2)
* [Jupyter Notebook](https://jupyter.org/)
* Check full code at [GitHub](https://github.com/ppant/course-v3/blob/master/lesson2_ppant_cows_classifier.ipynb)




