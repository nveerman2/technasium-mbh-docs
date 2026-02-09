# Drukknop en Arduino

Een **drukknop** (push button) is een eenvoudige schakelaar die wordt gebruikt om een elektrisch signaal te onderbreken of te maken.  
Wanneer je de knop indrukt, wordt de verbinding gesloten en kan de Arduino dit detecteren.  

Drukknoppen worden vaak gebruikt als **invoer** om acties te starten, zoals het aanzetten van een LED, het starten van een motor of het doorlopen van een programma.  

---

## Aansluiten van een drukknop

Een drukknop heeft meestal **twee pootjes** (soms vier, waarvan steeds twee verbonden zijn).  
De aansluitingen gaan vaak als volgt:  
- Eén kant van de knop → **digitale pin** van de Arduino.  
- De andere kant van de knop → **GND**.  
- Daarnaast gebruik je vaak een **pull-down weerstand** (bijv. 10kΩ) tussen de digitale pin en GND om te voorkomen dat de pin willekeurige waarden leest als de knop niet is ingedrukt. 

> Tip: Je kunt ook de **interne pull-up weerstand** van de Arduino gebruiken (minder bedrading nodig). In dat geval sluit je de knop tussen de digitale pin en **GND** en activeer je de interne pull-up in de code met `INPUT_PULLUP`. Hierdoor staat de pin standaard op **HIGH**. Als je de knop indrukt (verbonden met **GND**), leest de Arduino **LOW**.  

---

## Voorbeeld: LED aansturen met een drukknop

### Schakeling (met pull-down weerstand)
- Drukknop → pin 2 en GND  
- LED → pin 13 (met serieweerstand 220Ω naar GND)  

![drukknop](../../../img/vaardigheden/arduino/drukknop_led.png)

### Code

```cpp
const int buttonPin = 2;    // pin waar de drukknop op is aangesloten
const int ledPin = 13;      // pin waar de LED op is aangesloten

int buttonState = 0;        // variabele om de knopstatus op te slaan

void setup() {
  pinMode(buttonPin, INPUT); // gebruik externe pull-down weerstand
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Lees de status van de knop
  buttonState = digitalRead(buttonPin);

  // Als de knop is ingedrukt (HIGH door pull-down)
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH); // zet de LED aan
  } else {
    digitalWrite(ledPin, LOW);  // zet de LED uit
  }
}
```

---

## Uitleg

- De **drukknop** werkt als een schakelaar die de verbinding maakt naar GND.    
- Wanneer de knop wordt ingedrukt, verandert de waarde naar **HIGH**.  
- In dit voorbeeld gaat de LED aan als de knop wordt ingedrukt en weer uit als je loslaat.  

---
