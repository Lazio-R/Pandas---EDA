# Python Code using Pandas for EDA

## Pandas library
- The pandas library is a powerful open-source Python tool designed for data manipulation and analysis.
- Pandas makes it easy to explore and prepare data for modeling, visualization, or reporting. It’s the backbone of most Python-based data workflows. 
- Using pandas for EDA (Exploratory Data Analysis) means leveraging the pandas library in Python to explore, understand, and prepare your dataset before modeling or decision-making.

## What is EDA?

### Exploratory Data Analysis (EDA) is the process of:
 - Summarizing the main characteristics of a dataset
 - Identifying patterns, anomalies, and relationships
 - Cleaning and transforming data for further analysis

## EDA Tasks with pandas

- Load data:	pd.read_csv(), pd.read_excel()
- View structure:	df.head(), df.info(), df.shape
- Summary statistics:	df.describe()
- Missing values:	df.isnull().sum()
- Value counts	df['column'].value_counts()
- Grouping and aggregation:	df.groupby()
- Correlation:	df.corr()
