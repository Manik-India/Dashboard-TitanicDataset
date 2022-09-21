#importing libraries

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title=" Survival Rate Prediction", page_icon="🚢",
layout="wide")

@st.cache   #so that read_data() run once
def read_data():
    df = pd.read_csv("dataset.csv")
    return df

df = read_data()

st.title("🚢 Analysis on Titanic Dataset\n Analysed by: Manik")
st.markdown("##")


left_column, middle_column, right_column = st.columns(3)
# showing data in left col
# Number of Fist class Passenger Survived
# Number of Second class Passenger Survived
# Number of Second class Passenger Survived
with left_column:
   st.caption(f"First class Passenger Deaths: {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 0)])}")
   st.caption(f"Second class Passenger Deaths:{len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 0)])}")
   st.caption(f"Third class Passenger Deaths: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 0)])}")
# showing data in middle col
# Number of Fist class Passenger Deaths
# Number of Second class Passenger Deaths
# Number of Third class Passenger Deaths
with middle_column:
   st.caption(f"First class Passenger Survived : {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 1)])}")
   st.caption(f"Second class Passenger Survived: {len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 1)])}")
   st.caption(f"Third class Passenger Survived: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 1)])}")
# showing data in right col
# Average Fare Value
# Average Fare Tax
# Average Luggage Charges Value
with right_column:
   st.caption(f"Average Fare Value: {int(df['Fare'].mean())}")
   st.caption(f"Average Fare Tax : {int(df['Fare_Tax'].mean())}")
   st.caption(f"Average Luggage Charges Value: {int(df['Luggage Charges'].mean())}")

pie_chart = px.pie(names = df["Embarked"].unique(),
values=df.groupby("Embarked")["Embarked"].count(),hole=0.5)

box_plot = px.box(df, y="Age",x="Pclass")

group_plot = px.histogram(df, x="Survived", color="Pclass",barmode='group') 
    
st.markdown('---')


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Passenger belonging to Embarked % (Pie Chart)")
with middle_column:
    st.subheader("Survival Histogram based on Pclass")
with right_column:
    st.subheader("Box plot Based on Pclass vs age")

st.markdown("---")

left_column.plotly_chart(pie_chart,use_container_width=True)

right_column.plotly_chart(box_plot,use_container_width=True)

middle_column.plotly_chart(group_plot,use_container_width=True)

line_plot = px.line(df,x="Fare",y=["Fare_Tax","Luggage Charges", "Food Charges"])

plot = px.histogram(df, x="SibSp",color="Sex",barmode='group') 

pie_chart1 = px.pie(names = df["Survived"].unique(),values=df.groupby("Survived")["Survived"].count(),hole=0.5)


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader(" Survival Rate %(Pie Chart)")
with middle_column:
    st.subheader(" Histogram Based on sibsp")
with right_column:
    st.subheader(" Line plot for Fare_Tax,Luggage Charges, Food Charges")

st.markdown("---")

left_column.plotly_chart(pie_chart1,use_container_width=True)

middle_column.plotly_chart(plot,use_container_width=True)

right_column.plotly_chart(line_plot,use_container_width=True)

left_column, middle_column, right_column = st.columns(3)

group_plot1 = px.histogram(df, x="Survived", color="Sex", barmode='group')
with middle_column:
    st.subheader("Survival Histogram of Sex")
middle_column.plotly_chart(group_plot1, use_container_width=True)