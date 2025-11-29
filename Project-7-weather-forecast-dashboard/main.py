import  streamlit as st #run streamlit run main.py in the terminal to run the app
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:",placeholder="London")

days = st.slider("Forecast Days:",max_value=5,min_value=1,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} in {place}")

dates = ["2025-10-23","2025-10-24","2025-10-25","2025-10-26","2025-10-27"]

temperature = [10,11,14,13,15]
temperature = [days *i for i in temperature]
figure = px.line(x=dates,y=temperature,labels={'x':"Date",'y':"Temperature(C)"})

st.plotly_chart(figure)