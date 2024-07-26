#include <WiFi.h>

// WiFi Setting
const char* ssid = "addinedu_class_2 (2.4G)";
const char* password = "addinedu1";

// Server setting
WiFiServer server(80);

// Set a pin number for the IR sensor(TCRT5000)
#define TCRT5000_SENSOR_PIN 15

void setup() 
{
  // Begin Serial network
  Serial.begin(115200);

  // WiFi connection
  Serial.println("ESP32 TCP Server Start");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Set the sensor pin mod
  pinMode(TCRT5000_SENSOR_PIN, INPUT);

  // Start Server
  server.begin();
}

void loop() 
{
  // TCRT5000 센서 값 읽기
  int sensorValue = analogRead(TCRT5000_SENSOR_PIN);
  Serial.println(sensorValue);

  // // WiFi 연결 확인
  // if (WiFi.status() == WL_CONNECTED) 
  // {
  //   HTTPClient http;

  //   // 서버 시작
  //   http.begin(server);
  //   http.addHeader("Content-Type", "application/json");

  //   // JSON 데이터 생성
  //   StaticJsonDocument<200> jsonDoc;
  //   jsonDoc["sensor_value"] = sensorValue;

  //   // JSON 직렬화
  //   String requestBody;
  //   serializeJson(jsonDoc, requestBody);

  //   // HTTP POST 요청
  //   int httpResponseCode = http.POST(requestBody);

  //   if (httpResponseCode == 200) 
  //   {
  //     Serial.println("Data sent successfully");
  //   }
  //   else 
  //   {
  //     Serial.print("Failed to send data, error code: ");
  //     Serial.println(httpResponseCode);
  //   }

  //   // HTTP 연결 종료
  //   http.end();
  // } 
  // else 
  // {
  //   Serial.println("WiFi not connected");
  // }

  // // 주기적 데이터 전송을 위한 대기
  delay(1000);
}
