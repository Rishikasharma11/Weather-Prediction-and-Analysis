
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# -------------------------------------------------Stream Dataset---------------------------------------------------
# Load dataset
data = pd.read_csv("CleanedIndianWeatherRepository.csv")

# Title and Introduction
st.title("Weather Data Analysis Dashboard")
st.write("Explore key insights and trends from the Indian weather dataset.")

# Button to trigger the display
if st.button('Show Weather Data Insights'):
    # Dataset preview
    st.write("### Dataset Preview:")
    st.write(data)

    # Key statistics
    st.write("### Key Statistics")
    st.write(f"Minimum Temperature: {data['temperature_celsius'].min()} °C")
    st.write(f"Maximum Temperature: {data['temperature_celsius'].max()} °C")
    st.write(f"Average Humidity: {data['humidity'].mean()} %")

    # Summary
    st.write("### Summary")
    st.write("This dashboard provides key insights into temperature trends and weather patterns in India.")


data = pd.read_csv("CleanedIndianWeatherRepository.csv")
print(data)

# Minimum Temperatures of City in Celsius
minimum_temperature_c = data['temperature_celsius'].min()
minimum_temperature_in_celsius = data.loc[data['temperature_celsius'] == minimum_temperature_c, ('location_name', 'temperature_celsius')]
print("The coldest city in India is :\n", minimum_temperature_in_celsius)

# Maximum Temperatures of City in Celsius
maximum_temperature_c = data['temperature_celsius'].max()
maximum_temperature_in_celsius = data.loc[data['temperature_celsius'] == maximum_temperature_c, ('location_name', 'temperature_celsius')]
print("The warmest cities in India is :\n", maximum_temperature_in_celsius)

# Example data - replace with your actual minimum and maximum temperatures
minimum_temperature_in_celsius = pd.Series({'location_name': 'Kargil', 'temperature': -30.7})
maximum_temperature_in_celsius = pd.Series({'location_name': 'Bikaner', 'temperature': 38.3})

# ---------------------------------------------------Creating DataFrame using minimum and maximum temperatures-----------------------
temperature_celsius_df = pd.DataFrame({
    'City': [minimum_temperature_in_celsius['location_name'], maximum_temperature_in_celsius['location_name']],
    'Temperature in Celsius': [minimum_temperature_in_celsius['temperature'], maximum_temperature_in_celsius['temperature']]
})

# Plotting a line plot using Plotly
fig = px.line(temperature_celsius_df, x='City', y='Temperature in Celsius',
               title='Coldest and Warmest Cities in India',
               markers=True)

# Adding labels
fig.update_layout(xaxis_title='City', yaxis_title='Temperature (°C)',
                  template='plotly_dark')

# Show the plot
st.plotly_chart(fig)

fig = px.scatter(data, x='temperature_celsius', y='humidity',
                 title='Temperature vs. Humidity',
                 labels={'temperature_celsius': 'Temperature (°C)', 'humidity': 'Humidity (%)'})

# Show the plot
st.plotly_chart(fig)

avg_temp_by_region = data.groupby('region')['temperature_celsius'].mean().reset_index()

fig = px.bar(avg_temp_by_region, x='region', y='temperature_celsius',
             color = 'region',
             title='Average Temperature by Region',
             labels={'temperature_celsius': 'Average Temperature (°C)', 'region': 'Region'})

# Show the plot
st.plotly_chart(fig)

# Weather conditions distribution
weather_counts = data['condition_text'].value_counts().reset_index().head(7)
weather_counts.columns = ['Condition', 'Count']

# Plotting the pie chart for weather conditions
fig_weather = px.pie(weather_counts, names='Condition', values='Count',
                     title='Weather Conditions Distribution',
                     color_discrete_sequence=px.colors.sequential.RdBu)

# Show the plot
st.plotly_chart(fig_weather)

# Assuming you have a column called 'air_quality_category'
air_quality_counts = data['air_quality_Carbon_Monoxide'].value_counts().reset_index().head()
air_quality_counts.columns = ['Air Quality Category', 'Count']

# Plotting the pie chart for air quality categories
fig_air_quality = px.pie(air_quality_counts, names='Air Quality Category', values='Count',
                          title='Air Quality Categories Distribution',
                          color_discrete_sequence=px.colors.sequential.Greens)
st.plotly_chart(fig_air_quality)

# --------------------------------------scatter plot for Temperature vs. Humidity(Regions)----------------------------
fig_temp_humidity = px.scatter(data,
                                x='temperature_celsius',
                                y='humidity',
                                hover_name='region',
                                title='Temperature vs. Humidity',
                                labels={'temperature_celsius': 'Temperature (°C)',
                                        'humidity': 'Humidity (%)'},
                                color='region')

# Update layout for better readability
fig_temp_humidity.update_layout(template='plotly_dark')

# Show the plot
st.plotly_chart(fig_temp_humidity)

# --------------------------------------scatter plot for Temperature vs. Humidity(Cities)----------------------------
fig_temp_humidity = px.scatter(data,
                                x='temperature_celsius',
                                y='humidity',
                                hover_name='location_name',
                                title='Temperature vs. Humidity',
                                labels={'temperature_celsius': 'Temperature (°C)',
                                        'humidity': 'Humidity (%)'},
                                color='location_name')

# Update layout for better readability
fig_temp_humidity.update_layout(template='plotly_dark')

# Show the plot
st.plotly_chart(fig_temp_humidity)

# ---------------------------------scatter plot for Wind Speed vs. Visibility(Region)--------------------------------------------------------------
fig_wind_visibility = px.scatter(data,
                                  x='wind_kph',
                                  y='visibility_km',
                                  hover_name='region',
                                  title='Wind Speed vs. Visibility',
                                  labels={'wind_kph': 'Wind Speed (kph)',
                                          'visibility_km': 'Visibility (km)'},
                                  color='region')

# Update layout for better readability
fig_wind_visibility.update_layout(template='plotly_dark')

# Show the plot
st.plotly_chart(fig_wind_visibility)
