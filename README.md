# IoT ESP32 Temperature & Humidity Monitor Using Flask, StreamLit & Arduino IDE

This project utilizes an ESP32 microcontroller with a DHT11 sensor to monitor temperature and humidity levels. The data is sent to a Flask server for logging and analysis.

## Contents
- Documentation
- Hardware Components
- Wiring Diagram
- Installation & Setup Guide

<details>
  <summary>Click to expand</summary>

  Hidden content goes here.

</details>

| Feature   | Description         |
|-----------|---------------------|
| Fast      | Loads quickly       |
| Reliable  | Consistent results  |

- [x] Completed task
- [ ] Incomplete task

```python
def hello_world():
    print("Hello, world!")
```

## Documentation
Full setup documentation on the ESP32, Flask Server & StreamLit setup is available here.
- ESP32
- Flask Server
- StreamLit
[![Build Status]()]()
[![Verbose Build Status]()]()
[![External Libraries Test]()]()
[![Runtime Tests](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/badge.svg)](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/RUNTIME_TESTS_REPORT.md)

## 🧰 Hardware Components

- ESP32 Development Board
- DHT11 Temperature and Humidity Sensor
- 10kΩ Resistor
- Breadboard and Jumper Wires

## 🔌 Wiring Diagram
### Connect the components as follows:

- DHT11 VCC → 3.3V on ESP32
- DHT11 GND → GND on ESP32
- DHT11 Data → GPIO15 on ESP32
- Place a 10kΩ resistor between the Data and VCC lines of the DHT11 sensor.

Insert wiring diagram image here
![Circuit Diagram](images/circuit_diagram.png)


## 🚀 Installation & Setup Guide
### Prerequisites
- Python 3.7 or higher
- Arduino IDE configured for ESP32 development
- Required Python libraries:
  - Flask
  - Streamlit
  - Pandas

### Setup Guide
### 1. ESP32 Setup:
- Connect the DHT11 sensor to the ESP32 as per the wiring diagram.
- Open the Arduino IDE and install the necessary libraries:
  - `DHT sensor library`
  - `Adafruit Unified Sensor`
- Upload the provided Arduino code to the ESP32.

### 2. Flask Server Setup:
- Navigate to the flask_server directory.
- Install dependencies:
  - `py -m pip install flask pandas`
  - `py -m pip install pandas`
- Run the Flask server:
  - `python flask_server.py`

### 3. Streamlit Application Setup:
- Navigate to the streamlit_app directory.
- Install dependencies:
  - `py -m pip install streamlit pandas`
- Run the Streamlit app:
  - `streamlit run app.py`

- Ensure that the Flask server is running before starting the Streamlit application to allow real-time data visualisation.
  - Or you can refresh the StreamLit app

## 📊 Live Dashboard
The Streamlit web application provides real-time visualizations of the temperature and humidity data collected by the ESP32.

Insert screenshot of the Streamlit dashboard here

## 🧰 Setup Instructions

1. Connect the DHT11 sensor to the ESP32 as shown in the circuit diagram.
2. Upload the provided Arduino code to the ESP32.
3. Ensure your Flask server is running and accessible at the specified IP address.
4. Monitor the serial output for sensor readings and HTTP response codes.


## 🧠 Software Architecture Diagram
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

!image([https://github.com/DanTheProgrammerMan/IoT-Project-Hydroponics-ESP32/blob/main/Software-Architecture-Diagram_IoT.png])

## Visual Representation:
You can create a flowchart or diagram illustrating this architecture using tools like:

Lucidchart

draw.io (diagrams.net)

Canva

Embed the exported diagram in your README.md for clarity.

---

## 🔐 Security Considerations
Wi-Fi Security Protocols: The ESP32-WROOM-32 supports standard Wi-Fi security protocols, including WPA/WPA2. This ensures secure authentication and encryption for wireless communications.

#### Hardware Security Features:

Secure Boot: Ensures that only trusted firmware is executed by verifying the digital signature of the firmware during the boot process.

Flash Encryption: Protects sensitive data stored in flash memory by encrypting it, preventing unauthorized access.

Cryptographic Hardware Acceleration: The module includes hardware accelerators for cryptographic algorithms, enhancing performance and security for encryption/decryption operations.

Bluetooth Security: Supports Bluetooth security features, including Secure Simple Pairing and encryption, to protect data exchanged over Bluetooth connections.

---

## Local Device Protocols
Serial Communication (UART): The ESP32-WROOM-32 features multiple UART interfaces, enabling serial communication with peripherals such as sensors, actuators, and other microcontrollers. This facilitates tasks like data logging, debugging, and command interfacing.

SPI (Serial Peripheral Interface): SPI allows high-speed communication with devices like displays, memory chips, and sensors. The ESP32 supports multiple SPI interfaces, providing flexibility in connecting various peripherals.

I²C (Inter-Integrated Circuit): I²C is used for communication with devices like real-time clocks, EEPROMs, and other sensors. The ESP32 supports multiple I²C interfaces, allowing for efficient multi-device communication.

GPIO (General Purpose Input/Output): The module offers numerous GPIO pins that can be configured for digital input or output, enabling control over LEDs, buttons, and other digital devices.

PWM (Pulse Width Modulation): PWM is used for controlling devices like motors and LEDs by varying the duty cycle of digital signals. The ESP32's PWM capabilities allow for precise control over such devices.

ADC/DAC (Analog-to-Digital/Digital-to-Analog Converters): The ESP32 includes multiple ADC channels for reading analog signals from sensors and DAC channels for generating analog outputs.

## Wireless Protocols
Wi-Fi (2.4 GHz): The ESP32-WROOM-32 supports IEEE 802.11 b/g/n standards, enabling it to connect to Wi-Fi networks for internet access or local network communication. This is essential for IoT applications requiring cloud connectivity or remote monitoring.

Bluetooth: The module supports both Classic Bluetooth and Bluetooth Low Energy (BLE), allowing for communication with a wide range of Bluetooth-enabled devices, such as smartphones, tablets, and other microcontrollers.

---

## 📡 Connectivity Type
Wi-Fi (2.4 GHz): The ESP32-WROOM-32 supports IEEE 802.11 b/g/n standards, operating in the 2.4 GHz frequency band. This enables the module to connect to standard Wi-Fi networks, facilitating internet access and local network communication.

Bluetooth 4.2 (Classic and BLE): The module also supports Bluetooth v4.2, including both Basic Rate/Enhanced Data Rate (BR/EDR) and Bluetooth Low Energy (BLE) modes. This allows for short-range wireless communication with other Bluetooth-enabled devices.

## 📶 Bandwidth Requirements
Wi-Fi Throughput: The ESP32-WROOM-32 can achieve data rates up to 150 Mbps under optimal conditions when using the 802.11n standard. However, actual throughput will depend on factors such as signal strength, network congestion, and environmental interference.

Application Considerations: For typical IoT applications like sensor data transmission, bandwidth requirements are modest, often well within the capabilities of the ESP32's Wi-Fi performance. For more demanding applications, such as streaming audio or video, higher bandwidth and stable connections are necessary.

---



## 📄 License

This project is licensed under the MIT License.

---
---
---


# Arduino core for the ESP32, ESP32-C3, ESP32-C6, ESP32-H2, ESP32-P4, ESP32-S2 and ESP32-S3.

[![Build Status](https://img.shields.io/github/actions/workflow/status/espressif/arduino-esp32/push.yml?branch=master&event=push&label=Compilation%20Tests)](https://github.com/espressif/arduino-esp32/actions/workflows/push.yml?query=branch%3Amaster+event%3Apush)
[![Verbose Build Status](https://img.shields.io/github/actions/workflow/status/espressif/arduino-esp32/push.yml?branch=master&event=schedule&label=Compilation%20Tests%20(Verbose))](https://github.com/espressif/arduino-esp32/actions/workflows/push.yml?query=branch%3Amaster+event%3Aschedule)
[![External Libraries Test](https://img.shields.io/github/actions/workflow/status/espressif/arduino-esp32/lib.yml?branch=master&event=schedule&label=External%20Libraries%20Test)](https://github.com/espressif/arduino-esp32/blob/gh-pages/LIBRARIES_TEST.md)
[![Runtime Tests](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/badge.svg)](https://github.com/espressif/arduino-esp32/blob/gh-pages/runtime-tests-results/RUNTIME_TESTS_REPORT.md)


## Contents

  - [Development Status](#development-status)
  - [Development Planning](#development-planning)
  - [Documentation](#documentation)
  - [Supported Chips](#supported-chips)
  - [Decoding exceptions](#decoding-exceptions)
  - [Issue/Bug report template](#issuebug-report-template)
  - [Contributing](#contributing)

### Development Status

#### Latest Stable Release

[![Release Version](https://img.shields.io/github/release/espressif/arduino-esp32.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)
[![Release Date](https://img.shields.io/github/release-date/espressif/arduino-esp32.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)
[![Downloads](https://img.shields.io/github/downloads/espressif/arduino-esp32/latest/total.svg)](https://github.com/espressif/arduino-esp32/releases/latest/)


> [!NOTE]
> ESP32-C2 is also supported by Arduino-ESP32 but requires using Arduino as an ESP-IDF component or rebuilding the static libraries.
> For more information, see the [Arduino as an ESP-IDF component documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/esp-idf_component.html) or the
> [Lib Builder documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/lib_builder.html), respectively.
