# -*- coding: utf-8 -*-
"""Testing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qkL3iwrvtwKZYJL7O4Lp4p6NPcjVItC4
"""

from google.colab import drive
drive.mount('/content/drive')

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2019_1 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2019_1.xlsx')
df2019_2 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2019_2.xlsx')
df2020_1 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2020_1.xlsx')
df2020_2 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2020_2.xlsx')
df2021_1 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2021_1.xlsx')
df2021_2 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2021_2.xlsx')
df2022_1 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2022_1.xlsx')
df2022_2 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2022_2.xlsx')
df2023_1 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2023_1.xlsx')
df2023_2 = pd.read_excel('/content/drive/Shared drives/BDA/Crime_2023_2.xlsx')

df2019_1.head()

df2019_2['QualityOfLife'] = df2019_2['QualityOfLife'].replace({0: False, 1: True})
df2019_2.head()

df2020_1 = df2020_1.rename(columns={'FID':'ObjectID'})
df2020_1.drop('Attempt', axis=1, inplace=True)
df2020_1.head()

df2020_2 = df2020_2.rename(columns={'FID':'ObjectID'})
df2020_2.head()

df2021_1.head()

df2021_2 = df2021_2.rename(columns={'FID':'ObjectID'})
df2021_2.head()

df2022_1.head()

df2022_1.tail()

df2022_2['QualityOfLife'] = df2022_2['QualityOfLife'].replace({0: False, 1: True})
df2022_2.head()

df2023_1 = df2023_1.drop (['X','Y','LAT','LONG'], axis=1)
df2023_1 = df2023_1.rename(columns={'ObjectId':'ObjectID'})
df2023_1.head()

df2023_2 = df2023_2.drop (['X','Y','LAT','LONG'], axis=1)
df2023_2 = df2023_2.rename(columns={'ObjectId':'ObjectID'})
df2023_2.head()

df_2019 = pd.concat([df2019_1, df2019_2])
df_2019.head()

df_2020 = pd.concat([df2020_1, df2020_2])
df_2020.head()

df_2021 = pd.concat([df2021_1, df2021_2])
df_2021.head()

df_2022 = pd.concat([df2022_1, df2022_2])
df_2022.head()

df_2023 = pd.concat([df2023_1, df2023_2])
df_2023.head()

df_combined = pd.concat([df_2019, df_2020,df_2021, df_2022, df_2023 ])
df_combined.head()

df_combined.shape

import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame 'data' containing the provided data

# Convert 'DATEEND' to datetime format
df_combined['DATEEND'] = pd.to_datetime(df_combined['DATEEND'])

# Extract year from 'DATEEND'
df_combined['Year'] = df_combined['DATEEND'].dt.year

# Creating a new column for Quality of Life based on True/False values
df_combined['QualityOfLife'] = df_combined['QualityOfLife'].notnull()

# Filter crimes based on Quality of Life
quality_of_life_crimes = df_combined[df_combined['QualityOfLife']]

# Group by year and count the total crimes and quality of life crimes
total_crimes_by_year = df_combined.groupby('Year').size()
quality_of_life_crimes_by_year = quality_of_life_crimes.groupby('Year').size()

# Plotting the total crimes and quality of life crimes for different years
plt.figure(figsize=(10, 6))

plt.plot(total_crimes_by_year.index, total_crimes_by_year, label='Total Crimes')
plt.plot(quality_of_life_crimes_by_year.index, quality_of_life_crimes_by_year, label='Quality of Life Crimes')

plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.title('Total Crimes vs Quality of Life Crimes Over Years')
plt.legend()
plt.show()

# Convert 'Arrest' column to boolean type (True/False)
df_combined['Arrest'] = df_combined['Arrest'].replace({'Yes': True, 0: False})

# Calculate total reported crimes and total arrests
total_reported_crimes = df_combined.shape[0]
total_arrests = df_combined['Arrest'].sum()

# Calculate the percentage of reported crimes resulting in arrests
percentage_arrests = (total_arrests / total_reported_crimes) * 100

print(f"Total Reported Crimes: {total_reported_crimes}")
print(f"Total Arrests: {total_arrests}")
print(f"Percentage of Reported Crimes Resulting in Arrests: {percentage_arrests:.2f}%")

# Convert 'Arrest' column to boolean type (True/False)
df_combined['Arrest'] = df_combined['Arrest'].replace({'Yes': True, 0: False})

# Calculate total reported crimes and total arrests
total_reported_crimes = df_combined.shape[0]
total_arrests = df_combined['Arrest'].sum()

# Create a bar plot
fig, ax = plt.subplots()
bars = ax.bar(['Reported Crimes', 'Arrests'], [total_reported_crimes, total_arrests])

# Annotate the bars with their respective counts
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval), va='bottom')

# Set labels and title
ax.set_ylabel('Count')
ax.set_title('Reported Crimes vs. Arrests')

# Show the plot
plt.show()

import pandas as pd

# Convert 'DATEEND' column to datetime format
df_combined['DATEEND'] = pd.to_datetime(df_combined['DATEEND'])

# Extract features like month, day of the week, or other relevant time-related information
df_combined['Month'] = df_combined['DATEEND'].dt.month
# Extract additional time-related features as needed

# Group by month and count the occurrences of each crime category
crime_by_month = df_combined.groupby(['Month', 'CODE_DEFINED']).size().unstack()

# Visualize the trend of a specific crime category over months
specific_crime = 'LARCENY'  # Replace with the crime category of interest
crime_by_month[specific_crime].plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Occurrences')
plt.title(f'Trend of {specific_crime} Over Months')
plt.show()
df_combined.head()

import pandas as pd
import matplotlib.pyplot as plt
# Convert 'DATEEND' column to datetime format
df_combined['DATEEND'] = pd.to_datetime(df_combined['DATEEND'])

# Extract month and year from the date
df_combined['Month'] = df_combined['DATEEND'].dt.month
df_combined['Year'] = df_combined['DATEEND'].dt.year

# Group by year and month to observe the yearly patterns
crime_by_year_month = df_combined.groupby(['Year', 'Month']).size().unstack()

# Analyze and visualize yearly patterns for a specific crime category (e.g., 'AGGRAVATED ASSAULT')
specific_crime = 'AGGRAVATED ASSAULT'  # Replace with the crime category of interest
if specific_crime in df_combined['CODE_DEFINED'].unique():
    data_filtered = df_combined[df_combined['CODE_DEFINED'] == specific_crime]
    crime_filtered_by_year_month = data_filtered.groupby(['Year', 'Month']).size().unstack()

    crime_filtered_by_year_month.plot(kind='line')
    plt.xlabel('Month')
    plt.ylabel('Occurrences')
    plt.title(f'Yearly Patterns of {specific_crime} Over Months')
    plt.show()
else:
    print(f"Crime category '{specific_crime}' not found in the dataset.")

print(df_combined)

! pip install pyspark >& /dev/null
! pip install pyspark -q

# from pyspark.sql import SparkSession
# from pyspark import SparkContext
df_combined['QualityOfLife'] = df_combined['QualityOfLife'].replace({0: False, 1: True})
df_combined = df_combined

df_combined

#converting TIMESTART and TIMEEND to AM and PM time format.
def convert_to_ampm(time):
    try:
        time = float(time)
        if pd.notnull(time):
            if time < 1200:
                return f"{int(time // 100)}:{int(time % 100):02d} AM"
            elif time == 1200:
                return f"{int(time // 100)}:{int(time % 100):02d} PM"
            else:
                return f"{int(time // 100 - 12)}:{int(time % 100):02d} PM"
    except (ValueError, TypeError):
        return np.nan

# Apply conversion to 'TIMESTART' and 'TIMEEND' columns
df_combined['TIMESTART'] = df_combined['TIMESTART'].apply(convert_to_ampm)
df_combined['TIMEEND'] = df_combined['TIMEEND'].apply(convert_to_ampm)

# Display the updated DataFrame
print(df_combined)

df_combined.drop('TIME', axis=1, inplace=True)

df_combined

# Saving the cleaned DataFrame df_combined to a CSV file in the same file path

df_combined.to_csv('/content/drive/Shared drives/BDA/df_combined.csv', index=False)

from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext.getOrCreate()

spark = SparkSession\
    .builder\
    .appName('BDA Project Crime Data')\
    .getOrCreate()

spark = SparkSession.builder.appName("NaN_Value_Handling").getOrCreate()
df_combined = df_combined.fillna({
    'NumericalColumn': 0,          # Replace NaN with 0 for numerical columns
    'CategoricalColumn': 'Unknown', # Replace NaN with 'Unknown' for categorical columns
    'BooleanColumn': False          # Replace NaN with False for Boolean columns (if applicable)
})

#Creating a Schema and Spark Dataframe called Crime

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType, DateType
from pyspark.sql import functions as f

df_combined.replace({np.nan: None}, inplace=True)

# Define the schema for the DataFrame
schema = StructType([
    StructField("DATEEND", DateType(), True),
    StructField("TIMESTART", StringType(), True),
    StructField("TIMEEND", StringType(), True),
    StructField("ADDRESS", StringType(), True),
    StructField("CODE_DEFINED", StringType(), True),
    StructField("Arrest", BooleanType(), True),
    StructField("LarcenyCode", StringType(), True),
    StructField("ObjectID", IntegerType(), True),
    StructField("QualityOfLife", BooleanType(), True),
    StructField("Year", IntegerType(), True),
    StructField("Month", IntegerType(), True)
])

#creating a dataframe insurance
crime = spark.read.csv('/content/drive/Shared drives/BDA/df_combined.csv', header = True, schema = schema)

#Printing the resulting schema
crime.show()

from pyspark.sql.functions import hour, minute
from pyspark.sql.functions import expr

crime = crime.withColumn('HourStart', hour('TIMESTART'))
crime = crime.withColumn('MinuteStart', minute('TIMESTART'))

crime = crime.withColumn('Duration', expr("unix_timestamp(TIMEEND) - unix_timestamp(TIMESTART)"))

crime = crime.withColumn('Arrest', crime['Arrest'].cast('int'))
crime = crime.withColumn('QualityOfLife', crime['QualityOfLife'].cast('int'))

from pyspark.sql.functions import dayofmonth, month, year
crime = crime.withColumn('Day', dayofmonth('DATEEND'))
crime = crime.withColumn('Month', month('DATEEND'))
crime = crime.withColumn('Year', year('DATEEND'))

from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline
categorical_columns = ['CODE_DEFINED', 'LarcenyCode']
num_columns = ['Arrest']
indexer = [StringIndexer(inputCol=col, outputCol=col + "_index", handleInvalid="skip")for col in categorical_columns]

encoders = [OneHotEncoder(inputCol=col + "_index", outputCol=col + "_onehot") for col in categorical_columns]

assembler = VectorAssembler(inputCols=num_columns + [col + "_onehot" for col in categorical_columns], outputCol="features", handleInvalid="keep")

crime_pipe = Pipeline(stages= indexer + encoders + [assembler])

try:
    crime_fe = crime_pipe.fit(crime).transform(crime)
except Exception as e:
    print("Error:", e)

# Print the column names of the DataFrame
print(crime.columns)

from pyspark.sql.functions import col, isnan, when, count

# Check for nulls
null_counts = crime.select([count(when(col(c).isNull() | isnan(col(c)), c)).alias(c) for c in ['Arrest']]).show()

# If there are null values, you need to decide how to handle them

# Option 1: Fill null values with a default value (e.g., False)
crime = crime.na.fill({'Arrest': False})

# Option 2: Drop rows where 'Arrest' is null
crime = crime.na.drop(subset=["Arrest"])

null_counts = crime.select([count(when(col(c).isNull() | isnan(col(c)), c)).alias(c) for c in ['Arrest']]).show()

default_values = {'HourStart': 0, 'MinuteStart': 0, 'Duration': 0, 'Day': 0, 'Month': 0, 'Year': 0, 'CODE_DEFINED': 'Unknown', 'LarcenyCode': 'Unknown'}
crime = crime.na.fill(default_values)

columns_to_check = ['HourStart', 'MinuteStart', 'Duration', 'Day', 'Month', 'Year', 'CODE_DEFINED', 'LarcenyCode']
crime = crime.dropna(subset=columns_to_check)

"""**DESCISION TREE**"""

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Adjusted columns based on your DataFrame
categoricalCols = ['CODE_DEFINED', 'LarcenyCode']
indexers = [StringIndexer(inputCol=c, outputCol="{0}_indexed".format(c), handleInvalid="keep") for c in categoricalCols]
encoders = [OneHotEncoder(inputCol=indexer.getOutputCol(), outputCol="{0}_encoded".format(indexer.getOutputCol())) for indexer in indexers]

# VectorAssembler to combine feature columns
assemblerInputs = [encoder.getOutputCol() for encoder in encoders] + ['HourStart', 'MinuteStart', 'Duration', 'Day', 'Month', 'Year']
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")

# Decision Tree Model
dt = DecisionTreeClassifier(labelCol="Arrest", featuresCol="features")

# Pipeline
pipeline = Pipeline(stages=indexers + encoders + [assembler, dt])

# Split the data into training and test sets
(trainData, testData) = crime.randomSplit([0.7, 0.3])

# Train the model
model = pipeline.fit(trainData)

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Make predictions
predictions = model.transform(testData)

# Evaluate the model using MulticlassClassificationEvaluator for accuracy
evaluator = MulticlassClassificationEvaluator(labelCol="Arrest", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)

print("Accuracy = %g" % accuracy)

# Evaluate Weighted Precision (equivalent to Precision in binary classification)
precision_evaluator = MulticlassClassificationEvaluator(labelCol="Arrest", predictionCol="prediction", metricName="weightedPrecision")
precision = precision_evaluator.evaluate(predictions)

# Evaluate Weighted Recall (equivalent to Recall in binary classification)
recall_evaluator = MulticlassClassificationEvaluator(labelCol="Arrest", predictionCol="prediction", metricName="weightedRecall")
recall = recall_evaluator.evaluate(predictions)

# Evaluate F1 Score
f1_evaluator = MulticlassClassificationEvaluator(labelCol="Arrest", predictionCol="prediction", metricName="f1")
f1_score = f1_evaluator.evaluate(predictions)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1_score}")

"""**K-Means Clustering:**


"""

from pyspark.sql.functions import regexp_replace, lower
from pyspark.ml.feature import Tokenizer, HashingTF
from pyspark.ml.clustering import KMeans

crime = crime.withColumn('streetName', regexp_replace(crime['ADDRESS'], '^\d+\s', ''))

#Tokenization (Split the street names into words)
tokenizer = Tokenizer(inputCol="streetName", outputCol="tokens")
df_tokens = tokenizer.transform(crime)

#Feature Transformation (Convert street names to numeric feature vectors)
hashingTF = HashingTF(inputCol="tokens", outputCol="features", numFeatures=100)
featurizedData = hashingTF.transform(df_tokens)

#Clustering (Use K-Means or another clustering algorithm)
kmeans = KMeans().setK(5).setSeed(1)
model = kmeans.fit(featurizedData)

#Analysis (Make predictions to see which cluster each address belongs to)
predictions = model.transform(featurizedData)
predictions.select('streetName', 'prediction').show(truncate=False)

"""**GBT Model**"""

from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline


predictions = predictions.withColumnRenamed('prediction', 'cluster')

crime_with_cluster = crime.join(predictions.select('streetName', 'cluster'), on='streetName')

categorical_features = ['CODE_DEFINED', 'LarcenyCode']
indexers = [StringIndexer(inputCol=column, outputCol=column+"_index") for column in categorical_features]
encoders = [OneHotEncoder(inputCols=[indexer.getOutputCol() for indexer in indexers], outputCols=[indexer.getOutputCol()+"_encoded" for indexer in indexers])]


assemblerInputs = [indexer.getOutputCol()+"_encoded" for indexer in indexers] + ['Year', 'Month', 'HourStart', 'MinuteStart', 'Duration', 'Day', 'cluster']
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")

gbt = GBTClassifier(labelCol="QualityOfLife", featuresCol="features", maxIter=10)


(trainData, testData) = crime.randomSplit([0.7, 0.3])


pipeline = Pipeline(stages=indexers + encoders + [assembler, gbt])


pipelineModel = pipeline.fit(trainData)

predictions = pipelineModel.transform(testData)

evaluator = MulticlassClassificationEvaluator(labelCol="QualityOfLife", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
precision = evaluator.setMetricName("weightedPrecision").evaluate(predictions)
recall = evaluator.setMetricName("weightedRecall").evaluate(predictions)
f1 = evaluator.setMetricName("f1").evaluate(predictions)

print(f"Accuracy = {accuracy}")
print(f"Precision = {precision}")
print(f"Recall = {recall}")
print(f"F1 Score = {f1}")









