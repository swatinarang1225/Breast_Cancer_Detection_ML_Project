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
* <ins>**Data Exploration:-**</ins> This step involves the analysis to better understand the nature of data using data visualization and Statistical techniques such as                                      size, quantity, and accuracy.
* <ins>**Dealing with missing Values:-**</ins> Here we dropped or removed the column or row in case of any null values.
* <ins>**Dealing with categorical Data:-**</ins> Used pandas get_dummies function 
* <ins>**Countplot, Correlation matrix and Heatmap:-**</ins> T find the extent of relation between various features in the dataset.

### 2. Model Development

* <ins>**Splitting Dataset:-**</ins> We split Dataset into 2 categories: Training Dataset and testing Dataset. We have build the model with training dataset and                                            verified the accuracy of the final model using test dataset.
* <ins>**Feature Scaling:-**</ins>  scaled the data to make it easy for a model to learn and understand the problem.
* <ins>**Accurate Model:-**</ins> Trained many models using training dataset and finalize 1 model wth highest accuracy values and test the final model with test data.                                    Also, can verify the model with a singl value set from the dataset

### 3.Backened Creation

After finalizing and testing the model, maintain trained model using pickle which can be be used to connect with Flask application. In this project file is named as model.pkl.

### 4. Front-End Creation(Flask Application)

* Breast Cancer detection.ipynb — This contains code for the machine learning model to predict cancer based on the class.
* main.py — This contains Flask APIs that receives cells details through GUI or API calls, computes the predicted value based on our model and returns it
* templates & static — This folders contains the HTML template and CSS styling to allow user to enter cells details and displays the predicted output.

### 5. Integrating application with ML backened
 * Create main.py in which we have used flask web framework to handle POST and GET methods.
 *  Use numpy to python package to create array of requested data and pickle pacakge to load trained model to predict.
 *  we have bounded /api with the method predict(). In which predict method gets the data from the json passed by the requestor. model.predict() method takes input from the json and converts it into 2D numpy array the results are stored into the variable named prediction.   


### 6. Deployed on Heroku
To deploy the application on Heroku refer article [Heroku Deployment](https://medium.com/student-technical-community-vit-vellore/deploying-flask-app-on-heroku-using-github-504a40ed40de#:~:text=On%20Heroku%2C%20when%20it%20comes,repository%20to%20your%20Heroku%20app.)

## How to Execute the Code on local:
* Download the repository and extract in a folder.
* Verify the python version installed on your machine. This project runs on Python 3.6 and above.
* Now install the requirements mention in requirements.txt file.
* Execute the python script on terminal using : python main.py

## Contributions
Although it is an exercise to perform hands-on on the skill, but Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
For any questions,queries or suggestions, feel free to contact me at [swatinarang1225@gmail.com]







