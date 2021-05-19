#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pandas as pd
import numpy as np
from ipywidgets import interact
import matplotlib.pyplot as plt


# In[73]:


df=pd.read_csv('http://gddatalabs.com/Tests/DS/NSE-TATAGLOBAL.csv')
df.head(1)


# In[74]:


dt=df.describe()


# In[75]:


dt


# In[76]:


df.describe(include='object')


# In[77]:


df.describe(include='all')


# In[78]:


df.info()


# In[79]:


df1=pd.DataFrame({'Val-1':[10,20, np.nan, 20, np.nan],
             'Val-2':[10,20,30,50,np.nan]})


# In[80]:


df1.info()


# In[81]:


df1.describe()


# In[82]:


df1.corr()


# In[83]:


df.corr()


# In[84]:


df.corr()['Turnover (Lacs)'].sort_values()


# In[85]:


df['Date']= pd.to_datetime(df['Date'])


# In[86]:


df.groupby([df['Date'].dt.month, df['Date'].dt.day])['High'].mean()


# In[87]:


df['Days']= df['Date'].dt.day
df['Months']=df['Date'].dt.month


# In[88]:


df.head(1)


# In[89]:


dtmean=df.groupby(['Months','Days'])['Open','High','Low','Last','Close'].mean()


# In[90]:


dtmin=df.groupby(['Months','Days'])['Open','High','Low','Last','Close'].min()


# In[91]:


dtmax=df.groupby(['Months','Days'])['Open','High','Low','Last','Close'].max()


# In[92]:


dtmean[['Open','Close']].plot()


# In[93]:


dtmean.head().plot()


# In[94]:


dtmean.tail()


# In[95]:


df['years']=df['Date'].dt.year


# In[96]:


df.head(1)


# In[97]:


#Add option of choosing years from list of dropdown and show Pivot summary & Data
#Visualization

def getsummary(year, col_name):
    print('Show Pivot for Year {0} and Columns {1}'.format(year, col_name))
    dfa=df[df['years']==year]
    dt=pd.pivot_table(dfa, index='Months', columns='Days',
                  values=col_name, 
                  aggfunc='mean', fill_value=0)
    return dt


# In[98]:


df['years'].unique()


# In[99]:


df.columns


# In[100]:


# getsummary(2018, 'Close')


# In[101]:


interact(getsummary, year=df['years'].unique(), col_name=['Open', 'High', 'Low', 'Last', 'Close'])


# In[108]:


df['Weeks']=df['Date'].dt.weekday_name


# In[109]:


def getsummary(year, col_name):
    print('Show Pivot for Year {0} and Columns {1}'.format(year, col_name))
    dfa=df[df['years']==year]
    dt=pd.pivot_table(dfa, index='Months', columns='Weeks',
                  values=col_name, 
                  aggfunc='mean', fill_value=0)
    return dt


# In[110]:


interact(getsummary, year=df['years'].unique(), 
         col_name=['Open', 'High', 'Low', 'Last', 'Close'])


# In[141]:


df['Weeks'].unique()


# In[116]:


getsummary(2018,'High').loc[:,['Monday','Tuesday','Wednesday','Thursday','Friday']]


# In[117]:


# Create Pivot & Data Visualization to show Year & Month wise High & Low value of stock


# In[118]:


dt=df.groupby(['years','Months'])['Close'].agg([min, max])


# In[119]:


dt1=df.groupby(['years','Months'])['High','Low'].mean()


# In[120]:


dt.plot()


# In[121]:


dt1.plot()


# In[122]:


#Create Pivot & Data visualization to show Year, Month & Day wise Turnover amount, and indicate the high & low turnover 
#points
dt=df.groupby(['years','Months', 'Days'])['Turnover (Lacs)'].agg([min,max])
dt.head(1)


# In[123]:


dt=df.groupby(['years','Months', 'Days'])['Turnover (Lacs)'].mean()
dt


# In[124]:


dt.head(20).plot()


# In[125]:


sr=dt.head(20)


# In[126]:


sr.sort_values().head(1)


# In[127]:


sr.sort_values().tail(1)


# In[128]:


srmin= sr.sort_values().head(1)
a=srmin.index.tolist()[0]
xmin= str(a[0])+"-"+str(a[1])+"-"+str(a[2])
xmin


# In[129]:


srmax= sr.sort_values().tail(1)
a=srmax.index.tolist()[0]
xmax= str(a[0])+"-"+str(a[1])+"-"+str(a[2])
xmax


# In[130]:



x=[ str(a[0])+"-"+str(a[1])+"-"+str(a[2]) for a in  sr.index]


# In[132]:


plt.bar(x, sr.values, label='Sales')
plt.bar(xmin, srmin.values, label='Min Sales')
plt.bar(xmax, srmax.values, label='Max Sales')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[133]:


#Analyze whether high fluctuation in open & closing value of stock is impacting the Total Trade
#Quantity or not.


# In[134]:


df.head(1)


# In[136]:


df['Var']= df['Close']-df['Open']
df.head(1)


# In[137]:


df[['Var','Total Trade Quantity']].corr()


# In[138]:


df.groupby(['years'])['Var','Total Trade Quantity'].mean().corr()


# In[139]:


plt.plot(df['Date'], df['Turnover (Lacs)'])


# In[140]:


fig, (a1, a2,a3,a4) = plt.subplots(4,1)
dt=df.groupby('years')['Turnover (Lacs)'].mean()
a1.plot(dt.index, dt.values)
dt=df.groupby('Months')['Turnover (Lacs)'].mean()
a2.plot(dt.index, dt.values)
dt=df.groupby('Days')['Turnover (Lacs)'].mean()
a3.plot(dt.index, dt.values)
a4.plot(df['Date'], df['Turnover (Lacs)'])


# In[ ]:




