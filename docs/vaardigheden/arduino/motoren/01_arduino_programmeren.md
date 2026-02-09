# Programmeren in Arduino

Arduino-programmeren maakt gebruik van een op C/C++ gebaseerde taal, maar met eenvoudige functies en bibliotheken die specifiek zijn voor het Arduino-platform. Dit maakt het gemakkelijk te begrijpen, zelfs voor beginners. 

Het leren van programmeren in Arduino is als het leren van een nieuwe taal, zoals Frans. Net zoals bij Frans zijn spelling en grammatica belangrijk in programmeren. De "woorden" in de code kunnen worden opgezocht in een "woordenboek" zoals de Arduino-documentatie. Laten we eens kijken naar enkele belangrijke onderdelen in een code.

---

## void setup()

De `setup()` functie wordt slechts eenmaal uitgevoerd wanneer het programma begint. Het wordt gebruikt voor de begininstellingen, zoals het instellen van pinnen als invoer of uitvoer. Hier is een voorbeeld van `void setup()`:

```cpp
void setup() {
  pinMode(ledPin, OUTPUT);
}
```

---

## void loop()

De `loop()` functie wordt continu herhaald nadat de `setup()` functie is uitgevoerd. Hier worden de hoofdactiviteiten van het programma uitgevoerd, zoals het controleren van sensoren, het aansturen van LEDs, enzovoort. Hier is een voorbeeld van `void loop()`:

```cpp
void loop(){
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

---

## Comments

Comments (opmerkingen) zijn stukjes tekst in de code die worden genegeerd door de Arduino. Ze worden gebruikt om uitleg toe te voegen aan de code voor de programmeur. Comments kunnen worden herkend aan het dubbele schuine streepje `//` voor een enkele regel commentaar, of aan `/* */` voor meerdere regels commentaar.  

Bijvoorbeeld:

```cpp
/*
Hiertussen kunnen meerdere regels
commentaar komen te staan
*/

// Definieer de pinnen voor de LEDs
int ledPin1 = 13; // Pin voor de eerste LED
int ledPin2 = 12; // Pin voor de tweede LED
```

## Variabelen

Variabelen worden gebruikt om gegevens op te slaan en te manipuleren. Er zijn verschillende soorten variabelen, zoals int, float, char, etc. 

- **int**: Gebruikt voor het opslaan van gehele getallen (integer).  
- **const int**: Gebruikt voor gehele getallen die in het programma niet veranderen (constant)  
  
  Bijvoorbeeld:  

  ```cpp
  int ledPin = 13;
  const int ledRood = 12;
  ```

- **float**: Gebruikt voor het opslaan van kommagetallen (floating point).  
  Bijvoorbeeld:  

  ```cpp
  float voltage = 5.0;
  ```

- **char**: Gebruikt voor het opslaan van individuele tekens (characters).  
  Bijvoorbeeld:  

  ```cpp
  char letter = 'A';
  ```

In de opdrachten gaan we bijvoorbeeld gebruiken **int** om de pinnummers van de LEDs op te slaan. Zo kunnen we de naam `ledPin` gebruiken in de code in plaats van het getal 13. Dit maakt de code makkelijker te lezen.

In Tinkercad kun je, als je met blokken werkt, variabelen aanmaken onder *Variabelen*.

---