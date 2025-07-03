#include <DHT.h>
#include <DHT_U.h>
#include <Adafruit_Sensor.h>

#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT11.h>
// #include "esp_sleep.h"


#define DHTPIN 15
#define DHTTYPE DHT11

unsigned long startMillis = 0;

// #define uS_TO_S_FACTOR 1000000ULL  // Conversion factor for micro seconds to seconds
// #define TIME_TO_SLEEP 28            // Time ESP32 will go to sleep (in seconds)

const char* ssid = "WIFI_SSID_NAME";
const char* password = "WIFI_PASSWORD";
const char* serverName = "http://SERVER_IP_ADDRESS:5000/data"; // For Flask

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  startMillis = millis();  // Record the start time
}


void loop() {
  // Reads the Sensors every 60 seconds
  delay(60000);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT11 sensor!");
    return;
  }


  // Calculate uptime in hours:minutes:seconds
  unsigned long elapsedMillis = millis() - startMillis;
  unsigned long seconds = elapsedMillis / 1000;
  unsigned int hours = seconds / 3600;
  seconds = seconds % 3600;
  unsigned int minutes = seconds / 60;
  seconds = seconds % 60;

  char uptime[16];
  snprintf(uptime, sizeof(uptime), "%02u:%02u:%02lu", hours, minutes, seconds);


  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    if (!http.begin(serverName)) {
      Serial.println("HTTP begin failed");
      return;
    }

    http.addHeader("Content-Type", "application/json");

    String httpRequestData = "{\"temperature\": " + String(temperature) + ", \"humidity\": " + String(humidity) + ", \"uptime\": \"" + String(uptime) + "\"}";
    int httpResponseCode = http.POST(httpRequestData);


    Serial.print("DEBUG: Temperature(°C): ");
    Serial.println(temperature, 1); // Prints temperature with 1 decimal place
    
    Serial.print("DEBUG: Humidity(%): ");
    Serial.println(humidity, 1); // Prints temperature with 1 decimal place

    Serial.print("Uptime: ");
    Serial.println(uptime); // Prints the uptime string


    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  // ESP32 to enter Light Sleep Mode
    // Turn WiFi off to save more power before entering sleep mode
  // WiFi.disconnect(true);
  // WiFi.mode(WIFI_OFF);

    // Causing too many WiFi turn on/offs | Disabled for version 1
  // esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  // Serial.println("Entering light sleep for 28 seconds");
  // esp_light_sleep_start();
  // Serial.println("Woke up from light sleep");

}
