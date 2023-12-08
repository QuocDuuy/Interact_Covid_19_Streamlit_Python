#!/usr/bin/env python
# coding: utf-8

# # Implementation

# ### a. Importing Libraries

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# ### b. Importing the dataset

# In[2]:


df = pd.read_csv("C:/Users/ACER/Interactive_COVID-19_Dashboard_Streamlit_Python-main/database/district_wise.csv")


# # Starting with setting the title and the sidebar title for streamlit dashboard

# In[3]:


st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title('Visualization Selector')
st.sidebar.markdown("Select the Charts/Plots accordingly:")


# ### a. Visualization (part-1: using bar chart and pie chart

# In[4]:


select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox('Hide', True, key='1'):
    if select == 'Pie chart':
        st.title('Selected top 5 cities')
        fig = px.pie(df, values=df['Confirmed'][:5], names=df['State'][:5], title='Total Confirmed Cases')
        st.plotly_chart(fig)
    if select == 'Bar plot':
        st.title('Selected top 5 cities')
        fig = go.Figure(data=[go.Bar(name='Confirmed', x=df['State'][:5], y=df['Confirmed'][:5]), go.Bar(name='Recovered', x=df['State'][:5], y=df['Recovered'][:5]), go.Bar(name='Active', x=df['State'][:5], y=df['Active'][:5])])
        st.plotly_chart(fig)


# ### b. Visualization (part-2: active and confirmed cases on time series)

# In[5]:


df2 = pd.read_csv('C:/Users/ACER/Interactive_COVID-19_Dashboard_Streamlit_Python-main/database/case_time_series.csv')
df2['Date'] = df2['Date'].astype('datetime64[ns]')
select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='2')
if not st.sidebar.checkbox('Hide', True, key='2'):
    if select1 == 'Confirmed':
        fig = px.line(df2, x='Date', y='Cases')
        st.plotly_chart(fig)
    elif select1 == 'Recovered':
        fig = px.line(df2, x='Date', y='Recovered')
        st.plotly_chart(fig)


# ### c. Visualization (part-3: Area Charts)

# In[6]:


select2 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='3')
if not st.sidebar.checkbox('Hide', True, key='3'):
    if select2 == 'Confirmed':
        fig = px.area(df2, x="Date", y='Cases')
        st.plotly_chart(fig)
    elif select2 == 'Recovered':
        fig = px.area(df2, x='Date', y='Recovered')
        st.plotly_chart(fig)

