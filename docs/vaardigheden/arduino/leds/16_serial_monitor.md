# Serial Monitor

De Serial Monitor in Arduino is een tool waarmee je communicatie tussen je Arduino-board en je computer kunt bekijken. Het laat je berichten verzenden vanaf je Arduino naar de computer, zodat je ze kunt lezen op je scherm.  

In eenvoudige bewoordingen, stel je voor dat je Arduino praat en de Serial Monitor is als een luisterend oor dat je helpt te begrijpen wat de Arduino zegt.  

Om de Serial Monitor te gebruiken, moet je eerst de `Serial.begin()` functie in je `setup()` functie opnemen, zoals in het voorbeeld hieronder:

```cpp
void setup() {
  Serial.begin(9600); // Start de communicatie met de Serial Monitor op een baudrate van 9600
}
```

Daarna kun je berichten vanuit je Arduino naar de Serial Monitor sturen met de `Serial.print()` of `Serial.println()` functies:

```cpp
Serial.print("Dit is een stuk tekst dat naar de Serial Monitor wordt gestuurd.");
Serial.println(42); // Je kunt ook variabelen afdrukken, println start een nieuwe regel
```

Als je dit uploadt naar je Arduino en de Serial Monitor opent (zie onderstaande afbeeldingen), zul je deze berichten op je computerscherm zien verschijnen.  

Het is een handige tool om te gebruiken bij het debuggen van je code en om te begrijpen wat er gebeurt in je Arduino-projecten!  

![serialmonitor](../../../img/vaardigheden/arduino/serialmonitor.png)

*links de Serial Monitor in Tinkercad en rechts in de Arduino IDE*