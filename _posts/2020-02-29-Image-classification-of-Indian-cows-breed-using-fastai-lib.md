---
title: 'Image classification of Indian cows breed using fastai lib'
date: 2020-02-29T6:46:03+05:30
author: Pradeep Pant
layout: post
---

Inspiration of this blog post came from [fast.ai](https://course.fast.ai/videos/?lesson=2) course taught by Jeremy Howard. 
In first part of this post we'll learn how to build your image classification model using your own data through Google Images.

We'll go through all these steps as I create a model that can take on the vital task of differentiating among different asian/indian cows breeds **sindhi**, **hallikar** and **bargur**. 
We'll be using Google Colab, data will reside in Google drive which we'll map to Jupyter notebook.

### Map Google Drive 
````python
from fastai.vision import *
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"
base_dir = root_dir + 'fastai-v3/'
````
It will ask to Enter your Google authorization code and drived will be mapped and you will see 
a message like *Mounted at*
````python 
/content/gdrive 
````

### Get a list of URLs
#### Search and scroll
Go to Google Images and search for the images for **sindhi** cows. The more specific you are in your Google Search, the better the results and the less manual pruning you will have to do.

Scroll down until you've seen all the images you want to download, or until you see a button that says 'Show more results'. All the images you scrolled past are now available to download. 

Repeat the same procedure for **hallikar** cows and **bargur** cows.

#### Download into file
You need to run following command on Google Chrome Console

````python
urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));
window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));
````
### Create directory and upload urls file into your server

````python
folder = 'sindhi'
file = 'urls_sindhi_cows.txt'

folder = 'hallikar'
file = 'urls_hallikar_cows.txt'

folder = 'bargur'
file = 'urls_bargur_cows.txt'

path = Path(base_dir + 'data/cows_breed_classifier')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)
````
Check if paths are populated correctly
````python
path.ls()
[PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/sindhi'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/hallikar'),
 PosixPath('/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/bargur'),
 ````
Finally, upload your urls file.

### Download images
Time to download images from respective URL's 
````python
classes = ['sindhi','bargur','hallikar']
````
fastai has a function to download images. We'll just use that..
````python
download_images('/content/gdrive/My Drive/fastai-v3/data/urls/urls_sindhi_cows.txt', dest, max_pics=200)

download_images('/content/gdrive/My Drive/fastai-v3/data/urls/urls_bargur_cows.txt', dest, max_pics=200)

download_images('/content/gdrive/My Drive/fastai-v3/data/urls/urls_hallikar_cows.txt', dest, max_pics=200)
````
Then we can remove any images that can't be opened

````python
for c in classes:
print(path/c)
verify_images(path/c, delete=True, max_size=500)
````
You will see something like below.
````python
/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/sindhi
/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/bargur
/content/gdrive/My Drive/fastai-v3/data/cows_breed_classifier/hallikar
````

### View data
first we'll clean the data and then will view some random pics
````python
np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)

data.classes
['bargur', 'hallikar', 'sindhi']

````
Show random pics from all categories
````python
data.classes, data.c, len(data.train_ds), len(data.valid_ds)
(['bargur', 'hallikar', 'sindhi'], 3, 432, 108)
````

![Indian Cows Breed Preview](\data\images\indian_cows_breed_preview.png)

So now we have images in each category, in next post we'll see how to train the model to make a Indian Cows breed classifier.

*btw Happy leap year day :-)*

#### References: 
* [fast.ai](https://course.fast.ai/videos/?lesson=2)
* [Jupyter Notebook](https://jupyter.org/)
* Check full code at [GitHub](https://github.com/ppant/course-v3/blob/master/lesson2_ppant_cows_classifier.ipynb)