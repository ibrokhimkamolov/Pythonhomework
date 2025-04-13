from bs4 import BeautifulSoup

# Step 1: Load and Parse the HTML File
with open("/Users/ibrokhimkamolov/Documents/Analytics_Studies/Python/Pythonhomework/lesson-14/homework/weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Step 2: Extract Weather Forecast Data
weather_data = []
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append({
        "day": day,
        "temperature": temperature,
        "condition": condition
    })

# Step 3: Display Weather Data
print("5-Day Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Step 4: Find Specific Data
# a) Day(s) with the highest temperature
max_temp = max(entry["temperature"] for entry in weather_data)
hottest_days = [entry["day"] for entry in weather_data if entry["temperature"] == max_temp]

# b) Day(s) with "Sunny" condition
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]

print(f"\nDay(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")

# Step 5: Calculate Average Temperature
avg_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {avg_temp:.2f}°C")
