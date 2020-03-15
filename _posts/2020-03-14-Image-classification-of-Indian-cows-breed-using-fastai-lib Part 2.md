---
title: 'Image classification of Indian cows breed using fastai lib Part 2'
date: 2020-03-14T6:46:03+05:30
author: Pradeep Pant
layout: post
---

Inspiration of this blog post came from [fast.ai](https://course.fast.ai/videos/?lesson=2) course taught by Jeremy Howard. 
In the [Part 1](/2020/02/29/Image-classification-of-Indian-cows-breed-using-fastai-lib.html) of this post we'll learned how to build your image classification model using your own data through Google Images.

In this part we'll discuss about how to train the model and finally put the model in production.


We'll go through all these steps as I create a model that can take on the vital task of differentiating among different asian/indian cows breeds **sindhi**, **hallikar** and **bargur**. 
We'll be using Google Colab, data will reside in Google drive which we'll map to Jupyter notebook.

### Train model
````python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
````

````python
learn.fit_one_cycle(4)
Downloading: "https://download.pytorch.org/models/resnet34-333f7ec4.pth" to /root/.cache/torch/checkpoints/resnet34-333f7ec4.pth
100% 83.3M/83.3M [00:04<00:00, 20.4MB/s]

epoch	train_loss	valid_loss	error_rate	time
0	1.833954	1.676055	0.416667	00:53
1	1.701250	1.972784	0.481481	00:08
2	1.645258	1.958620	0.583333	00:06
3	1.581880	1.893333	0.583333	00:06

learn.save('stage-1')
learn.unfreeze()
learn.lr_find()

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

![indian_cows_breed_preview.png](\data\images\indian_cows_breed_preview.png)

So now we have images in each category, in next post we'll see how to train the model to make a Indian Cows breed classifier.

*btw Happy leap year day :-)*

#### References: 
* [fast.ai](https://course.fast.ai/videos/?lesson=2)
* [Jupyter Notebook](https://jupyter.org/)
* Check full code at [GitHub](https://github.com/ppant/course-v3/blob/master/lesson2_ppant_cows_classifier.ipynb)