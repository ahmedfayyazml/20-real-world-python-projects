import streamlit as st  #run streamlit run main.py in the terminal to run the app
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:", placeholder="London")

days = st.slider("Forecast Days:", max_value=5, min_value=1,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")
def get_data():



d,t = get_data(place,days,option)

figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature(C)"})
st.plotly_chart(figure)
