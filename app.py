import streamlit as st
import requests
import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

#'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger_count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
#'''
default_datetime = datetime.datetime.now()

# Create a datetime input widget
date_time = st.datetime_input(
    "On which date and time do you want to take the ride?",
    default_datetime)

pickup_longitude = st.number_input('Insert the pickup longitude')

pickup_latitude = st.number_input('Insert the pickup latitude')

dropoff_longitude = st.number_input('Insert the dropoff longitude')

dropoff_latitude = st.number_input('Insert the dropoff latitude')

passenger_count = st.slider('total number of passengers from 1-10',1,10)

def get_map_data():
    data = {
        "lat": [pickup_latitude, dropoff_latitude],
        "lon": [pickup_longitude, dropoff_longitude]
    }
    return pd.DataFrame(data)

# Generate data
df = get_map_data()

# Display map with the two points
st.map(df)

#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''
url = 'https://taxifare-1038167476274.europe-west1.run.app/predict?'

params = {
    "date_time": date_time,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}
output = requests.get(url, params=params)

st.write(f'Your fare will be: {output}')
