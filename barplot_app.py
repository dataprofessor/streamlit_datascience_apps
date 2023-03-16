# Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# App title
st.title('📊🐼 Plots with Pandas')

# Read CSV data
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
df['MolWt_class'] = pd.Series(['small' if x < 300 else 'large' for x in df['MolWt']])
df = df.groupby('MolWt_class').mean()

# Select columns to plot
selected_columns = st.multiselect('Select columns', list(df.columns), list(df.columns))
xlabel = st.text_input('Enter X label')
ylabel = st.text_input('Enter Y label')

# Create bar plot
fig, ax = plt.subplots()
df[selected_columns].plot.bar(ax=ax)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Display plot
st.pyplot(fig)

# Display DataFrame
with st.expander('Show Original DataFrame'):
    st.write(df)

with st.expander('Show Updated DataFrame'):
    st.write(df[selected_columns])
