import psycopg2
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(
    page_title="Red Bus",
    page_icon="C:/Users/MUGILAN/Downloads/download.png.png"  
)

st.markdown("""
    <h1 style='text-align: center; color: red;'>
    <i>RED BUS</i>
    </h1>
    """, unsafe_allow_html=True)

# Display images
st.image("C:/Users/MUGILAN/Downloads/download.png.png", use_column_width=True)


st.markdown("<h2 style='text-align: center;'>State Road Transport Corporation (SRTC) of India</h1>", unsafe_allow_html=True)

# Bus service names with full forms
bus_details = [
    'APSRTC - Andhra Pradesh State Road Transport Corporation',
    'ASTC - Assam State Transport Corporation',
    'BSRTC - Bihar state road transport corporation',
    'HRTC - Himachal Road Transport Corporation',
    'KSRTC - Kerala State Road Transport Corporation',
    'WBSTC - West Bengal State Transport Corporation',
    'RSRTC - Rajasthan State Road Transport Corporation',
    'PEPSU - Patiala and East Punjab States Union Buses',
    'TSRTC - Telangana State Road Transport Corporation',
    'UPSRTC - Uttar Pradesh State Road Transport Corporation'
]
st.write(bus_details)

# Define your connection parameters
connection = psycopg2.connect(
            user="postgres",  # Replace with your PostgreSQL username
            password="Mugi2004",  # Replace with your PostgreSQL password
            port="5432",  # Replace with your PostgreSQL port
            database="postgres"  # Replace with your PostgreSQL database name
        )
# Use pandas to execute a query
query = "select * from bus_details"
df = pd.read_sql(query, connection)

# Display the data using Streamlit
st.write(df)

# Close the connection when done
connection.close()

with st.sidebar:
    Menu=st.sidebar.selectbox(":red[_**Please Select The state:-**_]",("APSRTC - Andhra Pradesh State Road Transport Corporation", "ASTC - Assam State Transport Corporation", "HRTC - Himachal Pradesh Road Transport Corporation","KSRTC - Kerala State Road Transport Corporation","WBSTC - West Bengal State Transport Corporation","RSRTC - Rajasthan State Road Transport Corporation","TSRTC - Telangana State Road Transport Corporation","UPSRTC - Uttar Pradesh State Road Transport Corporation"))

if Menu == "APSRTC - Andhra Pradesh State Road Transport Corporation":

    st.header("Current Bus Schedules of Andhra Pradesh Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")

elif Menu == "ASTC - Assam State Transport Corporation":

    st.header("Current Bus Schedules of Assam Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile")

elif Menu == "HRTC - Himachal Pradesh Road Transport Corporation":

    st.header("Current Bus Schedules of Himachal Pradesh Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile")

elif Menu == "KSRTC - Kerala State Road Transport Corporation":

    st.header("Current Bus Schedules of Kerala Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile")

elif Menu == "BSRTC - Bihar state road transport corporation":

    st.header("Current Bus Schedules of Bihar Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/bihar-state-road-transport-corporation-bsrtc/?utm_source=rtchometile")

elif Menu == "PEPSU - Patiala and East Punjab States Union Buses":

    st.header("Current Bus Schedules of Punjab Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/pepsu/?utm_source=rtchometile")

elif Menu == "WBSTC - West Bengal State Transport Corporation":

    st.header("Current Bus Schedules of West Bengal Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile")

elif Menu == "RSRTC - Rajasthan State Road Transport Corporation":

    st.header("Current Bus Schedules Rajasthan of Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile")

elif Menu == "TSRTC - Telangana State Road Transport Corporation":

    st.header("Current Bus Schedules Telangana of Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile")

elif Menu == "UPSRTC - Uttar Pradesh State Road Transport Corporation":

    st.header("Current Bus Schedules Uttar Pradesh of Transportation")
    st.subheader(":orange[click the link to book your bus tickets now !]")

    st.write("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile")



