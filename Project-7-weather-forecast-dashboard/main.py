import  streamlit as st
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:",placeholder="London")
days = st.slider("Forecast Days:",max_value=5,min_value=1,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} in {place}")