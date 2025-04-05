
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd
import matplotlib.pyplot as plt

# Load weather data
weather_df = pd.read_csv("weather.csv")

# 1. Print first 10 rows of weather data
print("1) First 10 Rows of Weather Data:")
print(weather_df.head(10))

# 2. Find the maximum and minimum temperature
print("\n2) Max and Min Temperature:")
print("Maximum Temperature:", weather_df["temperature"].max())
print("Minimum Temperature:", weather_df["temperature"].min())

# 3. List the places with temperature less than 28°C
print("\n3) Places with Temperature < 28°C:")
print(weather_df[weather_df["temperature"] < 28]["place"].unique())

# 4. List the places with weather = “Cloudy”
print("\n4) Places with Cloudy Weather:")
print(weather_df[weather_df["weather"].str.lower() == "cloudy"]["place"].unique())

# 5. Sort and display each weather and its frequency
print("\n5) Weather Type Frequency:")
print(weather_df["weather"].value_counts())

# 6. Bar plot to visualize temperature of each day
plt.figure(figsize=(10, 6))
plt.bar(weather_df["date"], weather_df["temperature"], color='skyblue')
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Overview")
plt.tight_layout()
plt.grid(True)
plt.show()






