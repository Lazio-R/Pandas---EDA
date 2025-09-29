# Databricks notebook source
# MAGIC %md
# MAGIC ########### Pandas - EDA(Exploratory Data Analysis) #########

# COMMAND ----------

# MAGIC %md
# MAGIC Metadata

# COMMAND ----------

## Metadata is simply “data about data.” 
    - It doesn’t hold the content itself, but it describes and gives context to that content so it’s easier to understand, organize, and use.



# COMMAND ----------

# MAGIC %md
# MAGIC Install Dependencies

# COMMAND ----------

!pip install openpyxl -q

# COMMAND ----------

# MAGIC %md
# MAGIC Pandas and Numpy Libraries

# COMMAND ----------


## The pandas library is one of the most essential tools in Python for data analysis and manipulation.
    - Read and write data, Clean and transform, Analyze and visualize, manipulate data.

## NumPy (short for Numerical Python) is a foundational library for scientific computing in Python.
    - Efficient handling of large arrays and matrices, 
    - Fast mathematical operations, 
    - Support for linear algebra, statistics, and random number generation

# COMMAND ----------

## The line import pandas as pd is used to bring the pandas library into your Python environment and give it the nickname pd.
    # pd is just a short alias — instead of typing pandas.read_csv(), you can type pd.read_csv().

import pandas as pd

## The line import numpy as np is used to bring the NumPy library into your Python environment and give it the alias np. This makes it easier and faster to use NumPy’s powerful tools for numerical computing.
import numpy as np

# COMMAND ----------

# MAGIC %md
# MAGIC Data Load/Ingestion

# COMMAND ----------

## data_path is a variable that stores the path to the CSV file that contains the data you want to analyze.
    # CSV file location
data_path = "/Workspace/Users/ramslazio@gmail.com/Viewership Analysis.csv"



# COMMAND ----------

## Excel file location

# data_path = "/Workspace/Users/ramslazio@gmail.com/Viewership Analysis.xlsx"

# COMMAND ----------

## The pd.read_csv() function is used to read data from a CSV file into a pandas DataFrame. The function takes the path to the CSV file as an argument and returns a DataFrame object that contains the data from the CSV file.

# df = pd.read_csv(data_path)

# COMMAND ----------

## survey_analysis = df is a line of code that assigns the DataFrame object df to a new variable called survey_analysis. This allows you to work with the data in the DataFrame using the survey_analysis variable instead of df.

survey_analysis = pd.read_csv(data_path)

# COMMAND ----------

# Display data

display(survey_analysis)

# COMMAND ----------

# survey_analysis.head() is a method that displays the first few rows of the DataFrame.
survey_analysis.head()

# COMMAND ----------

# survey_analysis.shape is a method that displays the number of rows and columns.
survey_analysis.shape


# COMMAND ----------

# survey_analysis.dtypes is a method that displays the data types of each column.
# Displays data types of columns
survey_analysis.dtypes

# COMMAND ----------

# survey_analysis.describe() is a method that displays a summary of the DataFrame, including the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values for each column.
survey_analysis.describe()

# COMMAND ----------

# survey_analysis.info() is a method that displays information about the DataFrame, including the number of rows, data types of each column, and memory usage
survey_analysis.info()

# COMMAND ----------

# survey_analysis.columns is a line of code that displays the column names of the DataFrame.
survey_analysis.columns

# COMMAND ----------

# Check unique values in the 'playeventtype' column using pandas
survey_analysis['PlayEventType'].unique()

# COMMAND ----------

# Check unique values in the 'platform' column using pandas
survey_analysis['Platform'].unique()

# COMMAND ----------

# Check unique values in the 'videotitle' column using pandas
survey_analysis['VideoTitle'].unique()

# COMMAND ----------

# Check unique values in the 'totaltimewatched' column using pandas
survey_analysis['TotalTimeWatched'].unique()

# COMMAND ----------

survey_analysis['TotalTimeWatched'].min()

# COMMAND ----------

survey_analysis['TotalTimeWatched'].max()

# COMMAND ----------


# Check for duplicate rows in the DataFrame using pandas
survey_analysis.duplicated().sum()


# COMMAND ----------

# Check for missing values in the DataFrame using pandas

survey_analysis.isnull().sum()

# COMMAND ----------

# Dropping duplicate rows
survey_analysis.drop_duplicates(inplace=True)
# Dropped 1 duplicate rows
survey_analysis.duplicated().sum()

# COMMAND ----------

help(pd.Series.loc)