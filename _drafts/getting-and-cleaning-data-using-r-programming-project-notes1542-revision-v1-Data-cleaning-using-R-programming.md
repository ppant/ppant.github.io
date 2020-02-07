---
id: 1568
title: Data cleaning using R programming
date: 2016-06-30T14:02:25+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2016/06/1542-revision-v1/
permalink: /2016/06/30/1542-revision-v1/
---
Brief notes from learning from course project on [data getting and cleaning on](https://www.coursera.org/learn/data-cleaning) coursera.

The purpose of this project is to demonstrate your ability to collect, work with, and clean a data set. The goal is to prepare tidy data that can be used for later analysis.

One of the most exciting areas in all of the data science right now is wearable computing &#8211; see for example companies like Fitbit, Nike, tomtom, Garmin etc are racing to develop the most advanced algorithms to attract new users. In this case study, the data is collected from the accelerometers from the Samsung Galaxy S smartphone. A full description is available at the site where the data was obtained:

<http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones>

Here is the dataset for the project:

<https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip>

I have created an R script called _run_analysis.R_ which does the following.

  * Merges the training and the test sets to create one data set.
  * Extracts only the measurements on the mean and standard deviation for each measurement.
  * Uses descriptive activity names to name the activities in the data set
  * Appropriately labels the data set with descriptive variable names.
  * Finally, creates a second, independent tidy data set with the average of each variable for each activity and each subject. 
    Ref:</li> </ul> 
    
    <http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones>  
    <https://www.coursera.org/learn/data-cleaning>
    
    &nbsp;
    
    For working code and tidy dataset please check my [Github](https://github.com/ppant/getting-and-cleaning-data-project-coursera) repo.
    
    &nbsp;