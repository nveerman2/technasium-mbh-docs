# Arduino Programmeren – Basisbegrippen

Arduino-programmeren maakt gebruik van een op C/C++ gebaseerde taal, maar met eenvoudige functies en bibliotheken die specifiek zijn voor het Arduino-platform. Dit maakt het gemakkelijk te begrijpen, zelfs voor beginners.  

Het leren van programmeren in Arduino is als het leren van een nieuwe taal, zoals Frans. Net zoals bij Frans zijn spelling en grammatica belangrijk in programmeren. De "woorden" in de code kun je opzoeken in een "woordenboek" zoals de Arduino-documentatie.  

Laten we eens kijken naar enkele belangrijke onderdelen in een code.

---

## Variabelen

Variabelen worden gebruikt om gegevens op te slaan en te manipuleren. Er zijn verschillende soorten variabelen, zoals `int`, `float`, `char`, etc.  

- **int**: gebruikt voor het opslaan van gehele getallen (integers).  
  **Voorbeeld:**
  ```cpp
  int ledPin = 13;
  ```
- **const int**: gebruikt voor gehele getallen die in het programma niet veranderen (constant).  
  **Voorbeeld:**
  ```cpp
  const int ledRood = 12;
  ```
- **float**: gebruikt voor het opslaan van kommagetallen (floating point).  
  **Voorbeeld:**
  ```cpp
  float voltage = 5.0;
  ```
- **char**: gebruikt voor het opslaan van individuele tekens (characters).  
  **Voorbeeld:**
  ```cpp
  char letter = 'A';
  ```

In de opdrachten gebruik je `int` om de pinnummers van de LEDs op te slaan. Zo kun je de naam `ledPin` gebruiken in de code in plaats van het getal `13`. Dit maakt de code makkelijker te lezen.  

In **Tinkercad** kun je, als je met blokken werkt, variabelen aanmaken onder *Variabelen*.  

---

## De `setup()` functie

De `setup()` functie wordt slechts eenmaal uitgevoerd wanneer het programma begint.  
Het wordt gebruikt voor de begininstellingen, zoals het instellen van pinnen als invoer of uitvoer.  

**Voorbeeld:**
```cpp
void setup() {
  pinMode(ledPin, OUTPUT);
}
```

---

## De `loop()` functie

De `loop()` functie wordt continu herhaald nadat de `setup()` functie is uitgevoerd.  
Hier worden de hoofdactiviteiten van het programma uitgevoerd, zoals het controleren van sensoren en het aansturen van LEDs.  

**Voorbeeld:**
```cpp
void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

---

## Comments (Opmerkingen)

Comments zijn stukjes tekst in de code die door de Arduino worden genegeerd.  
Ze worden gebruikt om uitleg toe te voegen aan de code voor de programmeur.  

Je herkent ze aan:
- `//` voor een enkele regel commentaar  
- `/* ... */` voor meerdere regels commentaar  

**Voorbeeld:**
```cpp
/*
Hiertussen kunnen meerdere regels
commentaar komen te staan
*/

// Definieer de pinnen voor de LEDs
int ledPin1 = 13; // Pin voor de eerste LED
int ledPin2 = 12; // Pin voor de tweede LED
```
