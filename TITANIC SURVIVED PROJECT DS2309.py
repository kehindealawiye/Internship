#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# **LOAD AND PREPARE THE DATASET**

# In[17]:


# Load the Titanic dataset
titanic_data = pd.read_csv(r'C:\Users\ENVY\OneDrive\Documents\titanic_train.csv')


# In[18]:


titanic_data


# In[19]:


# Select features and target variable
X = titanic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
y = titanic_data['Survived']


# **DATA PREPROCESSING:**
# 
# Preprocess the data by handling missing values, converting categorical variables into numerical format (e.g., one-hot encoding for 'Sex'), and any other necessary preprocessing steps.

# In[20]:


# Check the structure and column names of X
print(X.head())  # Print the first few rows to inspect the data
print(X.columns)  # Check the column names


# In[21]:


# Check for missing values in the 'Sex' column
print(X['Sex'].isnull().sum())


# In[22]:


# Convert 'X' to a DataFrame if it's not already
X = pd.DataFrame(X, columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'])


# In[23]:


# One-hot encode the 'Sex' column 
X = pd.get_dummies(X, columns=['Sex'], drop_first=True)


# In[24]:


# Fill missing values with the mean (this assumes you've already checked for missing values)
X.fillna(X.mean(), inplace=True)


# **SPLIT DATA INTO TRAINING AND TESTING SETS**

# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[26]:


model = RandomForestClassifier(n_estimators=100, random_state=42)


# **TRAIN THE MODEL**

# In[27]:


model.fit(X_train, y_train)


# **MAKE PREDICTIONS**

# In[28]:


y_pred = model.predict(X_test)


# **EVALUATE THE MODEL**

# In[29]:


accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)

