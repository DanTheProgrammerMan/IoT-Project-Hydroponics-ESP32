from flask import Flask, request
import csv
import json
from datetime import datetime, timezone
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'sensor_data.csv')
JSON_FILE = os.path.join(BASE_DIR, 'sensor_data.json')

# Check if the CSV file exists with headers and is empty
if not os.path.exists(CSV_FILE): # or os.path.getsize(CSV_FILE) == 0:
    try:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'temperature', 'humidity', 'uptime'])
    except Exception as e:
        print(f"Error writing to CSV: {e}")


@app.route('/data', methods=['POST', 'GET'])
def receive_data():
    data = request.get_json()

    # Debugging to see if data is right or errors
    print(data)

    if data:
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        uptime = data.get('uptime')


        # Generate current timestamp for each request
        dt = datetime.now(timezone.utc).astimezone() # IMPORTANT TO HAVE IT HERE AND NOT ANYWHERE ELSE
        timestamp = dt.strftime('%H:%M:%S, %d-%m-%Y %z') # SELFNOTE: ISOFORAMT (ISO8601) is probably better for longterm
        timestamp = f"{timestamp[:-2]}:{timestamp[-2:]}"

        # Append to CSV
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temperature, humidity, uptime])

        # Append to JSON
        entry = {
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity,
            'uptime': uptime
        }

        # Load existing data
        try:
            with open(JSON_FILE, 'r') as f:
                try:
                    json_data = json.load(f)
                except json.JSONDecodeError:
                    json_data = []
        except FileNotFoundError:
            json_data = []

        json_data.append(entry)

        try:
            with open(JSON_FILE, 'w') as f:
                json.dump(json_data, f, indent=4)
        except IOError as e:
            print(f"Error writing to {JSON_FILE}: {e}")

        return 'Data received', 200
    else:
        return 'No data received', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
