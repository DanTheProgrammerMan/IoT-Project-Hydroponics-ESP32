# IoT ESP32 Temperature & Humidity Monitor Using Flask, StreamLit & Arduino IDE

This project utilises an ESP32 microcontroller with a DHT11 sensor to monitor temperature and humidity levels. The data is sent to a Flask server for logging, then a StreamLit web app does analysis and visualisation.

## Contents
- [Documentation](#Documentation)
  - [🧰 Hardware Components](#Hardware-Components)
  - [🔌 Wiring Diagram](#Wiring-Diagram)
  - [🧠 Software Architecture Diagram](#Software-Architecture-Diagram)
- [🚀 Installation & Setup Guide](#Installation-&-Setup-Guide)
- [🔐Security Considerations](#Security-Considerations)

| Feature   | Description         |
|-----------|---------------------|
| Fast      | Loads quickly       |
| Reliable  | Consistent results  |

```python
def hello_world():
    print("Hello, world!")
```

## Documentation
Full setup documentation on the ESP32, Flask Server & StreamLit setup is available here.
- ESP32
- Flask Server
- StreamLit

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

Insert wiring diagram image here
![Circuit Diagram](images/circuit_diagram.png)


## Installation & Setup Guide
### Prerequisites
- Python 3.7 or higher
- Arduino IDE configured for ESP32 development
- Required Python libraries:
  - Flask
  - Streamlit
  - Pandas

### Setup Guide
### 1. ESP32 Setup:
1. Connect the DHT11 sensor to the ESP32 as per the wiring diagram.
2. Open the Arduino IDE and install the necessary libraries:
  - `DHT sensor library`
  - `Adafruit Unified Sensor`
3. Upload the provided Arduino code to the ESP32.

### 2. Flask Server Setup:
1. Navigate to the flask_server directory.
2. Install dependencies:
  - `py -m pip install flask pandas`
  - `py -m pip install pandas`
3. Run the Flask server:
  - `python flask_server.py`
  - 
- Ensure your Flask server is running and accessible at the specified IP address.

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

## 📊 Live Dashboard
The Streamlit web application provides real-time visualizations of the temperature and humidity data collected by the ESP32.

Insert screenshot of the Streamlit dashboard here

---

## Software Architecture Diagram
The system architecture consists of three main components:

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
You can create a flowchart or diagram illustrating this architecture using tools like:

!image([https://github.com/DanTheProgrammerMan/IoT-Project-Hydroponics-ESP32/blob/main/Software-Architecture-Diagram_IoT.png])

---

## Security Considerations


## 📄 License

This project is licensed under the MIT License.

---

[![Runtime Tests](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/badge.svg)](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/RUNTIME_TESTS_REPORT.md)

#### Latest Stable Release

[![Release Version](https://img.shields.io/github/release/espressif/arduino-esp32.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)
[![Release Date](https://img.shields.io/github/release-date/espressif/arduino-esp32.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)
[![Downloads](https://img.shields.io/github/downloads/espressif/arduino-esp32/latest/total.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)


> [!NOTE]
> ESP32-C2 is also supported by Arduino-ESP32 but requires using Arduino as an ESP-IDF component or rebuilding the static libraries.
> For more information, see the [Arduino as an ESP-IDF component documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/esp-idf_component.html) or the
> [Lib Builder documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/lib_builder.html), respectively.
