#Aditya Seshadri- se24ucse012
#Q2 Simple Reflex Agent

def calculate_aqi(pm25, pm10):
    if pm25 <= 30 and pm10 <= 50:
        return "Good"
    elif pm25 <= 60 and pm10 <= 100:
        return "Moderate"
    elif pm25 <= 90 and pm10 <= 250:
        return "Poor"
    else:
        return "Hazardous"


def reflex_agent():
    sensor_data = {
        "PM2.5": 40,
        "PM10": 70
    }

    pm25 = sensor_data["PM2.5"]
    pm10 = sensor_data["PM10"]

    aqi = calculate_aqi(pm25, pm10)

    print("AQI Status:", aqi)


print("Running Simple Reflex Agent")
reflex_agent()
