# Movie-Series_french_review_satisfaction_prediction

This project objective is to create a machine learning model that predict movie or series satisfaction
just with a french text review. 

## Data collection

First we need data, so I decided to collect data from "https://www.allocine.fr/".
I collected more than 10 000 reviews with their respective ranking with web scrapping.
To get the dataset, I wrote and run a script called "scrapp_review.py". The data will
be stored in a csv file "allocine_reviews.csv".

## Model training

Data exploration, preprocessing, model training and evaluation are in "review_prediction.ipynb" notebook:

   - Data reading
   - Preprocessing with TFIDF Vectorizer
   - Training with a neural network
   - Model evaluation
   - Example tests with custom reviews

The result will be a score between 0 and 1, with 0 a very bad review and 1 an excellent one.
