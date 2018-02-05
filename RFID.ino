/*
 * 
 * All the resources for this project: http://randomnerdtutorials.com/
 * Modified by Rui Santos
 * 
 * Created by FILIPEFLOP
 * 
 * Later modified for MangoHacks by Jake Harrison 
 */
 
#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  //Serial.println("Approximate your card to the reader...");
  //Serial.println();

}
void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  //Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     //Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  //Serial.println();
  
  content.toUpperCase();
  if (content.substring(1) == "04 C8 98 EA D0 4F 80"){ //UID for Jake
    Serial.println("1");
    delay(1000);
  }
  else if (content.substring(1) == "04 C1 98 EA D0 4F 80"){ //UID for Gabby
    Serial.println("2");
    delay(1000);
  }
  else if (content.substring(1) == "04 BD 96 EA D0 4F 80"){ //UID for Cody
    Serial.println("3");
    delay(1000);
  }
  else if (content.substring(1) == "04 2A 82 EA D0 4F 80"){ //UID for Kyle
    Serial.println("4");
    delay(1000);
  }
  else if (content.substring(1) == "E0 23 17 1B"){ //UID for master
    Serial.println("5");
    delay(1000);
  }
} 
