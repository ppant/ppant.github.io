---
id: 1542
title: Getting and cleaning data using R programming project notes
date: 2016-06-30T14:25:31+05:30
author: Pradeep Pant
layout: post
guid: /?p=1542
permalink: /2016/06/30/getting-and-cleaning-data-using-r-programming-project-notes/
---
Brief notes of my learning from course project of[ getting and cleaning data](https://www.coursera.org/learn/data-cleaning) course from [John Hopkins University](https://www.jhu.edu/).

The purpose of this project is to demonstrate the ability to collect, work with, and clean a data set. Final goal here is to prepare tidy data that can be used for later analysis.

One of the most exciting areas in all of the data science right now is wearable computing &#8211; see for example companies like Fitbit, Nike, tomtom, Garmin etc are racing to develop the most advanced algorithms to attract new users. In this case study, the data is collected from the accelerometers from the Samsung Galaxy S smartphone. A full description is available at the site where the data was obtained:

<http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones>

Here is the dataset for the project:

<https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip>

I have created an R script called _run_analysis.R_ which does the following.

  * Merges the training and the test sets to create one data set.
  * Extracts only the measurements on the mean and standard deviation for each measurement.
  * Uses descriptive activity names to name the activities in the data set.
  * Appropriately labels the data set with descriptive variable names.
  * Finally, creates a second, independent tidy data set with the average of each variable for each activity and each subject.References:

<http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones>  
[https://www.coursera.org/learn/data-cleaning  
https://github.com/ppant/getting-and-cleaning-data-project-coursera](https://www.coursera.org/learn/data-cleaning)

&nbsp;

For working code and tidy dataset please check my [Github](https://github.com/ppant/getting-and-cleaning-data-project-coursera) repo.

&nbsp;