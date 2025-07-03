# IoT ESP32 Temperature & Humidity Monitor Using Flask, StreamLit & Arduino IDE

This project utilises an ESP32 microcontroller with a DHT11 sensor to monitor temperature and humidity levels. The data is sent to a Flask server for logging, then a StreamLit web app does analysis and visualisation.

## Contents
- [Documentation](#Documentation)
  - [🧰 Hardware Components](#Hardware-Components)
  - [🔌 Wiring Diagram](#Wiring-Diagram)
- [🚀 Installation & Setup Guide](#Installation-and-Setup-Guide)
- [🧠 Software Architecture Diagram](#Software-Architecture-Diagram)

---

## Documentation
Full setup documentation on the ESP32, Flask Server & StreamLit setup is available here.
- ESP32
- Flask Server
- StreamLit
- [File Structure](#dirtectory-file-structure)
  - StreamLit Web App
  - Flask

##  Hardware Components

- ESP32 Development Board
- DHT11 Temperature and Humidity Sensor
- 10kΩ Resistor
- Breadboard and Jumper Wires

## Wiring Diagram
### Connect the components as follows:

- DHT11 VCC → 3.3V on ESP32
- DHT11 GND → GND on ESP32
- DHT11 Data → GPIO15 on ESP32
- Place a 10kΩ resistor between the Data and VCC lines of the DHT11 sensor.

_File: circuit.svg_
![Circuit Diagram](https://github.com/DanTheProgrammerMan/IoT-Project-Hydroponics-ESP32/blob/main/circuit.svg)


## Installation and Setup Guide
### Prerequisites
- Python 3.7 or higher
- Arduino IDE configured for ESP32 development
- Required Python libraries:
  - Flask
  - Streamlit
  - Pandas
- Install: `py -m pip install flask`

### Setup Guide
### 1. ESP32 Setup:
1. Connect the DHT11 sensor to the ESP32 as per the wiring diagram.
2. Open the Arduino IDE and install the necessary libraries:
  - `DHT sensor library`
  - `esp32 by Espressif Systems`
  - `Adafruit Sensor`
3. Upload the provided Arduino code to the ESP32.

### 2. Flask Server Setup:
1. Navigate to the flask_server directory.
2. Install dependencies:
  - `py -m pip install flask pandas`
  - `py -m pip install pandas`
3. Run the Flask server:
  - `python flask_server.py`

> [!NOTE]
> Ensure your Flask server is running and accessible at the specified IP address.

### 3. Streamlit Application Setup:
1. Navigate to the streamlit_app directory.
2. Install dependencies:
  - `py -m pip install streamlit pandas`
3. Run the Streamlit app:
  - `streamlit run app.py`

> [!NOTE]
> Ensure that the Flask server is running before starting the ESP32, otherwise you will receive data from the ESP32 where the uptime has all already started.
> **Debug/Testing:** Monitor the serial output for sensor readings and HTTP response codes.

---

## Software Architecture Diagram
### The system architecture consists of three main components:

#### ESP32 Microcontroller:

- Reads data from the DHT11 sensor.

- Connects to Wi-Fi and sends HTTP POST requests containing the sensor data to the Flask server.

#### Flask Server:

- Receives data from the ESP32.

- Appends the received data to a CSV file for storage.

#### Streamlit Web Application:

- Reads the CSV file periodically.

- Displays real-time graphs and statistics based on the sensor data.

## Visual Representation:

![Circuit Diagram](https://github.com/DanTheProgrammerMan/IoT-Project-Hydroponics-ESP32/blob/main/Software-Architecture-Diagram_IoT.png)

---

## Dirtectory File Structure
Organise your project as follows. Adjust paths in your code if your Flask server is located outside the shown structure.

```plaintext
your-project/
├── flask_server/            ← Flask server code & data storage  
│   ├── app.py               ← Flask application    
│   └── data.csv             ← Stored sensor readings  
│
├── streamlit_app/                 ← Streamlit application
│   ├── main_dashboard.py          ← Main dashboard (entrypoint) implementation (menus, scripts)
│   ├── home_page.py               ← Home page layout  
│   ├── analytics_page.py          ← Analytics overview page
│   ├── view_footage_list.py       ← Video footage list viewer
│   ├── uptime_live.py             ← Live uptime monitor  
│   ├── utils.py                   ← Helper functions and utilities  
│   ├── data/                      
│   │   └── data.csv               ← Symlink or copy of `../flask_server/data.csv`  
│   ├── images/                    ← Images used in the Streamlit app  
│   └── styles/                    ← CSS styles for the Streamlit app
│
├── README.md                ← Project documentation  
└── .gitignore    
```
> ![NOTE]
> `main_dashboard.py` refers to `IoT_Project-1_Dashboard_v1_FINAL.py` | `analytics_page.py` refers to `analytics_overview.py`

---

## 📊 Live Dashboard
The Streamlit web application provides real-time visualisations of the temperature & humidity data collected by the ESP32.

| Feature   | Description         |
|-----------|---------------------|
| Fast      | Loads quickly       |
| Reliable  | Consistent results  |

## 📄 License

This project is licensed under the MIT License.
