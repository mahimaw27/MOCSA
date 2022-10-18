import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)

# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Scatter Plot'])


# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()
