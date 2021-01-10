# Python for Data Analysis Project
## The Dataset

The Dataset called "Online Shoppers Purchasing Intention" is a dataset composed of 18 variables : 10 numerical and 8 categorical.
It has 12330 lines of data regarding the data of visitors of websites.

The goal here is to predict whether if the visitor will be buying or not according to his data.

The column 'Revenue' is the target of our study. It's True if the visitor will buy and False if he will not buy.

"Administrative", "Administrative Duration", "Informational", "Informational Duration", "Product Related" and "Product Related Duration" represent the number of
different types of pages visited by the visitor in that session and total time spent in each of these page. The values of these features are derived from
the URL information of the pages visited by the user and updated in real time when a user takes an action, e.g. moving from one page to another. The "Bounce Rate",
"Exit Rate" and "Page Value" features represent the metrics measured by "Google Analytics" for each page in the e-commerce site. The value of "Bounce Rate" feature
for a web page refers to the percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics
server during that session. The value of "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in
the session. The "Page Value" feature represents the average value for a web page that a user visited before completing an e-commerce transaction. The "Special Day" feature
indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with
transaction. The value of this attribute is determined by considering the dynamics of e-commerce such as the duration between the order date and delivery date. For example,
for Valentina’s day, this value takes a nonzero value between February 2 and February 12, zero before and after this date unless it is close to another special day, and its
maximum value of 1 on February 8. The dataset also includes operating system, browser, region, traffic type, visitor type as returning or new visitor, a Boolean value
indicating whether the date of the visit is weekend, and month of the year.

## My work

* Data Visualization : The goal here is to visualize the data in several ways to understand it. To understand the target 'Revenue' and it's link to other variables
* Modelling : The goal here is to test different models on the data to get the best prediction possible. I used :
    * Random Forest
    * Logistic Regression
    * SVM
    * Naïve Bayes
    * K-Nearest Neighbors
* Creating an API with one model to simulate and predict input data


## What will you find on this Git

* A Jupyter Notebook containing data visualization and modelling
* A PowerPoint (in .pdf) explaining the problem and my work
* An API folder containing the API


## My conclusions

After the data visualization, we could see that the variable mostly linked to the target 'Revenue' is the 'PageValues'. All the other variables don't have a strong correlation with the target however all of them are useful for the model

After using 5 different models, I arrived to the conclusion that the best model was the Random Forest with 89,54% of accuracy.


## API

The API was created using Flask.

To use the API : 
* git clone https://github.com/yan-podolak/ESILV/tree/main/Python%20for%20Data%20Analysis/API
* python app.py
* Go to : http://127.0.0.1:5000/
