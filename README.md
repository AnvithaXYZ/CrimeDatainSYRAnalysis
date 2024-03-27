# CrimeDatainSYRAnalysis
The project utilized diverse datasets covering historical crime records, socio-economic indicators, demographic information, weather patterns, and geographical features spanning five years (2019-2023). Initial steps involved meticulous data collection and preprocessing, addressing missing values and implementing feature engineering techniques.

Dataset Description
The dataset includes Part 1 and Part 2 crime data from the City of Syracuse, spanning five years from 2019 to 2023. Part 1 crimes include serious offenses such as Homicide, Rape, Robbery, and Aggravated Assault, while Part 2 includes other offenses like Kidnapping, Simple Assault, and Stolen Property. The combined dataset comprises 63,449 crime event records across 11 variables.

Exploratory Data Analysis (EDA)
EDA focuses on understanding the dataset through visualizations, identifying patterns, and preparing the data for predictive modeling. Key EDA steps involve data cleaning, handling missing values, and feature engineering to enhance model performance.

Prediction and Inference Goals
Crime Rate Prediction: Predicting the overall crime rate and specific crimes in different locations.
Arrest Probability: Estimating the likelihood of an arrest given a reported crime.
Quality of Life Impact Prediction: Assessing how crimes impact the quality of life in Syracuse.
Type of Larceny Prediction: Predicting the type of larceny based on historical data.
Methodologies
The project employs various machine learning models, including Random Forest, Decision Trees, Logistic Regression, and Gradient Boosted Trees, for robust crime prediction. It also involves feature engineering techniques to prepare data for modeling and evaluates model performance using metrics like accuracy, precision, recall, and F1-score.

How to Run the Code
Ensure Python and required libraries (pandas, numpy, matplotlib, sklearn, pyspark) are installed.
The code primarily runs in Google Colab, mounting Google Drive for data storage and access.
Load the dataset files into Google Drive as specified in the code.
Follow the sequence of code cells, starting from loading libraries, mounting Google Drive, reading the dataset, and progressing through data preprocessing, EDA, model training, and evaluation.
Problems Encountered
Challenges included data cleaning due to inaccuracies and handling large datasets in Google Colab. Despite these, various models provided valuable insights, although some, like Linear Regression, showed limitations in predictive performance.

Citations
City of Syracuse Open Data Inventory: Link
Syracuse Crime Data: Link
For more details on the project setup, methodologies, and results, please refer to the project report and code files.
