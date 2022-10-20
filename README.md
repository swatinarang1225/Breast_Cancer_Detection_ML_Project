# Breast Cancer Detection ML Project
## Web Application to predict Breast Cancer using Logistic regression
**Note: Deployment for this Web application is done through Heroku app and procedure is described in below steps.**

![project front](https://user-images.githubusercontent.com/28431152/196962909-90bac9b4-bec9-4e69-a754-335868fefd2b.JPG)

[Deployed on Heroku](https://breast-cancer-detection-webapp.herokuapp.com/)
 
## Objective:
This repositiory is an practical exercise:

1. To apply Machine Learning Fundamentals with already prepared Dataset.
2. Evaluating my results and justify the interpretation based on observed Data Set.

## Project Requirements
* Anaconda Python (for Python libraries)
* pip install flask - for Front End application.

The analysis has been done through the following steps:

### 1. Data Preprocessing

* <ins>**Loading the data:-**</ins> The prepared data at [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?select=data.csv) have been used to                                       train the model
* <ins>** Data Exploration:-**</ins> This step involves the analysis to better understand the nature of data using data visualization and Statistical techniques such as                                      size, quantity, and accuracy.
* <ins>** Dealing with missing Values:-**</ins> Here we dropped or removed the column or row in case of any null values.
* <ins>** Dealing with categorical Data:-**</ins> Used pandas get_dummies function 
* <ins>** Countplot, Correlation matrix and Heatmap:-**</ins> T find the extent of relation between various features in the dataset.

## 2. Model Development

* <ins>**Splitting Dataset:-**</ins> We split Dataset into 2 categories: Training Dataset and testing Dataset. We have build the model with training dataset and                                            verified the accuracy of the final model using test dataset.
* <ins>**Feature Scaling:-**</ins>  scaled the data to make it easy for a model to learn and understand the problem.
* <ins>** Accurate Model:-**</ins> Trained many models using training dataset and finalize 1 model wth highest accuracy values and test the final model with test data.                                    Also, can verify the model with a singl value set from the dataset

### 3.Backened Creation

After finalizing and testing the model, maintain trained model using pickle which can be be used to connect with Flask application.





