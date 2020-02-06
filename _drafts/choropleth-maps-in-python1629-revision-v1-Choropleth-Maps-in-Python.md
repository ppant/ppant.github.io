---
id: 1644
title: Choropleth Maps in Python
date: 2017-02-03T23:06:57+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2017/02/1629-revision-v1/
permalink: /2017/02/03/1629-revision-v1/
---
Choropleth maps are a great way to represent geographical data. I have done a basic implementation of two different data sets. I have used [jupyter notebook](http://jupyter.org/) to show the plots.

**World Power Consumption 2014**

First do Plotly imports  
`import plotly.graph_objs as go<br />
from plotly.offline import init_notebook_mode,iplot<br />
init_notebook_mode(connected=True)<br />
` 

Next step is to fetch the dataset, we&#8217;ll use Python [pandas](http://pandas.pydata.org/) library to read the read the csv file

`import pandas as pd<br />
df = pd.read_csv('2014_World_Power_Consumption')<br />
` 

Next, we need to create data and layout variable which contains a dict

<p style="padding-left: 30px;">
  <code>data = dict(type='choropleth',&lt;br />
</code><code>locations = df['Country'],&lt;br />
locationmode = 'country names', z = df['Power Consumption KWH'],&lt;br />
text = df['Country'], colorbar = {'title':'Power Consumption KWH'},&lt;br />
colorscale = 'Viridis', reversescale = True)&lt;br />
</code><br /> Let&#8217;s make a layout
</p>

<p style="padding-left: 30px;">
  <code>layout = dict(title='2014 World Power Consumption',&lt;br />
geo = dict(showframe=False,projection={'type':'Mercator'}))&lt;br />
</code>
</p>

<p style="padding-left: 30px;">
  Pass the data and layout and plot using iplot
</p>

<p style="padding-left: 30px;">
  <code>choromap = go.Figure(data = [data],layout = layout)&lt;br />
iplot(choromap,validate=False)&lt;br />
</code>
</p>

<p style="padding-left: 30px;">
  The output will be be like below:
</p>

<p style="padding-left: 30px;">
  <a href="http://pradeeppant.com/wp-content/uploads/2017/02/2014_world_power_consumption_chorlopleth_plot.png"><img class="aligncenter wp-image-1639" src="http://pradeeppant.com/wp-content/uploads/2017/02/2014_world_power_consumption_chorlopleth_plot-300x193.png" alt="" width="404" height="260" srcset="http://pradeeppant.com/wp-content/uploads/2017/02/2014_world_power_consumption_chorlopleth_plot-300x193.png 300w, http://pradeeppant.com/wp-content/uploads/2017/02/2014_world_power_consumption_chorlopleth_plot.png 700w" sizes="(max-width: 404px) 100vw, 404px" /></a>
</p>

<p style="padding-left: 30px;">
  Check <a href="https://github.com/ppant/Datascience-MI-Bootcamp-Python/blob/master/Choropleth_Maps_Exercise_solutions.py">github</a> for full code.
</p>

<p style="padding-left: 30px;">
  In next post I will try to make a choropleth for a different data set.
</p>

<p style="padding-left: 30px;">
   References:<a href="https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp"> </a>
</p>

<p style="padding-left: 30px;">
  <a href="https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp">https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp</a>
</p>

      <https://plot.ly/python/choropleth-maps/>

<p style="padding-left: 30px;">