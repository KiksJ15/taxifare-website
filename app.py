import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

start_date = st.date_input('Insert a date', value=datetime.datetime(2019,7,6))
start_time = st.time_input('Insert a time', datetime.time(8, 45))
date_and_time = datetime.datetime.combine(start_date, start_time)

pickup_longitude = st.number_input('Insert a pickup longitude')

pickup_latitude = st.number_input('Insert a pickup latitude')

dropoff_longitude = st.number_input('Insert a dropoff longitude')

dropoff_latitude = st.number_input('Insert a dropoff latitude')

passenger_count = st.number_input('Insert a passenger count')



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = "https://taxifare-605719025671.europe-west1.run.app/predict?"

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

dictionaire_request_api = {
    "pickup_datetime": date_and_time,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude":pickup_latitude,
    "dropoff_longitude":dropoff_longitude,
    "dropoff_latitude":dropoff_latitude,
    "passenger_count":passenger_count,
    }


response = requests.get(url,dictionaire_request_api)

response = response.json().get("fare")

response
