import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("LA Marathi Authors' Literameet (LAMAL)")

"LA Marathi Authors' Literameet (LAMAL) is a group in Greater Los Angeles Area \
that meets every two months to read together Marathi writing done in the \
previous period, generally on a given topic"

"Here are the articles so far ..."
lamalarts = pd.read_csv("lamalart_20201025.csv")
lamalarts[['Topic','Author','Title']]

if st.checkbox('Show top authors'):
	fig, ax = plt.subplots()
	lamalarts['Author'].value_counts()[:10].plot.bar()
	st.pyplot(fig)

if st.checkbox('Show top topics'):
	fig, ax = plt.subplots()
	lamalarts['Topic'].value_counts()[:10].plot.bar()
	st.pyplot(fig)

author = st.sidebar.selectbox(
    'Select by Author',
     lamalarts['Author'].unique())

'You selected Author:',author 
lamalarts[lamalarts['Author']==author][['Topic','Title','Host']]

topic = st.sidebar.selectbox(
    'Select by Topic',
     lamalarts['Topic'].unique())

'You selected Topic:', topic, '(Host: ', lamalarts[lamalarts['Topic']==topic]['Host'].iloc[0],')'
lamalarts[lamalarts['Topic']==topic][['Author','Title','Host']]

