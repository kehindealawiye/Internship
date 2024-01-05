#!/usr/bin/env python
# coding: utf-8

# In[54]:


import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from math import sqrt
import scipy.stats as stats
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import PowerTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import warnings 
warnings.simplefilter('ignore')


# In[55]:


# Load the dataset
happiness_data = pd.read_csv(r'C:\Users\ENVY\OneDrive\Documents\happiness_score_dataset.csv')

# Explore the dataset
print(happiness_data.head())


# In[57]:


happiness_data.columns


# In[58]:


happiness_data.shape


# In[59]:


happiness_data.isnull().sum()


# In[60]:


happiness_data.info


# In[61]:


happiness_data.describe()


# In[63]:


happiness_data_New=happiness_data.drop(['Country','Region','Happiness Rank'],axis=1)


# In[64]:


upper_triangel=np.tril(happiness_data_New.corr())
sns.heatmap(happiness_data_New.corr(),vmin=-1,vmax=1,annot=True,annot_kws={'size':10},cmap='gist_earth',mask=upper_triangel)
plt.show()


# In[65]:


corr_hmap=happiness_data_New.corr()
plt.figure(figsize=(20,10))
sns.heatmap(corr_hmap,annot=True,cmap='gist_earth')
plt.show()


# In[66]:


#Using the PairPlot:
sns.pairplot(happiness_data_New)
plt.show()


# In[67]:


plt.rcParams['figure.figsize']=(20,20)
happiness_data_New.hist(bins=20,color='blue',density=True,label='Value',histtype='bar')
plt.tight_layout()
plt.show()


# In[68]:


happiness_data_New.plot(kind='box',subplots=True,layout=(5,7),figsize=(20,20),notch=True)


# In[69]:


happiness_data_New.skew()


# Outilier removal:

# In[72]:


# z Score Method:
z=np.abs(zscore(happiness_data_New))
threshold=3
np.where(z>3)
happiness_data_New1=happiness_data_New[(z<3).all(axis=1)]
happiness_data_New1


# In[73]:


# Percentage of Data Loss:
data_loss=(158-149)/158*100
data_loss


# In[74]:


x=happiness_data_New1.drop('Happiness Score',axis=1)# list of all Feature
y=happiness_data_New1['Happiness Score'] # Label


# In[75]:


x.shape


# In[76]:


y.shape


# In[77]:


x.head


# In[78]:


y.head


# Scaling

# In[81]:


scale1=PowerTransformer(method='yeo-johnson')
x_scaled=pd.DataFrame(scale1.fit_transform(x),columns=x.columns)


# In[82]:


x_scaled


# In[83]:


#Creating the Training and Testing data sets:
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,train_size=0.75, random_state=42, shuffle=True)


# In[84]:


# Model Selection:
linear_model=LinearRegression()
svr_model=SVR(C=1.0,epsilon=0.2,kernel='poly',gamma='auto')
dtr_model=DecisionTreeRegressor(criterion='poisson',random_state=111)
rfr_model=RandomForestRegressor(max_depth=2,max_features="sqrt")
knr_model=KNeighborsRegressor(n_neighbors=2,algorithm='kd_tree')


# In[85]:


# Training the Models:
linear_model.fit(x_train,y_train)
svr_model.fit(x_train,y_train)
dtr_model.fit(x_train,y_train)
rfr_model.fit(x_train,y_train)
knr_model.fit(x_train,y_train)


# In[86]:


#Prediction:
pred_linear=linear_model.predict(x_test)
pred_svr=svr_model.predict(x_test)
pred_dtr=dtr_model.predict(x_test)
pred_rfr=rfr_model.predict(x_test)
pred_knr=knr_model.predict(x_test)


# Evaluation Metrics

# In[88]:


se_linear=mean_squared_error(y_test,pred_linear)
se_svr=mean_squared_error(y_test,pred_svr)
se_dtr=mean_squared_error(y_test,pred_dtr)
se_rfr=mean_squared_error(y_test,pred_rfr)
se_knr=mean_squared_error(y_test,pred_knr)

rmse_linear=sqrt(se_linear)
rmse_svr=sqrt(se_svr)
rmse_dtr=sqrt(se_dtr)
rmse_rfr=sqrt(se_rfr)
rmse_knr=sqrt(se_knr)

print(f"RMSE of Linear Regression is: ", rmse_linear)
print(f"RMSE of Support Vector Regression is: ", rmse_svr)
print(f"RMSE of Decision Tree Regressor is: ", rmse_dtr)
print(f"RMSE of Random Forest Regressor is: ", rmse_rfr)
print(f"RMSE of K Neighbors Regressor is: ", rmse_knr)


# In[89]:


#R2 Score for the model:

print(f"R2 Score for Linear Regression is:",r2_score(y_test,pred_linear,multioutput='variance_weighted')*100)
print(f"R2 Score for Support Vector Regression is:",r2_score(y_test,pred_svr,multioutput='variance_weighted')*100)
print(f"R2 Score for Decision Tree Regressor  is:",r2_score(y_test,pred_dtr,multioutput='variance_weighted')*100)
print(f"R2 Score for Random Forest Regressor  is:",r2_score(y_test,pred_rfr,multioutput='variance_weighted')*100)
print(f"R2 Score for K Neighbors Regressor  is:",r2_score(y_test,pred_knr,multioutput='variance_weighted')*100)


# In[95]:


#Hyper Parameter Tuning on the best ML Model:
Lr_Param={'fit_intercept':[True,False],'n_jobs':[True,False],'copy_X':[True,False],'n_jobs':[1,2,3,4,5,6,7,8,9,10]}
    


# In[96]:


from sklearn.model_selection import GridSearchCV


# In[97]:


GSCV=GridSearchCV(LinearRegression(),Lr_Param,cv=5)


# In[98]:


GSCV.fit(x_train,y_train)


# In[99]:


GSCV.best_params_


# In[104]:


Final_model=LinearRegression(copy_X=True,fit_intercept=True, n_jobs=1)
CLassifer=Final_model.fit(x_train,y_train)
lr_pred=Final_model.predict(x_test)
lr_r2_score = r2_score(y_test, lr_pred, multioutput='variance_weighted')
print(f"R2 score for the Final Model is:", lr_r2_score*100)


# In[ ]:




