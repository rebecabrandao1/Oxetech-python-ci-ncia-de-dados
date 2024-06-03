#include "dht.h" 

const int dhtpin = 7; 

dht DHT; 

void setup(){
  Serial.begin(9600); 
  delay(2000);
}

void loop(){
  DHT.read11(dhtpin); 
  Serial.print("Umidade: "); 
  Serial.print(DHT.humidity); 
  Serial.print("%"); 
  Serial.print(" / Temperatura: ");
  Serial.print(DHT.temperature, 0); 
  Serial.println("*C"); 
  delay(2000); 
}