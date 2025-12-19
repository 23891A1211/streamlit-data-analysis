import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Tips Dataset Explorer", layout="wide")

st.title("📊 Tips Dataset Analysis")
st.markdown("This app explores the Seaborn 'tips' dataset, converted from your Jupyter Notebook.")

# 1. Data Loading (Caching for performance)
@st.cache_data
def load_data():
    return sns.load_dataset("tips")

df = load_data()

# 2. Sidebar - Data Overview
st.sidebar.header("Data Settings")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Dataset")
    st.write(df)

# 3. Basic Info Section (from df.shape and df.columns)
st.header("1. Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.write("**Column Names:**")
col3.write(", ".join(df.columns.tolist()))

# 4. Descriptive Statistics (from df.describe())
st.header("2. Descriptive Statistics")
st.write(df.describe())

# 5. Visualizations (Expanded from the notebook's intent)
st.header("3. Data Visualization")

chart_type = st.selectbox("Select Chart Type", 
                          ["Scatter Plot (Total Bill vs Tip)", 
                           "Box Plot (Day vs Total Bill)", 
                           "Distribution of Tips"])

fig, ax = plt.subplots()

if chart_type == "Scatter Plot (Total Bill vs Tip)":
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="smoker", ax=ax)
    st.pyplot(fig)

elif chart_type == "Box Plot (Day vs Total Bill)":
    sns.boxplot(data=df, x="day", y="total_bill", hue="time", ax=ax)
    st.pyplot(fig)

elif chart_type == "Distribution of Tips":
    sns.histplot(df["tip"], kde=True, ax=ax)
    st.pyplot(fig)

# 6. Data Filtering Interactive Feature
st.header("4. Filter Data")
selected_day = st.multiselect("Filter by Day", options=df['day'].unique(), default=df['day'].unique())
filtered_df = df[df['day'].isin(selected_day)]
st.dataframe(filtered_df)
