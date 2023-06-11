#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as plt


# In[2]:


df=pd.read_csv('https://raw.githubusercontent.com/niteen11/DataAnalyticsAcademy/master/Python/dataset_diabetes/diabetic_data.csv')


# In[3]:


# Reviewing Data Set
df.head()


# In[23]:


df.dtypes


# In[58]:


# Cleaning Data - Drop Columns not needed
drop_cols=['admission_source_id',
          'payer_code',
           'weight',
          'medical_specialty',
          'num_lab_procedures',
          'num_procedures',
          'num_medications',
          'number_outpatient',
          'number_inpatient',
          'diag_1',
          'diag_2',
          'diag_3',
          'number_diagnoses',
          'max_glu_serum',
          'metformin',
          'repaglinide',
          'nateglinide',
          'chlorpropamide',
          'glimepiride',
          'acetohexamide',
          'glipizide',
          'glyburide',
          'tolbutamide',
          'pioglitazone',
          'rosiglitazone',
          'acarbose',
          'miglitol',
          'troglitazone',
          'tolazamide',
          'examide',
          'citoglipton',
          'insulin',
          'glyburide-metformin',
          'glipizide-metformin',
           'A1Cresult',
          'glimepiride-pioglitazone',
          'metformin-rosiglitazone',
          'metformin-pioglitazone'
]


# In[59]:


#Data review/confirm dropped Columns
df.head()


# In[60]:


df.dtypes


# In[61]:


df.shape


# In[62]:


df.describe


# In[63]:


#Review Counts by Age and Gender
df.groupby(['age', 'gender']).count()


# In[ ]:


#Research Question: Is there a change to readmissions when a medication change takes place? 


# In[64]:


#Review counts by age and changes to medication
df.groupby(['age', 'change']).count()


# In[65]:


#Create new data fram --- age group > medication change 'Yes' > -readmission within 30 Days vs no medicaiton change > readmission within 30 days


# In[66]:


df2 = df[['encounter_id', 'patient_nbr', 'age', 'change', 'time_in_hospital', 'readmitted']]


# In[67]:


df2.head()


# In[68]:


df2.groupby(['age', 'change']).count().plot(kind='bar')


# In[69]:


df3 = df2[['age', 'change', 'readmitted']]


# In[70]:


#Count of Readmissions related to age and change in medication
df3.groupby(['age', 'change']).count()


# In[71]:


df3.groupby(['age', 'readmitted']).count()


# In[72]:


df3.groupby(['age']).count()


# In[74]:


sns.displot(df3['change'])


# In[75]:


sns.displot(x=df3['change'], y=df3['age'])


# In[76]:


sns.displot(x=df3['change'], y=df3['readmitted'])


# In[77]:


df4 = df3.loc[(df3.age == '[40-50)')]


# In[93]:


df4.groupby(['age', 'change']).count()


# In[92]:


df4.groupby(['age', 'change']).count().plot(kind='bar')


# In[84]:


df5 = df4.loc[(df3.age == '[60-70)')]


# In[94]:


df5.groupby(['age', 'change']).count()


# In[91]:


df5.groupby(['age', 'change']).count().plot(kind='bar')


# In[95]:


df3.groupby(['age', 'change']).count().plot(kind='bar')


# In[82]:


# In summary there is a slight decrease in re-admissions when a medication change takes place during visit. 


# In[ ]:




