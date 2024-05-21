# -*- coding: utf-8 -*-
"""Afame_P2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uyDtPkxZp0CPRR_K07h3JNjz7Mfis7hB
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv('HR Data.csv')
df

# Display the data types of each column
print("Data Types of Columns:")
print(df.dtypes)

# Display common information about the columns
print("\nCommon Information about Columns:")
for column in df.columns:
    unique_values = df[column].nunique()
    data_type = df[column].dtype
    if unique_values <= 10:  # Adjust the threshold as needed
        values = df[column].unique()
        print(f"{column}: {data_type}, {unique_values} unique values, Values: {values}")
    else:
        print(f"{column}: {data_type}, {unique_values} unique values")

# Data Cleansing
# Remove unnecessary columns
unnecessary_columns = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']
df_cleaned = df.drop(columns=unnecessary_columns)

# Rename columns
new_column_names = {
    'MonthlyIncome': 'Income',
    'YearsAtCompany': 'Tenure'
    # Add more renames as needed
}
df_cleaned = df_cleaned.rename(columns=new_column_names)

# Eliminate redundant entries (if any)
df_cleaned = df_cleaned.drop_duplicates()

# Eliminate NaN values
df_cleaned = df_cleaned.dropna()

# Display the cleaned dataset
print(df_cleaned.head())