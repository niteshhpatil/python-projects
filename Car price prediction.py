#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


from sklearn.model_selection import train_test_split


# In[6]:


from sklearn.linear_model import LinearRegression


# In[7]:


from sklearn.linear_model import Lasso


# In[8]:


from sklearn import metrics


# In[13]:


car_dataset = pd.read_csv(r'D:\python ex\DATA\vehicle price data\car data.csv')


# In[14]:


car_dataset.head()


# In[15]:


#checking the numuber of rows and colums
car_dataset.shape


# In[16]:


#getting some information about dataset
car_dataset.info()


# In[20]:


# Checking the number of missing values
car_dataset.isunll().sum()


# In[22]:


# checking the distribution of categorical data
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())


# In[26]:


# Encoding the categorical data
#encoding "Fuel_Type" Column
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

#encoding "Seller_Type" Column
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)


#encoding "Transmission" Column
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)


# In[27]:


car_dataset.head()


# In[33]:


#Splitting data and Target

X = car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
Y = car_dataset['Selling_Price']


# In[39]:


print(X)


# In[41]:


print(y)


# In[44]:


#Splitting Training and Test data

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size = 0.1,random_state=2)


# In[47]:


#Model Training

#Linear Regression Model

lin_reg_model = LinearRegression()


# In[49]:


lin_reg_model.fit(X_train,Y_train)


# In[50]:


#prediction on Training data 

training_data_prediction = lin_reg_model.predict(X_train) 


# In[52]:


# R squared error
error_score = metrics.r2_score(Y_train,training_data_prediction)
print("R squared Error :",error_score)


# In[53]:


#Visusalize the actual prices and Predicted prices
plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()


# In[56]:


#prediction on Training data 

test_data_prediction = lin_reg_model.predict(X_test) 


# In[58]:


# R squared error
error_score = metrics.r2_score(Y_test,test_data_prediction)
print("R squared Error :",error_score)


# In[59]:


#Visusalize the actual prices and Predicted prices
plt.scatter(Y_test,test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()


# In[ ]:


Lasso Regression
 

