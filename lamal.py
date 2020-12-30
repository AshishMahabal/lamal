import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("LA Marathi Authors' Literameet (LAMAL)")
st.sidebar.title("LAMAL")

"LA Marathi Authors' Literameet (LAMAL) is a group in Greater Los Angeles Area \
that meets every two months to read together Marathi writing done in the \
previous period, generally on a given topic."

lamalarts = pd.read_csv("lamalart_20201025.csv")

toDisplay = st.sidebar.radio(
	"What would you like to see?",
	["All articles", "By author", "By topic"],
	index=0
)

if toDisplay == "By author":
	author = st.sidebar.selectbox(
		'Select by Author',
		lamalarts['Author'].unique())	
	numart = len(lamalarts[lamalarts['Author']==author])
	'You selected Author:',author,' (',numart,' contributions)'
	lamalarts[lamalarts['Author']==author][['Topic','Title','Host','Month','Year']]	
elif toDisplay == "By topic":
	topic = st.sidebar.selectbox(
		'Select by Topic',
		lamalarts['Topic'].unique())
	numsub = len(lamalarts[lamalarts['Topic']==topic])
	'You selected Topic:', topic, '(',\
	'Host: ', lamalarts[lamalarts['Topic']==topic]['Host'].iloc[0],\
	'Epoch: ', lamalarts[lamalarts['Topic']==topic]['Month'].iloc[0],\
	'/',lamalarts[lamalarts['Topic']==topic]['Year'].iloc[0],\
	')',\
	numsub,' submission(s)'
	lamalarts[lamalarts['Topic']==topic][['Author','Title']]
else:
	if st.checkbox('Show top authors',value=True):
			fig, ax = plt.subplots()
			lamalarts['Author'].value_counts()[:10].plot.bar()
			st.pyplot(fig)
	if st.checkbox('Show top topics'):
			fig, ax = plt.subplots()
			lamalarts['Topic'].value_counts()[:10].plot.bar()
			st.pyplot(fig)
	"Here are the articles so far ..."
	lamalarts[['Topic','Author','Title']]