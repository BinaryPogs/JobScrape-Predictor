# Indeed DataScrape + Machine Learning predictions


# Introduction
This is a web scraping program that scrapes the first 20 pages of the job advertising website Indeed.com based on a certain search criteria. It scrapes information from the job description such as candidate requirements so that I can analyse the data and can quickly identify which jobs I want to apply for.

# How it works

The goal of this program is to scrape a large amount of job requirements/data from the [website](www.indeed.com), create a .csv file containing that data. I will then label the with the response `Applied` which indicates whether or not I would apply for the job. I will then use the labelled data as my training set for my predictive model and see how well my model can predict whether or not I would want to apply for the new, unseen jobs. To do this I will be using a RandomForestClassifier or a GBM, as well as stemming/lemmatizing and TF-IDF. 

Below is an example of marked data which I have manually trained:
[Sample training data](https://github.com/SnowQuack/JobScrape-Predictor/blob/master/sampletrain.png?raw=true)

