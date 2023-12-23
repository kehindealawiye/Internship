#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV


# In[5]:


# Load the dataset
url = "https://github.com/FlipRoboTechnologies/ML-Datasets/raw/main/Red%20Wine/winequality-red.csv"
wine_data = pd.read_csv(url)

# Explore the dataset
print(wine_data.head())


# In[ ]:


# Preprocess the data
wine_data['good_wine'] = np.where(wine_data['quality'] >= 7, 1, 0)
X = wine_data.drop(['quality', 'good_wine'], axis=1)
y = wine_data['good_wine']


# In[ ]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a Decision Tree model
dt_classifier = DecisionTreeClassifier(random_state=42)


# In[ ]:


# Hyperparameter tuning using GridSearchCV
param_grid = {'max_depth': [3, 5, 7, 9],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4]}

grid_search = GridSearchCV(dt_classifier, param_grid, cv=5, scoring='roc_auc')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

# Train the model with the best parameters
best_dt_classifier = DecisionTreeClassifier(**best_params, random_state=42)
best_dt_classifier.fit(X_train, y_train)


# In[ ]:


# Exploratory Data Analysis (EDA)
sns.pairplot(wine_data, hue='good_wine')
plt.show()

correlation_matrix = wine_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


# In[ ]:


# Cross-Validation
cv_scores = cross_val_score(best_dt_classifier, X_train, y_train, cv=5, scoring='roc_auc')
print("Cross-Validation Scores:", cv_scores)
print("Mean AUC from Cross-Validation: {:.2f}".format(np.mean(cv_scores)))


# In[ ]:


# Feature Importance
feature_importance = best_dt_classifier.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importance')
plt.show()


# In[ ]:


# Predict on the test set
y_pred_prob = best_dt_classifier.predict_proba(X_test)[:, 1]

# Calculate ROC curve and AUC
fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)


# In[ ]:


# Visualize ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()


# In[ ]:


# Confusion Matrix
y_pred = best_dt_classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Good', 'Good'], yticklabels=['Not Good', 'Good'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()


# In[ ]:


# Evaluate the model
accuracy = best_dt_classifier.score(X_test, y_test)
print("Accuracy: {:.2f}".format(accuracy))
print("AUC: {:.2f}".format(roc_auc))

