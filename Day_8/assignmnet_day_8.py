# Question-11:
# Weather mock API 
# format comes from below endpoint 
    # Parse format, if xml, show xml, 
    # if none, show json 
    # Put all random temp 
    # City name may change based on PATH param 
    # (currently not implemented in demo api endpoint)

#urls
#http://localhost:5000/weather/Delhi
#http://localhost:5000/weather/Delhi?format=xml
#http://localhost:5000/weather/Delhi?date=18-04-2025
#http://localhost:5000/weather/Delhi?format=xml&date=18-04-2025
    
from flask import Flask, request, Response, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_forecast_data(city_list, num_days=100):
    weather_types = ["Sunny", "Cloudy", "Partly Cloudy", "Mostly Sunny", "Windy", "Clear Sky", "Breezy"]
    result = {}

    start_date = datetime.strptime("17-04-2025", "%d-%m-%Y")

    for city in city_list:
        forecast_list = []
        current_date = start_date

        for _ in range(num_days):
            date_str = current_date.strftime("%d-%B-%Y")
            day_name = current_date.strftime("%a")
            high = random.randint(25, 45)
            low = random.randint(10, high)
            humidity = random.randint(25, 45)
            rain_chances = random.randint(10, 40)

            forecast_list.append({
                "date": date_str,
                "day": day_name,
                "high_temp": high,
                "low_temp": low,
                "humidity": humidity,
                "rain_chances": rain_chances,
                "text": random.choice(weather_types),
                "code": random.randint(20, 50)
            })
            current_date += timedelta(days=1)
          
        result[city] = {
            "forecast": forecast_list
        }

    return result

def convert_to_xml(data):
    xml_output = "<forecast>"
    for item in data:
        xml_output += "<day>"
        for key, value in item.items():
            xml_output += f"<{key}>{value}</{key}>"
        xml_output += "</day>"
    xml_output += "</forecast>"
    return xml_output

Cities = ["Mumbai", "Chennai", "Hyderabad", "Bengaluru", "Pune", "Delhi","Vizag","Kochi","Jaipur","Lucknow"]
forecast_result = generate_forecast_data(Cities)

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    format_type = request.args.get('format', 'json').lower()
    target_date = request.args.get('date')  

    if city not in forecast_result:
        return jsonify({"error": f"No data available for city: {city}"}), 404

    forecast_data = forecast_result[city]['forecast']

    if target_date:
        try:
            target_date_formatted = datetime.strptime(target_date, "%d-%m-%Y").strftime("%d-%B-%Y")
            single_day = next((item for item in forecast_data if item["date"] == target_date_formatted), None)

            if not single_day:
                return jsonify({"error": f"No forecast data found for {city} on {target_date}"}), 404

            if format_type == "xml":
                xml_data = convert_to_xml([single_day])
                return Response(xml_data, mimetype='application/xml', status=200)

            return jsonify({city: {"forecast": [single_day]}})

        except ValueError:
            return jsonify({"error": "Invalid date format. Use DD-MM-YYYY."}), 400

    if format_type == "xml":
        xml_data = convert_to_xml(forecast_data)
        return Response(xml_data, mimetype='application/xml', status=200)

    return jsonify({city: {"forecast": forecast_data}})


if __name__ == '__main__':
    app.run()
